# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VoicePreviewResponse"]


class VoicePreviewResponse(BaseModel):
    duration_secs: float = FieldInfo(alias="durationSecs")
    """Duration of the audio preview in seconds."""

    url: str
    """A presigned URL to the audio preview. The URL expires after 24 hours."""
