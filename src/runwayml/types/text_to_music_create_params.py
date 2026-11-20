# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TextToMusicCreateParams"]


class TextToMusicCreateParams(TypedDict, total=False):
    model: Required[Literal["eleven_music_v2_5"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A description of the track to generate, such as its genre, mood, instruments,
    and vocals. Prompts that name specific artists or songs are rejected.
    """

    duration: int
    """The length of the track in whole seconds.

    You are billed for the requested length.
    """

    instrumental: bool
    """When true, the track has no vocals.

    When omitted, the model decides from the prompt.
    """
