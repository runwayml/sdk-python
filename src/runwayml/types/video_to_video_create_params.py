# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "VideoToVideoCreateParams",
    "Gen4Aleph",
    "Gen4AlephContentModeration",
    "Gen4AlephReference",
    "Aleph2",
    "Aleph2ContentModeration",
    "Aleph2Keyframe",
    "Aleph2KeyframeUnionMember0",
    "Aleph2KeyframeUnionMember1",
    "Aleph2PromptImage",
    "Aleph2PromptImagePosition",
    "Aleph2PromptImagePositionTimestampPosition",
    "Aleph2PromptImagePositionRelativePosition",
    "Seedance2",
    "Seedance2ReferenceAudio",
    "Seedance2Reference",
    "Seedance2ReferenceVideo",
]


class Gen4Aleph(TypedDict, total=False):
    model: Required[Literal["gen4_aleph"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL."""

    content_moderation: Annotated[Gen4AlephContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
    """Deprecated.

    This field is ignored. The resolution of the output video is determined by the
    input video.
    """

    references: Iterable[Gen4AlephReference]
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


class Gen4AlephContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Gen4AlephReference(TypedDict, total=False):
    """
    Passing an image reference allows the model to emulate the style or content of the reference in the output.
    """

    type: Required[Literal["image"]]

    uri: Required[str]
    """A HTTPS URL."""


class Aleph2(TypedDict, total=False):
    model: Required[Literal["aleph2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A non-empty string up to 1000 characters describing what should appear in the
    output.
    """

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL."""

    content_moderation: Annotated[Aleph2ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    keyframes: Iterable[Aleph2Keyframe]
    """Timed guidance images placed at specific points in the input video.

    Up to 5 keyframes.
    """

    prompt_image: Annotated[Iterable[Aleph2PromptImage], PropertyInfo(alias="promptImage")]
    """
    A list of up to 5 image keyframes for guiding the edit at specific points in the
    video.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Aleph2ContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Aleph2KeyframeUnionMember0(TypedDict, total=False):
    seconds: Required[float]
    """
    Absolute timestamp in seconds from the start of the input video when this
    guidance image should apply.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Aleph2KeyframeUnionMember1(TypedDict, total=False):
    at: Required[float]
    """
    Position as a fraction [0.0, 1.0] of the input video duration when this guidance
    image should apply.
    """

    uri: Required[str]
    """A HTTPS URL."""


Aleph2Keyframe: TypeAlias = Union[Aleph2KeyframeUnionMember0, Aleph2KeyframeUnionMember1]


class Aleph2PromptImagePositionTimestampPosition(TypedDict, total=False):
    timestamp_seconds: Required[Annotated[float, PropertyInfo(alias="timestampSeconds")]]
    """Absolute timestamp in seconds from the start of the output video."""

    type: Required[Literal["timestamp"]]


class Aleph2PromptImagePositionRelativePosition(TypedDict, total=False):
    position_percentage: Required[Annotated[float, PropertyInfo(alias="positionPercentage")]]
    """Position as a fraction [0.0, 1.0] of the total video duration."""

    type: Required[Literal["position"]]


Aleph2PromptImagePosition: TypeAlias = Union[
    Literal["first", "last"], Aleph2PromptImagePositionTimestampPosition, Aleph2PromptImagePositionRelativePosition
]


class Aleph2PromptImage(TypedDict, total=False):
    position: Required[Aleph2PromptImagePosition]
    """
    - `first` - Places the image at the start of the output video (timestamp 0).
    - `last` - Places the image at the end of the output video (timestamp =
      duration).
    """

    uri: Required[str]
    """A HTTPS URL."""


class Seedance2(TypedDict, total=False):
    model: Required[Literal["seedance2"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL."""

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    An optional text prompt up to 3500 characters describing what should appear in
    the output video.
    """

    ratio: Literal[
        "992:432",
        "864:496",
        "752:560",
        "640:640",
        "560:752",
        "496:864",
        "1470:630",
        "1280:720",
        "1112:834",
        "960:960",
        "834:1112",
        "720:1280",
        "2206:946",
        "1920:1080",
        "1664:1248",
        "1440:1440",
        "1248:1664",
        "1080:1920",
    ]
    """The resolution of the output video."""

    reference_audio: Annotated[Iterable[Seedance2ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    Audio references require a text prompt, and the total combined duration must not
    exceed 15 seconds.
    """

    references: Iterable[Seedance2Reference]
    """An optional array of image references (up to 9).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Seedance2ReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL."""


class Seedance2Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""

    position: Literal["first", "last"]
    """The position of the image in the output video.

    "first" will use the image as the first frame, "last" as the last frame. Omit
    for a reference image.
    """


class Seedance2ReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL."""


VideoToVideoCreateParams: TypeAlias = Union[Gen4Aleph, Aleph2, Seedance2]
