# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "TaskRetrieveResponse",
    "Pending",
    "PendingEstimatedCost",
    "Throttled",
    "ThrottledEstimatedCost",
    "Cancelled",
    "CancelledCost",
    "Running",
    "RunningEstimatedCost",
    "Failed",
    "FailedCost",
    "Succeeded",
    "SucceededCost",
]


class PendingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class Pending(BaseModel):
    """A pending task"""

    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    estimated_cost: PendingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    status: Literal["PENDING"]


class ThrottledEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class Throttled(BaseModel):
    """A throttled task"""

    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    estimated_cost: ThrottledEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    status: Literal["THROTTLED"]


class CancelledCost(BaseModel):
    """Final cost in credits for a terminal task. A refunded task reports 0."""

    credits: int
    """Credits charged for this task."""


class Cancelled(BaseModel):
    """A cancelled or deleted task"""

    id: str
    """The ID of the task being returned."""

    cost: CancelledCost
    """Final cost in credits for a terminal task. A refunded task reports 0."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    status: Literal["CANCELLED"]


class RunningEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class Running(BaseModel):
    """A running task"""

    id: str
    """The ID of the task being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    estimated_cost: RunningEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    progress: float

    status: Literal["RUNNING"]


class FailedCost(BaseModel):
    """Final cost in credits for a terminal task. A refunded task reports 0."""

    credits: int
    """Credits charged for this task."""


class Failed(BaseModel):
    """A failed task"""

    id: str
    """The ID of the task being returned."""

    cost: FailedCost
    """Final cost in credits for a terminal task. A refunded task reports 0."""

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


class SucceededCost(BaseModel):
    """Final cost in credits for a terminal task. A refunded task reports 0."""

    credits: int
    """Credits charged for this task."""


class Succeeded(BaseModel):
    """A succeeded task"""

    id: str
    """The ID of the task being returned."""

    cost: SucceededCost
    """Final cost in credits for a terminal task. A refunded task reports 0."""

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
