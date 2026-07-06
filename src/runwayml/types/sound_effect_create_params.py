# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SoundEffectCreateParams"]


class SoundEffectCreateParams(TypedDict, total=False):
    model: Required[Literal["eleven_text_to_sound_v2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text description of the sound effect to generate."""

    duration: float
    """The duration of the sound effect in seconds, between 0.5 and 30 seconds.

    If not provided, the duration will be determined automatically based on the text
    description.
    """

    loop: bool
    """Whether the output sound effect should be designed to loop seamlessly."""
