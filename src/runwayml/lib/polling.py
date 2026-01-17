import time
import random
from typing import TYPE_CHECKING, Type, Union, TypeVar, Callable, Annotated, Coroutine, cast
from typing_extensions import ParamSpec, TypeAlias

import anyio

from runwayml._utils import PropertyInfo

from .._models import BaseModel
from ..types.task_retrieve_response import (
    Failed,
    Pending,
    Running,
    Cancelled,
    Succeeded,
    Throttled,
    TaskRetrieveResponse,
)

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


class AwaitablePending(AwaitableTaskResponseMixin, Pending): ...


class AwaitableThrottled(AwaitableTaskResponseMixin, Throttled): ...


class AwaitableCancelled(AwaitableTaskResponseMixin, Cancelled): ...


class AwaitableRunning(AwaitableTaskResponseMixin, Running): ...


class AwaitableFailed(AwaitableTaskResponseMixin, Failed): ...


class AwaitableSucceeded(AwaitableTaskResponseMixin, Succeeded): ...


AwaitableTaskRetrieveResponse: TypeAlias = Annotated[
    Union[
        AwaitablePending, AwaitableThrottled, AwaitableCancelled, AwaitableRunning, AwaitableFailed, AwaitableSucceeded
    ],
    PropertyInfo(discriminator="status"),
]


class AsyncAwaitablePending(AsyncAwaitableTaskResponseMixin, Pending): ...


class AsyncAwaitableThrottled(AsyncAwaitableTaskResponseMixin, Throttled): ...


class AsyncAwaitableCancelled(AsyncAwaitableTaskResponseMixin, Cancelled): ...


class AsyncAwaitableRunning(AsyncAwaitableTaskResponseMixin, Running): ...


class AsyncAwaitableFailed(AsyncAwaitableTaskResponseMixin, Failed): ...


class AsyncAwaitableSucceeded(AsyncAwaitableTaskResponseMixin, Succeeded): ...


AsyncAwaitableTaskRetrieveResponse: TypeAlias = Annotated[
    Union[
        AsyncAwaitablePending,
        AsyncAwaitableThrottled,
        AsyncAwaitableCancelled,
        AsyncAwaitableRunning,
        AsyncAwaitableFailed,
        AsyncAwaitableSucceeded,
    ],
    PropertyInfo(discriminator="status"),
]


def _make_sync_wait_for_task_output(
    client: "RunwayML",
) -> Callable[["AwaitableTaskResponseMixin", Union[float, None]], TaskRetrieveResponse]:
    """Create a wait_for_task_output method bound to the given client."""

    def wait_for_task_output(
        self: "AwaitableTaskResponseMixin", timeout: Union[float, None] = 60 * 10
    ) -> TaskRetrieveResponse:
        start_time = time.time()
        while True:
            time.sleep(POLL_TIME + random.random() * POLL_JITTER - POLL_JITTER / 2)
            task_details = client.tasks.retrieve(self.id)  # type: ignore[attr-defined]
            if task_details.status == "SUCCEEDED":
                return task_details
            if task_details.status == "FAILED":
                raise TaskFailedError(task_details)
            if timeout is not None and time.time() - start_time > timeout:
                raise TaskTimeoutError(task_details)

    return wait_for_task_output


def inject_sync_wait_method(client: "RunwayML", response: T) -> T:
    """Inject the wait_for_task_output method onto the response instance."""
    import types

    response.wait_for_task_output = types.MethodType(_make_sync_wait_for_task_output(client), response)  # type: ignore[attr-defined]
    return response


def _make_async_wait_for_task_output(
    client: "AsyncRunwayML",
) -> Callable[["AsyncAwaitableTaskResponseMixin", Union[float, None]], Coroutine[None, None, TaskRetrieveResponse]]:
    """Create an async wait_for_task_output method bound to the given client."""

    async def wait_for_task_output(
        self: "AsyncAwaitableTaskResponseMixin", timeout: Union[float, None] = 60 * 10
    ) -> TaskRetrieveResponse:
        start_time = anyio.current_time()
        while True:
            await anyio.sleep(POLL_TIME + random.random() * POLL_JITTER - POLL_JITTER / 2)
            task_details = await client.tasks.retrieve(self.id)  # type: ignore[attr-defined]
            if task_details.status == "SUCCEEDED":
                return task_details
            if task_details.status == "FAILED" or task_details.status == "CANCELLED":
                raise TaskFailedError(task_details)
            if timeout is not None and anyio.current_time() - start_time > timeout:
                raise TaskTimeoutError(task_details)

    return wait_for_task_output


def inject_async_wait_method(client: "AsyncRunwayML", response: T) -> T:
    """Inject the async wait_for_task_output method onto the response instance."""
    import types

    response.wait_for_task_output = types.MethodType(_make_async_wait_for_task_output(client), response)  # type: ignore[attr-defined]
    return response
