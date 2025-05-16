# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TextToImageCreateResponse"]


class TextToImageCreateResponse(BaseModel):
    id: str
    """The ID of the newly created task."""
