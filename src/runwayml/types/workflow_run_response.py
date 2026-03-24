# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowRunResponse"]


class WorkflowRunResponse(BaseModel):
    id: str
    """The ID of the workflow invocation that was created."""
