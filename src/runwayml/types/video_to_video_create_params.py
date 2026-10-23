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
    "KlingO3_4k",
    "KlingO3_4kProviderSettings",
    "KlingO3_4kProviderSettingsMultiPrompt",
    "KlingO3_4kReferencesPromptImage",
    "Hailuo3",
    "Hailuo3ReferenceAudio",
    "Hailuo3Reference",
    "Hailuo3ReferenceVideo",
    "KlingO3Pro",
    "KlingO3ProProviderSettings",
    "KlingO3ProProviderSettingsMultiPrompt",
    "KlingO3ProReferencesPromptImage",
    "KlingO3Standard",
    "KlingO3StandardProviderSettings",
    "KlingO3StandardProviderSettingsMultiPrompt",
    "KlingO3StandardReferencesPromptImage",
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
    "GeminiOmniFlash1_1",
    "GeminiOmniFlash1_1Reference",
    "Seedance2_5",
    "Seedance2_5ReferenceAudio",
    "Seedance2_5Reference",
    "Seedance2_5ReferenceVideo",
    "Kling4",
    "Kling4Reference",
]


class Variant0(TypedDict, total=False):
    model: Required[Literal["aleph2"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    content_moderation: Annotated[Variant0ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    keyframes: Iterable[Variant0Keyframe]
    """Timed guidance images placed at specific points in the input video.

    Up to 5 keyframes.
    """

    output_format: Annotated[
        Literal["mp4", "prores", "png_sequence", "sdr_rec709_10bit"], PropertyInfo(alias="outputFormat")
    ]
    """The container/encoding of the output.

    `mp4` (default) returns an H.264 .mp4. `prores` returns a ProRes .mov.
    `png_sequence` returns a .zip of PNG frames. `sdr_rec709_10bit` returns a 10-bit
    Rec.709 HEVC .mp4 for SDR grading pipelines. Non-mp4 formats incur an additional
    surcharge: 5 credits per second for `prores` and `png_sequence`, and 20 credits
    per second for `sdr_rec709_10bit` — 40 credits per second when the output is
    larger than 4 megapixels — includes anything larger than 1440p, up through 4K.
    """

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A non-empty and optional string describing what should appear in the output."""

    prores_profile: Annotated[
        Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"], PropertyInfo(alias="proresProfile")
    ]
    """The ProRes profile to use.

    Only valid when `outputFormat` is `prores`. Defaults to `4444`. Note: generated
    content contains no transparency — the alpha channel in `4444` / `4444 XQ`
    outputs is present but fully opaque; choose these tiers for 12-bit 4:4:4 color
    fidelity, not for mattes.
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


class KlingO3_4k(TypedDict, total=False):
    model: Required[Literal["klingO3_4k"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing what should appear in the output video."""

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    provider_settings: Annotated[KlingO3_4kProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation and video editing."""

    references: Union[str, Iterable[KlingO3_4kReferencesPromptImage]]
    """An optional array of reference images (up to 4).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3_4kProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3_4kProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation and video editing."""

    keep_original_sound: Annotated[bool, PropertyInfo(alias="keepOriginalSound")]
    """Whether to preserve the original audio when editing a video.

    Only applicable for video-to-video. Defaults to true.
    """

    multi_prompt: Annotated[Iterable[KlingO3_4kProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
    """


class KlingO3_4kReferencesPromptImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    position: Literal["first", "last"]
    """The position of the image in the output video.

    "first" will use the image as the first frame, "last" as the last frame. Omit
    for a reference image.
    """


class Hailuo3(TypedDict, total=False):
    model: Required[Literal["hailuo3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
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

    resolution: Literal["768p", "2k", "768P", "2K"]
    """The output resolution. Hailuo 3.0 supports 768p and 2k.

    - `768P` - Deprecated: Use "768p" instead.
    - `2K` - Deprecated: Use "2k" instead.
    """


class Hailuo3ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class KlingO3Pro(TypedDict, total=False):
    model: Required[Literal["klingO3_pro"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing what should appear in the output video."""

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    provider_settings: Annotated[KlingO3ProProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation and video editing."""

    references: Union[str, Iterable[KlingO3ProReferencesPromptImage]]
    """An optional array of reference images (up to 4).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3ProProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3ProProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation and video editing."""

    keep_original_sound: Annotated[bool, PropertyInfo(alias="keepOriginalSound")]
    """Whether to preserve the original audio when editing a video.

    Only applicable for video-to-video. Defaults to true.
    """

    multi_prompt: Annotated[Iterable[KlingO3ProProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
    """


class KlingO3ProReferencesPromptImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    position: Literal["first", "last"]
    """The position of the image in the output video.

    "first" will use the image as the first frame, "last" as the last frame. Omit
    for a reference image.
    """


class KlingO3Standard(TypedDict, total=False):
    model: Required[Literal["klingO3_standard"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing what should appear in the output video."""

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    provider_settings: Annotated[KlingO3StandardProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation and video editing."""

    references: Union[str, Iterable[KlingO3StandardReferencesPromptImage]]
    """An optional array of reference images (up to 4).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3StandardProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3StandardProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation and video editing."""

    keep_original_sound: Annotated[bool, PropertyInfo(alias="keepOriginalSound")]
    """Whether to preserve the original audio when editing a video.

    Only applicable for video-to-video. Defaults to true.
    """

    multi_prompt: Annotated[Iterable[KlingO3StandardProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
    """


class KlingO3StandardReferencesPromptImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    position: Literal["first", "last"]
    """The position of the image in the output video.

    "first" will use the image as the first frame, "last" as the last frame. Omit
    for a reference image.
    """


class Seedance2(TypedDict, total=False):
    model: Required[Literal["seedance2"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
    """

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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Seedance2ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2Fast(TypedDict, total=False):
    model: Required[Literal["seedance2_fast"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
    """

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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Seedance2FastReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Seedance2Mini(TypedDict, total=False):
    model: Required[Literal["seedance2_mini"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
    """

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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Seedance2MiniReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class GeminiOmniFlash(TypedDict, total=False):
    model: Required[Literal["gemini_omni_flash"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty instruction describing the edit to apply."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
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


class GeminiOmniFlash1_1(TypedDict, total=False):
    model: Required[Literal["gemini_omni_flash_1.1"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty prompt describing the output or extension."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    duration: Union[Literal["auto"], int]
    """The duration in seconds.

    In reference mode, this is the output video length. In extend mode, this is the
    amount of footage added to the input video. Use "auto" to let the model choose a
    duration.
    """

    mode: Literal["reference", "extend", "edit"]
    """How the input video is used.

    `reference` generates a new video guided by the input, `extend` continues it,
    and `edit` transforms it according to the prompt.
    """

    ratio: Literal["640:360", "360:640", "1280:720", "720:1280", "1920:1080", "1080:1920", "3840:2160", "2160:3840"]
    """The resolution and aspect ratio of the output video."""

    references: Iterable[GeminiOmniFlash1_1Reference]
    """An optional array of image references to guide the output."""


class GeminiOmniFlash1_1Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2_5(TypedDict, total=False):
    model: Required[Literal["seedance2_5"]]

    prompt_video: Required[Annotated[str, PropertyInfo(alias="promptVideo")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    audio: bool
    """Whether to generate audio for the video."""

    draft: bool
    """Generate a cheap 480p preview instead of a full-quality video.

    The returned task ID can later be enhanced to a 1080p video with the same
    content by passing it as `draftTaskId` to `text_to_video`. Drafts can be
    enhanced within 7 days of creation. Defaults to false.
    """

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes. Defaults to 5.
    """

    mode: Literal["reference", "extend", "edit"]
    """How the input video is used.

    `reference` (the default) generates a new video conditioned on the input video
    and accepts `duration` and `ratio`. `extend` continues the input video, requires
    `promptText`, and matches the input aspect ratio, so `ratio` may not be
    provided. `edit` modifies the input video in place, requires `promptText`,
    requires `duration: "auto"`, and does not accept `ratio`.
    """

    output_format: Annotated[Literal["mp4", "mov"], PropertyInfo(alias="outputFormat")]
    """Container for the output video.

    `mov` keeps high colour precision for grading and compositing. Defaults to
    `mp4`. Draft mode only supports `mp4`.
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
        "2206:946",
        "1920:1080",
        "1664:1248",
        "1440:1440",
        "1248:1664",
        "1080:1920",
    ]
    """The resolution of the output video.

    Seedance 2.5 supports 480p, 720p, and 1080p.
    """

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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Seedance2_5ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Kling4(TypedDict, total=False):
    model: Required[Literal["kling_4"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing how to edit the video."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    ratio: Literal["auto_720p", "auto_1080p"]
    """Output quality tier. The video keeps the input media framing."""

    references: Iterable[Kling4Reference]
    """Images of characters, objects or styles to use in the video.

    Up to 10 images in total, frames included.
    """


class Kling4Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


VideoToVideoCreateParams: TypeAlias = Union[
    Variant0,
    KlingO3_4k,
    Hailuo3,
    KlingO3Pro,
    KlingO3Standard,
    Seedance2,
    Seedance2Fast,
    Seedance2Mini,
    GeminiOmniFlash,
    GeminiOmniFlash1_1,
    Seedance2_5,
    Kling4,
]
