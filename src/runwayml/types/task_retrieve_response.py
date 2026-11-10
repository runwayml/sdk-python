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
    "SucceededLayer",
    "SucceededLayerBoundingBox",
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
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits report what remains charged.
    """

    credits: int
    """Credits charged for this task."""


class Cancelled(BaseModel):
    """A cancelled or deleted task"""

    id: str
    """The ID of the task being returned."""

    cost: CancelledCost
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits
    report what remains charged.
    """

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
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits report what remains charged.
    """

    credits: int
    """Credits charged for this task."""


class Failed(BaseModel):
    """A failed task"""

    id: str
    """The ID of the task being returned."""

    cost: FailedCost
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits
    report what remains charged.
    """

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
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits report what remains charged.
    """

    credits: int
    """Credits charged for this task."""


class SucceededLayerBoundingBox(BaseModel):
    """
    The layer bounds in absolute and normalized coordinates, when returned by the model provider.
    """

    absolute: List[float]

    normalized: List[float]


class SucceededLayer(BaseModel):
    uri: str
    """An ephemeral URL for this layer, matching output at the same index."""

    bounding_box: Optional[SucceededLayerBoundingBox] = FieldInfo(alias="boundingBox", default=None)
    """
    The layer bounds in absolute and normalized coordinates, when returned by the
    model provider.
    """

    name: Optional[str] = None
    """The layer filename."""

    z_index: Optional[float] = FieldInfo(alias="zIndex", default=None)
    """The layer stacking order returned by the model provider."""


class Succeeded(BaseModel):
    """A succeeded task"""

    id: str
    """The ID of the task being returned."""

    cost: SucceededCost
    """Final cost in credits for a terminal task.

    Fully refunded tasks report 0; tasks that later returned unused prepaid credits
    report what remains charged.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    output: List[str]
    """An array of URLs that return the output of the task.

    These URLs will expire within 24-48 hours; fetch the task again to get fresh
    URLs. It is expected that you download the assets at these URLs and store them
    in your own storage system.
    """

    status: Literal["SUCCEEDED"]

    layers: Optional[List[SucceededLayer]] = None
    """Layer details for successful Seedream 5 Pro Layers tasks.

    Each URI matches the output URL at the same index.
    """


TaskRetrieveResponse: TypeAlias = Annotated[
    Union[Pending, Throttled, Cancelled, Running, Failed, Succeeded], PropertyInfo(discriminator="status")
]
