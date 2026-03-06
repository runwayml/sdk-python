# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoicePreviewParams"]


class VoicePreviewParams(TypedDict, total=False):
    model: Required[Literal["eleven_multilingual_ttv_v2", "eleven_ttv_v3"]]
    """The voice design model to use."""

    prompt: Required[str]
    """A text description of the desired voice characteristics.

    Must be at least 20 characters.
    """
