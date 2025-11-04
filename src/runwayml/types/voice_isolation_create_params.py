# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceIsolationCreateParams"]


class VoiceIsolationCreateParams(TypedDict, total=False):
    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL."""

    model: Required[Literal["eleven_voice_isolation"]]
