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

    output_count: Optional[int] = FieldInfo(alias="outputCount", default=None)
    """
    Number of output files the generation returned, including ones the user later
    deleted and excluding attachments such as playable proxies. Copying an output
    into a project can raise it. 0 when it returned no files, for example while it
    runs or after it failed. `null` when `taskId` is null or the generation no
    longer exists.
    """

    output_type: Optional[
        Literal["image", "video", "text", "file", "audio", "font", "model", "project", "mesh", "cloud", "splat"]
    ] = FieldInfo(alias="outputType", default=None)
    """
    Media type of the generation's output: one of the listed values, which won't be
    remapped. Agent sandbox sessions report `file`. `null` when `taskId` is null,
    the generation no longer exists, or the type wasn't recorded.
    """

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """
    ID of the Runway web app project the generation was made in (not this API
    project). `null` when no project is recorded for it, which includes generations
    made outside a project, generations made before project tracking was rolled out
    (late May to mid-August 2026), and rows with a null `taskId`.
    """

    project_name: Optional[str] = FieldInfo(alias="projectName", default=None)
    """
    Current name of that project, so it changes when the project is renamed (group
    by `projectId`). Still returned after the project is archived or deleted. `null`
    when `projectId` is null.
    """

    status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", "FAILED", "SUCCEEDED", "CANCELLED"]] = None
    """
    Current status of the generation when you request it, so it can change between
    pulls (upsert on `transactionId`). A refund row doesn't mean the generation
    failed. `null` when `taskId` is null or the generation no longer exists.
    """

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
