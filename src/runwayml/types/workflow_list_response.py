# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowListResponse", "Data", "DataVersion"]


class DataVersion(BaseModel):
    """A specific published version of a workflow."""

    id: str
    """The globally unique ID of this published workflow version."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When this version was published"""

    version: int
    """A monotonically increasing version number.

    Each workflow version for the same published workflow has a unique version
    number.
    """


class Data(BaseModel):
    """A published workflow with all its available versions."""

    name: str
    """The name of the published workflow."""

    versions: List[DataVersion]
    """The published versions of this workflow, newest first."""


class WorkflowListResponse(BaseModel):
    data: List[Data]
    """A list of published workflows grouped by source workflow."""
