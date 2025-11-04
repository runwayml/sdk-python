# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["UploadCreateEphemeralResponse"]


class UploadCreateEphemeralResponse(BaseModel):
    uri: str
    """The Runway upload URI to use in other API generation requests."""

