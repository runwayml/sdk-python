# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVideoCreateParams", "PromptImagePromptImage"]


class ImageToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen4_turbo", "gen3a_turbo"]]
    """The model variant to use."""

    prompt_image: Required[Annotated[Union[str, Iterable[PromptImagePromptImage]], PropertyInfo(alias="promptImage")]]
    """
    A HTTPS URL or data URI containing an encoded image to be used as the first
    frame of the generated video. See [our docs](/assets/inputs#images) on image
    inputs for more information.
    """

    ratio: Required[
        Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672", "1280:768", "768:1280"]
    ]
    """The resolution of the output video.

    `gen4_turbo` supports the following values:

    - `1280:720`
    - `720:1280`
    - `1104:832`
    - `832:1104`
    - `960:960`
    - `1584:672`

    `gen3a_turbo` supports the following values:

    - `1280:768`
    - `768:1280`
    """

    duration: Literal[5, 10]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    A non-empty string up to 1000 UTF-16 code points in length (that is,
    `promptText.length === 1000` in JavaScript). This should describe in detail what
    should appear in the output.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first", "last"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video, "last" will use the
    image as the last frame of the video.

    "last" is currently supported for `gen3a_turbo` only.
    """

    uri: Required[str]
    """A HTTPS URL or data URI containing an encoded image.

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """
