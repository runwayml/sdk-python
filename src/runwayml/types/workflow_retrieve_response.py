# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowRetrieveResponse", "Graph"]


class Graph(BaseModel):
    """The workflow graph definition."""

    edges: List[object]
    """The list of edges connecting nodes in the workflow graph.

    Each edge defines data flow between nodes.
    """

    nodes: List[object]
    """The list of nodes in the workflow graph.

    Each node represents a processing step.
    """

    version: int
    """The schema version of the workflow graph format."""


class WorkflowRetrieveResponse(BaseModel):
    id: str
    """The globally unique ID of the published workflow."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When this version was published"""

    description: Optional[str] = None
    """The description of the published workflow."""

    graph: Graph
    """The workflow graph definition."""

    name: str
    """The name of the published workflow."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When this version was last updated"""

    version: int
    """A monotonically increasing version number.

    Each workflow version for the same published workflow has a unique version
    number.
    """
