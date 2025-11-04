# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ImageToVideoCreateParams",
    "Gen4Turbo",
    "Gen4TurboPromptImagePromptImage",
    "Gen4TurboContentModeration",
    "Gen3aTurbo",
    "Gen3aTurboPromptImagePromptImage",
    "Gen3aTurboContentModeration",
    "Veo3_1",
    "Veo3_1PromptImagePromptImage",
    "Veo3_1Fast",
    "Veo3_1FastPromptImagePromptImage",
    "Veo3",
    "Veo3PromptImagePromptImage",
]


class Gen4Turbo(TypedDict, total=False):
    model: Required[Literal["gen4_turbo"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Gen4TurboPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL."""

    ratio: Required[Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672"]]
    """The resolution of the output video."""

    content_moderation: Annotated[Gen4TurboContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    duration: int
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


class Gen4TurboPromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Gen4TurboContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Gen3aTurbo(TypedDict, total=False):
    model: Required[Literal["gen3a_turbo"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Gen3aTurboPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL."""

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    content_moderation: Annotated[Gen3aTurboContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    duration: Literal[5, 10]
    """The duration of the output video in seconds."""

    ratio: Literal["768:1280", "1280:768"]
    """The resolution of the output video."""

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Gen3aTurboPromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first", "last"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video, "last" will use the
    image as the last frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Gen3aTurboContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Veo3_1(TypedDict, total=False):
    model: Required[Literal["veo3.1"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Veo3_1PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. This model does not
    support generating with only a last frame.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """


class Veo3_1PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first", "last"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video, "last" will use the
    image as the last frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Veo3_1Fast(TypedDict, total=False):
    model: Required[Literal["veo3.1_fast"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Veo3_1FastPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. This model does not
    support generating with only a last frame.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """


class Veo3_1FastPromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first", "last"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video, "last" will use the
    image as the last frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Veo3(TypedDict, total=False):
    duration: Required[Literal[8]]
    """The number of seconds of duration for the output video."""

    model: Required[Literal["veo3"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Veo3PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL."""

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """


class Veo3PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL."""


ImageToVideoCreateParams: TypeAlias = Union[Gen4Turbo, Gen3aTurbo, Veo3_1, Veo3_1Fast, Veo3]
