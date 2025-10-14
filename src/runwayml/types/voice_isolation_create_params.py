# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceIsolationCreateParams"]


class VoiceIsolationCreateParams(TypedDict, total=False):
    audio_url: Required[Annotated[str, PropertyInfo(alias="audioUrl")]]
    """A HTTPS URL or data URI containing the audio file to process.

    See [our docs](/assets/inputs#audio) on audio inputs for more information.
    """

    model: Required[Literal["eleven_voice_isolation"]]
    """The model variant to use."""
