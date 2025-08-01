# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoToVideoCreateParams", "ContentModeration", "Reference"]


class VideoToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen4_aleph"]]
    """The model variant to use."""

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[
        Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
    ]
    """The resolution of the output video."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL pointing to a video or a data URI containing a video.

    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    content_moderation: Annotated[ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    references: Iterable[Reference]
    """An array of references.

    Currently up to one reference is supported. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class ContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Reference(TypedDict, total=False):
    type: Required[Literal["image"]]

    uri: Required[str]
    """A HTTPS URL pointing to an image or a data URI containing an image.

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """
