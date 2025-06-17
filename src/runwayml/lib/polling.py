import time
import random
from typing import TYPE_CHECKING, Type, Union, TypeVar, cast
from typing_extensions import ParamSpec

import anyio

from .._models import BaseModel
from ..types.task_retrieve_response import TaskRetrieveResponse

if TYPE_CHECKING:
    from .._client import RunwayML, AsyncRunwayML

P = ParamSpec("P")
T = TypeVar("T")

POLL_TIME = 6
POLL_JITTER = 3


class AwaitableTaskResponseMixin:
    def wait_for_task_output(self, timeout: Union[float, None] = 60 * 10) -> TaskRetrieveResponse:  # type: ignore[empty-body]
        """
        When called, this will block until the task is complete.

        If the task fails or is cancelled, a `TaskFailedError` will be raised.

        Args:
          timeout: The maximum amount of time to wait for the task to complete in seconds. If not
              specified, the default timeout is 10 minutes. Will raise a `TaskTimeoutError` if the
              task does not complete within the timeout.

        Returns:
          The task details, equivalent to calling `client.tasks.retrieve(task_id)`.
        """
        ...


class NewTaskCreatedResponse(AwaitableTaskResponseMixin, BaseModel):
    id: str


class AwaitableTaskRetrieveResponse(AwaitableTaskResponseMixin, TaskRetrieveResponse):
    pass


class AsyncAwaitableTaskResponseMixin:
    async def wait_for_task_output(self, timeout: Union[float, None] = 60 * 10) -> TaskRetrieveResponse:  # type: ignore[empty-body]
        """
        When called, this will wait until the task is complete.

        If the task fails or is cancelled, a `TaskFailedError` will be raised.

        Args:
          timeout: The maximum amount of time to wait for the task to complete in seconds. If not
              specified, the default timeout is 10 minutes. Will raise a `TaskTimeoutError` if the
              task does not complete within the timeout. Setting this to `None` will wait
              indefinitely (disabling the timeout).

        Returns:
          The task details, equivalent to awaiting `client.tasks.retrieve(task_id)`.
        """
        ...


class AsyncNewTaskCreatedResponse(AsyncAwaitableTaskResponseMixin, BaseModel):
    id: str


class AsyncAwaitableTaskRetrieveResponse(AsyncAwaitableTaskResponseMixin, TaskRetrieveResponse):
    pass


def create_waitable_resource(base_class: Type[T], client: "RunwayML") -> Type[NewTaskCreatedResponse]:
    class WithClient(base_class):  # type: ignore[valid-type,misc]
        id: str

        def wait_for_task_output(self, timeout: Union[float, None] = 60 * 10) -> TaskRetrieveResponse:
            start_time = time.time()
            while True:
                time.sleep(POLL_TIME + random.random() * POLL_JITTER - POLL_JITTER / 2)
                task_details = client.tasks.retrieve(self.id)
                if task_details.status == "SUCCEEDED":
                    return task_details
                if task_details.status == "FAILED":
                    raise TaskFailedError(task_details)
                if timeout is not None and time.time() - start_time > timeout:
                    raise TaskTimeoutError(task_details)

    WithClient.__name__ = base_class.__name__
    WithClient.__qualname__ = base_class.__qualname__

    return cast(Type[NewTaskCreatedResponse], WithClient)


def create_async_waitable_resource(base_class: Type[T], client: "AsyncRunwayML") -> Type[AsyncNewTaskCreatedResponse]:
    class WithClient(base_class):  # type: ignore[valid-type,misc]
        id: str

        async def wait_for_task_output(self, timeout: Union[float, None] = 60 * 10) -> TaskRetrieveResponse:
            start_time = anyio.current_time()
            while True:
                await anyio.sleep(POLL_TIME + random.random() * POLL_JITTER - POLL_JITTER / 2)
                task_details = await client.tasks.retrieve(self.id)
                if task_details.status == "SUCCEEDED":
                    return task_details
                if task_details.status == "FAILED" or task_details.status == "CANCELLED":
                    raise TaskFailedError(task_details)
                if timeout is not None and anyio.current_time() - start_time > timeout:
                    raise TaskTimeoutError(task_details)

    WithClient.__name__ = base_class.__name__
    WithClient.__qualname__ = base_class.__qualname__

    return cast(Type[AsyncNewTaskCreatedResponse], WithClient)


class TaskFailedError(Exception):
    def __init__(self, task_details: TaskRetrieveResponse):
        self.task_details = task_details
        super().__init__(f"Task failed")


class TaskTimeoutError(Exception):
    def __init__(self, task_details: TaskRetrieveResponse):
        self.task_details = task_details
        super().__init__(f"Task timed out")
