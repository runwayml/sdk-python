# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebappListUsageResponse"]


class WebappListUsageResponse(BaseModel):
    credits: float
    """Credits charged for this generation."""

    email: str
    """Email of the user who generated."""

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """ID of the generation this row belongs to.

    A charge and its refunds share it. `null` for App Studio usage, which has no
    generation.
    """

    timestamp: datetime
    """When the generation was charged."""

    tool: str
    """Model/task display name for the generation."""

    transaction_id: str = FieldInfo(alias="transactionId")
    """Unique ID of the credit transaction behind this row.

    Stable across requests, so use it to deduplicate overlapping pulls.
    """

    type: Literal["charge", "refund"]
    """
    Whether the row is a credit charge for a generation or a task refund (negative
    credits).
    """

    unit: Literal["credits"]
    """Unit of `credits`. Always `credits`."""

    user_id: int = FieldInfo(alias="userId")
    """ID of the user who generated."""

    workspace_id: int = FieldInfo(alias="workspaceId")
    """ID of the owning workspace."""

    workspace_name: str = FieldInfo(alias="workspaceName")
    """Name of the owning workspace."""
