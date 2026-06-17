# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RecipeProductAdResponse"]


class RecipeProductAdResponse(BaseModel):
    id: str
    """The ID of the task that was created. Use this to retrieve the task later."""
