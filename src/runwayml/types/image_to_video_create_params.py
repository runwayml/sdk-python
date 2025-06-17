# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVideoCreateParams", "PromptImagePromptImage", "ContentModeration"]


class ImageToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen3a_turbo", "gen4_turbo"]]
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

    content_moderation: Annotated[ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    duration: Literal[5, 10]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
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


class ContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """
