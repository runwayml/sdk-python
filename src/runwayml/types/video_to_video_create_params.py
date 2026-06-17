# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "VideoToVideoCreateParams",
    "Variant0",
    "Variant0ContentModeration",
    "Variant0Keyframe",
    "Variant0KeyframeUnionMember0",
    "Variant0KeyframeUnionMember0Range",
    "Variant0KeyframeUnionMember1",
    "Variant0KeyframeUnionMember1Range",
    "Seedance2",
    "Seedance2ReferenceAudio",
    "Seedance2Reference",
    "Seedance2ReferenceVideo",
    "Seedance2Fast",
    "Seedance2FastReferenceAudio",
    "Seedance2FastReference",
    "Seedance2FastReferenceVideo",
]


class Variant0(TypedDict, total=False):
    model: Required[Literal["aleph2"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL."""

    content_moderation: Annotated[Variant0ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    keyframes: Iterable[Variant0Keyframe]
    """Timed guidance images placed at specific points in the input video.

    Up to 5 keyframes.
    """

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    An optional string up to 1000 characters describing what should appear in the
    output.
    """

    ratio: str

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """

    target_aspect_ratio: Annotated[
        Literal["16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "21:9"], PropertyInfo(alias="targetAspectRatio")
    ]
    """Target aspect ratio for expand/outpaint.

    Letterboxes the input video and keyframes before generation.
    """


class Variant0ContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Variant0KeyframeUnionMember0Range(TypedDict, total=False):
    """Optional edit window.

    When set, the edit applies only to this time range and the keyframe timestamp must fall within it. All keyframes must either set a range or none may.
    """

    end_seconds: Required[int]
    """
    End of the edit window (exclusive) in whole seconds from the start of the input
    video.
    """

    start_seconds: Required[int]
    """Start of the edit window in whole seconds from the start of the input video."""


class Variant0KeyframeUnionMember0(TypedDict, total=False):
    seconds: Required[float]
    """
    Absolute timestamp in seconds from the start of the input video when this
    guidance image should apply.
    """

    uri: Required[str]
    """A HTTPS URL."""

    range: Variant0KeyframeUnionMember0Range
    """Optional edit window.

    When set, the edit applies only to this time range and the keyframe timestamp
    must fall within it. All keyframes must either set a range or none may.
    """


class Variant0KeyframeUnionMember1Range(TypedDict, total=False):
    """Optional edit window.

    When set, the edit applies only to this time range and the keyframe timestamp must fall within it. All keyframes must either set a range or none may.
    """

    end_seconds: Required[int]
    """
    End of the edit window (exclusive) in whole seconds from the start of the input
    video.
    """

    start_seconds: Required[int]
    """Start of the edit window in whole seconds from the start of the input video."""


class Variant0KeyframeUnionMember1(TypedDict, total=False):
    at: Required[float]
    """
    Position as a fraction [0.0, 1.0] of the input video duration when this guidance
    image should apply.
    """

    uri: Required[str]
    """A HTTPS URL."""

    range: Variant0KeyframeUnionMember1Range
    """Optional edit window.

    When set, the edit applies only to this time range and the keyframe timestamp
    must fall within it. All keyframes must either set a range or none may.
    """


Variant0Keyframe: TypeAlias = Union[Variant0KeyframeUnionMember0, Variant0KeyframeUnionMember1]


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
    the output.
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


class Seedance2Fast(TypedDict, total=False):
    model: Required[Literal["seedance2_fast"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL."""

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    An optional text prompt up to 3500 characters describing what should appear in
    the output.
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
    ]
    """The resolution of the output video.

    Seedance 2.0 Fast supports 480p and 720p only.
    """

    reference_audio: Annotated[Iterable[Seedance2FastReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    Audio references require a text prompt, and the total combined duration must not
    exceed 15 seconds.
    """

    references: Iterable[Seedance2FastReference]
    """An optional array of image references (up to 9).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Seedance2FastReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2FastReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL."""


class Seedance2FastReference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""

    position: Literal["first", "last"]
    """The position of the image in the output video.

    "first" will use the image as the first frame, "last" as the last frame. Omit
    for a reference image.
    """


class Seedance2FastReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL."""


VideoToVideoCreateParams: TypeAlias = Union[Variant0, Seedance2, Seedance2Fast]
