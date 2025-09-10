# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TextToVideoCreateParams"]


class TextToVideoCreateParams(TypedDict, total=False):
    duration: Required[Literal[8]]
    """Veo 3 videos must be 8 seconds long."""

    model: Required[Literal["veo3"]]
    """The model variant to use."""

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280"]]
    """A string representing the aspect ratio of the output video."""

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """
