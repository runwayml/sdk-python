# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VideoUpscaleCreateResponse", "EstimatedCost"]


class EstimatedCost(BaseModel):
    """The maximum credits this task may charge.

    The final amount may be lower after the task completes.
    """

    credits: float
    """Estimated cost of the generation in credits."""


class VideoUpscaleCreateResponse(BaseModel):
    id: str
    """The ID of the task that was created. Use this to retrieve the task later."""

    estimated_cost: EstimatedCost = FieldInfo(alias="estimatedCost")
    """The maximum credits this task may charge.

    The final amount may be lower after the task completes.
    """
