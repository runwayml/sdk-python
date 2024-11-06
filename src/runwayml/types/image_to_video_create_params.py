# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVideoCreateParams", "PromptImagePromptImage"]


class ImageToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen3a_turbo"]]
    """The model variant to use."""

    prompt_image: Required[Annotated[Union[str, Iterable[PromptImagePromptImage]], PropertyInfo(alias="promptImage")]]
    """
    A HTTPS URL or data URI containing an encoded image to be used as the first
    frame of the generated video. See [our docs](/assets/inputs#images) on image
    inputs for more information.
    """

    duration: Literal[5, 10]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]

    ratio: Literal["1280:768", "768:1280"]

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """

    watermark: bool
    """
    A boolean indicating whether or not the output video will contain a Runway
    watermark.
    """


class PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first", "last"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video, "last" will use the
    image as the last frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL or data URI containing an encoded image.

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """
