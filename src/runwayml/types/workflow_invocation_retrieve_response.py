# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "WorkflowInvocationRetrieveResponse",
    "Pending",
    "Throttled",
    "Cancelled",
    "Running",
    "RunningNodeErrors",
    "Failed",
    "FailedNodeErrors",
    "Succeeded",
    "SucceededNodeErrors",
]


class Pending(BaseModel):
    """A pending workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    status: Literal["PENDING"]


class Throttled(BaseModel):
    """A throttled workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    status: Literal["THROTTLED"]


class Cancelled(BaseModel):
    """A cancelled or deleted workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    status: Literal["CANCELLED"]


class RunningNodeErrors(BaseModel):
    message: str
    """A human-readable description of the node error."""

    node_name: Optional[str] = FieldInfo(alias="nodeName", default=None)
    """The human-readable name of the node that errored."""


class Running(BaseModel):
    """A running workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    output: Dict[str, List[str]]
    """
    A record mapping workflow node IDs to arrays of output URLs for nodes that have
    already completed. This allows streaming partial results while the workflow is
    still running.
    """

    progress: float
    """A number between 0 and 1 representing the overall workflow execution progress."""

    status: Literal["RUNNING"]

    node_errors: Optional[Dict[str, RunningNodeErrors]] = FieldInfo(alias="nodeErrors", default=None)
    """A record mapping workflow node IDs to their error details.

    Only present when one or more nodes have errored.
    """


class FailedNodeErrors(BaseModel):
    message: str
    """A human-readable description of the node error."""

    node_name: Optional[str] = FieldInfo(alias="nodeName", default=None)
    """The human-readable name of the node that errored."""


class Failed(BaseModel):
    """A failed workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    failure: str
    """A human-friendly reason for the failure.

    We do not recommend returning this to users directly without adding context.
    """

    status: Literal["FAILED"]

    failure_code: Optional[str] = FieldInfo(alias="failureCode", default=None)
    """A machine-readable error code for the failure.

    See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
    """

    node_errors: Optional[Dict[str, FailedNodeErrors]] = FieldInfo(alias="nodeErrors", default=None)
    """A record mapping workflow node IDs to their error details.

    Only present when one or more nodes have errored.
    """


class SucceededNodeErrors(BaseModel):
    message: str
    """A human-readable description of the node error."""

    node_name: Optional[str] = FieldInfo(alias="nodeName", default=None)
    """The human-readable name of the node that errored."""


class Succeeded(BaseModel):
    """A succeeded workflow invocation"""

    id: str
    """The ID of the workflow invocation being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the workflow invocation was submitted at."""

    output: Dict[str, List[str]]
    """A record mapping workflow node IDs to arrays of output URLs.

    Each key is the UUID of a workflow node that produced output, and each value is
    an array of URLs for that node's artifacts. These URLs will expire within 24-48
    hours; fetch the invocation again to get fresh URLs. It is expected that you
    download the assets at these URLs and store them in your own storage system.
    """

    status: Literal["SUCCEEDED"]

    node_errors: Optional[Dict[str, SucceededNodeErrors]] = FieldInfo(alias="nodeErrors", default=None)
    """A record mapping workflow node IDs to their error details.

    Even when the overall workflow succeeds, individual nodes may have encountered
    non-fatal errors. Only present when one or more nodes have errored.
    """


WorkflowInvocationRetrieveResponse: TypeAlias = Annotated[
    Union[Pending, Throttled, Cancelled, Running, Failed, Succeeded], PropertyInfo(discriminator="status")
]
