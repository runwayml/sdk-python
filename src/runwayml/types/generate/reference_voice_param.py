# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReferenceVoiceParam"]


class ReferenceVoiceParam(TypedDict, total=False):
    """Clone a voice from a reference audio clip, then speak promptText in that voice.

    Routes only to models that support voice cloning.
    """

    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """

    type: Required[Literal["reference-audio"]]
