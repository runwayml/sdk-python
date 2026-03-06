# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VoiceCreateResponse"]


class VoiceCreateResponse(BaseModel):
    id: str
    """The ID of the voice that was created."""
