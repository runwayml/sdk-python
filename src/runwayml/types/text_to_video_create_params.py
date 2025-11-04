# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["TextToVideoCreateParams", "Veo3_1", "Veo3_1Fast", "Veo3"]


class Veo3_1(TypedDict, total=False):
    model: Required[Literal["veo3.1"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""


class Veo3_1Fast(TypedDict, total=False):
    model: Required[Literal["veo3.1_fast"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""


class Veo3(TypedDict, total=False):
    duration: Required[Literal[8]]
    """The number of seconds of duration for the output video."""

    model: Required[Literal["veo3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""


TextToVideoCreateParams: TypeAlias = Union[Veo3_1, Veo3_1Fast, Veo3]
