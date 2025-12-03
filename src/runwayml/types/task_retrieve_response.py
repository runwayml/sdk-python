# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["TaskRetrieveResponse", "Pending", "Throttled", "Cancelled", "Running", "Failed", "Succeeded"]


class Pending(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    status: Literal["PENDING"]


class Throttled(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    status: Literal["THROTTLED"]


class Cancelled(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    status: Literal["CANCELLED"]


class Running(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    progress: float

    status: Literal["RUNNING"]


class Failed(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    failure: str
    """A human-friendly reason for the failure.

    We do not recommend returning this to users directly without adding context.
    """

    status: Literal["FAILED"]

    failure_code: Optional[str] = FieldInfo(alias="failureCode", default=None)
    """A machine-readable error code for the failure.

    See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
    """


class Succeeded(BaseModel):
    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    output: List[str]
    """An array of URLs that return the output of the task.

    These URLs will expire within 24-48 hours; fetch the task again to get fresh
    URLs. It is expected that you download the assets at these URLs and store them
    in your own storage system.
    """

    status: Literal["SUCCEEDED"]


TaskRetrieveResponse: TypeAlias = Annotated[
    Union[Pending, Throttled, Cancelled, Running, Failed, Succeeded], PropertyInfo(discriminator="status")
]
