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
    "Hailuo3",
    "Hailuo3ReferenceAudio",
    "Hailuo3Reference",
    "Hailuo3ReferenceVideo",
    "Seedance2",
    "Seedance2ReferenceAudio",
    "Seedance2Reference",
    "Seedance2ReferenceVideo",
    "Seedance2Fast",
    "Seedance2FastReferenceAudio",
    "Seedance2FastReference",
    "Seedance2FastReferenceVideo",
    "Seedance2Mini",
    "Seedance2MiniReferenceAudio",
    "Seedance2MiniReference",
    "Seedance2MiniReferenceVideo",
    "GeminiOmniFlash",
    "GeminiOmniFlashReference",
    "Seedance2_5",
    "Seedance2_5ReferenceAudio",
    "Seedance2_5Reference",
    "Seedance2_5ReferenceVideo",
]


class Variant0(TypedDict, total=False):
    model: Required[Literal["aleph2"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    content_moderation: Annotated[Variant0ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    keyframes: Iterable[Variant0Keyframe]
    """Timed guidance images placed at specific points in the input video.

    Up to 5 keyframes.
    """

    output_format: Annotated[Literal["mp4", "prores", "png_sequence"], PropertyInfo(alias="outputFormat")]
    """The container/encoding of the output.

    `mp4` (default) returns an H.264 .mp4. `prores` returns a ProRes .mov.
    `png_sequence` returns a .zip of PNG frames (plus a separate .wav artifact when
    the output has audio). Non-mp4 formats incur an additional surcharge of 5
    credits per second of output.
    """

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty and optional string describing what should appear in the output."""

    prores_profile: Annotated[
        Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"], PropertyInfo(alias="proresProfile")
    ]
    """The ProRes profile to use.

    Only valid when `outputFormat` is `prores`. Defaults to `4444`.
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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    range: Variant0KeyframeUnionMember1Range
    """Optional edit window.

    When set, the edit applies only to this time range and the keyframe timestamp
    must fall within it. All keyframes must either set a range or none may.
    """


Variant0Keyframe: TypeAlias = Union[Variant0KeyframeUnionMember0, Variant0KeyframeUnionMember1]


class Hailuo3(TypedDict, total=False):
    model: Required[Literal["hailuo3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    ratio: Literal["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"]
    """The aspect ratio of the output video.

    Use adaptive only when image or video references are provided; text-only
    requests require a concrete ratio.
    """

    reference_audio: Annotated[Iterable[Hailuo3ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    Audio references require a text prompt, and the total combined duration must not
    exceed 15 seconds.
    """

    references: Iterable[Hailuo3Reference]
    """An optional array of image references (up to 9).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Hailuo3ReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    resolution: Literal["2K", "768P"]
    """The output resolution. Hailuo 3.0 supports 768P and 2K."""


class Hailuo3ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Hailuo3Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Hailuo3ReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2(TypedDict, total=False):
    model: Required[Literal["seedance2"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

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
        "3840:1646",
        "3840:2160",
        "3840:2880",
        "3840:3840",
        "2880:3840",
        "2160:3840",
    ]
    """The resolution of the output video."""

    reference_audio: Annotated[Iterable[Seedance2ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    The total combined duration must not exceed 15 seconds.
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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Seedance2Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2ReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2Fast(TypedDict, total=False):
    model: Required[Literal["seedance2_fast"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

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

    The total combined duration must not exceed 15 seconds.
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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Seedance2FastReference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2FastReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2Mini(TypedDict, total=False):
    model: Required[Literal["seedance2_mini"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

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

    Seedance 2.0 Mini supports 480p and 720p only.
    """

    reference_audio: Annotated[Iterable[Seedance2MiniReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    The total combined duration must not exceed 15 seconds.
    """

    references: Iterable[Seedance2MiniReference]
    """An optional array of image references (up to 9).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Seedance2MiniReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2MiniReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Seedance2MiniReference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2MiniReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class GeminiOmniFlash(TypedDict, total=False):
    model: Required[Literal["gemini_omni_flash"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty instruction describing the edit to apply."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    references: Iterable[GeminiOmniFlashReference]
    """An optional array of image references to guide the edit."""


class GeminiOmniFlashReference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2_5(TypedDict, total=False):
    model: Required[Literal["seedance2_5"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """The number of seconds of duration for the output video. Defaults to 5."""

    mode: Literal["reference", "extend"]
    """How the input video is used.

    `reference` (the default) generates a new video conditioned on the input video
    and accepts `duration` and `ratio`. `extend` continues the input video, requires
    `promptText`, and matches the input aspect ratio, so `ratio` may not be
    provided.
    """

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    An optional text prompt up to 15000 characters describing what should appear in
    the output.
    """

    ratio: Literal[
        "992:432",
        "854:480",
        "752:560",
        "640:640",
        "560:752",
        "480:854",
        "1470:630",
        "1280:720",
        "1112:834",
        "960:960",
        "834:1112",
        "720:1280",
    ]
    """The resolution of the output video. Seedance 2.5 supports 480p and 720p only."""

    reference_audio: Annotated[Iterable[Seedance2_5ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    The total combined duration must be less than 30 seconds.
    """

    references: Iterable[Seedance2_5Reference]
    """An optional array of image references (up to 30).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Seedance2_5ReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 30 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2_5ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 16MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Seedance2_5Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2_5ReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


VideoToVideoCreateParams: TypeAlias = Union[
    Variant0, Hailuo3, Seedance2, Seedance2Fast, Seedance2Mini, GeminiOmniFlash, Seedance2_5
]
