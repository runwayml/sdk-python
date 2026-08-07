# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    timestamp: datetime
    """When the generation was charged."""

    tool: str
    """Model/task display name for the generation."""

    type: Literal["charge", "refund"]
    """
    Whether the row is a credit charge for a generation or a task refund (negative
    credits).
    """

    workspace_id: int = FieldInfo(alias="workspaceId")
    """ID of the owning workspace."""

    workspace_name: str = FieldInfo(alias="workspaceName")
    """Name of the owning workspace."""
