# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoicePreviewParams"]


class VoicePreviewParams(TypedDict, total=False):
    model: Required[Literal["eleven_ttv_v3", "eleven_multilingual_ttv_v2"]]
    """The voice design model to use.

    Prefer eleven_ttv_v3 (latest); eleven_multilingual_ttv_v2 is the previous
    generation.
    """

    prompt: Required[str]
    """A text description of the desired voice characteristics.

    Must be at least 20 characters.
    """
