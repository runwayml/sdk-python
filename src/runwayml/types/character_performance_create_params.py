# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CharacterPerformanceCreateParams",
    "Character",
    "CharacterVideo",
    "CharacterImage",
    "Reference",
    "ContentModeration",
]


class CharacterPerformanceCreateParams(TypedDict, total=False):
    character: Required[Character]
    """The character to control.

    You can either provide a video or an image. A visually recognizable face must be
    visible and stay within the frame.
    """

    model: Required[Literal["act_two"]]
    """The model variant to use."""

    ratio: Required[Literal["1280:720", "720:1280", "960:960", "1104:832", "832:1104", "1584:672"]]
    """The resolution of the output video."""

    reference: Required[Reference]

    body_control: Annotated[bool, PropertyInfo(alias="bodyControl")]
    """A boolean indicating whether to enable body control.

    When enabled, non-facial movements and gestures will be applied to the character
    in addition to facial expressions.
    """

    content_moderation: Annotated[ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    expression_intensity: Annotated[int, PropertyInfo(alias="expressionIntensity")]
    """An integer between 1 and 5 (inclusive).

    A larger value increases the intensity of the character's expression.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class CharacterVideo(TypedDict, total=False):
    type: Required[Literal["video"]]

    uri: Required[str]
    """
    A HTTPS URL pointing to a video or a data URI containing a video of your
    character. See [our docs](/assets/inputs#videos) on video inputs for more
    information.
    """


class CharacterImage(TypedDict, total=False):
    type: Required[Literal["image"]]

    uri: Required[str]
    """
    A HTTPS URL pointing to an image or a data URI containing an image of your
    character. See [our docs](/assets/inputs#images) on image inputs for more
    information.
    """


Character: TypeAlias = Union[CharacterVideo, CharacterImage]


class Reference(TypedDict, total=False):
    type: Required[Literal["video"]]

    uri: Required[str]
    """
    A HTTPS URL pointing to a video or a data URI containing a video of a person
    performing in the manner that you would like your character to perform. The
    video must be between 3 and 30 seconds in duration. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class ContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """
