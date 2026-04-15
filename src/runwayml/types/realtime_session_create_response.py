# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RealtimeSessionCreateResponse"]


class RealtimeSessionCreateResponse(BaseModel):
    id: str
    """The ID of the created realtime session.

    This same value is later used as the conversation ID in the avatar conversation
    endpoints.
    """
