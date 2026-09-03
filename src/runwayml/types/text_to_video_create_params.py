# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TextToVideoCreateParams",
    "Gen4_5",
    "Gen4_5ContentModeration",
    "Veo3_1",
    "Veo3_1Fast",
    "Hailuo3",
    "Hailuo3ReferenceAudio",
    "Hailuo3Reference",
    "Hailuo3ReferenceVideo",
    "Happyhorse1_0",
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
    "Seedance2_5",
    "Seedance2_5ReferenceAudio",
    "Seedance2_5Reference",
    "Seedance2_5ReferenceVideo",
    "GrokImagine1_5",
    "GrokImagine1_5ReferenceAudio",
    "GrokImagine1_5Reference",
    "Wan3",
    "Wan3ReferenceAudio",
    "Wan3Reference",
    "Wan3ReferenceVideo",
    "GeminiOmniFlash1_1",
    "GeminiOmniFlash1_1Reference",
    "GeminiOmniFlash1_1ReferenceVideo",
    "Wan3Prime",
    "Wan3PrimeReferenceAudio",
    "Wan3PrimeReference",
    "Wan3PrimeReferenceVideo",
    "H3Max",
]


class Gen4_5(TypedDict, total=False):
    duration: Required[int]
    """The number of seconds of duration for the output video.

    Must be an integer from 2 to 10.
    """

    model: Required[Literal["gen4.5"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280"]]
    """The resolution of the output video."""

    content_moderation: Annotated[Gen4_5ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    output_format: Annotated[
        Literal[
            "mp4",
            "prores",
            "png_sequence",
            "hdr10",
            "hlg",
            "sdr_rec709_10bit",
            "hdr_pq_12bit_master",
            "hdr_prores",
            "hdr_png_sequence",
            "hdr_exr_sequence",
            "hdr_exr_acescg_sequence_1_3",
            "hdr_exr_acescg_sequence_2_0",
        ],
        PropertyInfo(alias="outputFormat"),
    ]
    """The container/encoding of the output.

    `mp4` (default) returns an H.264 .mp4. `prores` returns a ProRes .mov.
    `png_sequence` returns a .zip of PNG frames (plus a separate .wav artifact when
    the output has audio). `hdr10` (HEVC Main 10, BT.2020 + PQ) and `hlg` (HEVC Main
    10, BT.2020 + HLG) return true-HDR 10-bit .mp4s; `sdr_rec709_10bit` returns a
    10-bit Rec.709 HEVC .mp4 for SDR grading pipelines; `hdr_pq_12bit_master`
    returns a 12-bit 4:4:4 BT.2020 + PQ HEVC .mov with measured HDR10 content-light
    metadata for mastering; `hdr_prores` returns a BT.2020 + PQ ProRes .mov
    editorial mezzanine, whose tier is selectable with `proresProfile` (`422`,
    `422 HQ`, or `4444`; defaults to `422 HQ`); `hdr_png_sequence` returns a .zip of
    16-bit PNG frames carrying the PQ signal losslessly (plus a colorimetry.json
    sidecar and a separate .wav when the output has audio); `hdr_exr_sequence`
    returns a .zip of half-float OpenEXR frames carrying the HDR signal as linear
    BT.2020 display light, 1.0 = 100 nits (plus a colorimetry.json sidecar and a
    separate .wav when the output has audio); `hdr_exr_acescg_sequence_1_3` returns
    the same delivery as scene-referred ACEScg (inverted through the ACES 1.3 Output
    Transform), reading correctly with the stock `ACES - ACEScg` input transform in
    ACES-configured pipelines, with VFX sequence frame naming (frame.0001.exr).
    Non-mp4 formats incur an additional per-second credit surcharge: 5 credits per
    second for `prores` and `png_sequence`, and 20 credits per second for every
    10-bit and deeper profile (including the 12-bit, 16-bit, and EXR ones), rising
    to 40 credits per second when the output is larger than 4 megapixels — that
    includes 1440p (2560x1440 is under the line, but anything larger crosses it) up
    through 4K.
    """

    prores_profile: Annotated[
        Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"], PropertyInfo(alias="proresProfile")
    ]
    """The ProRes profile to use.

    Only valid when `outputFormat` is `prores` or `hdr_prores`. For `prores`, any
    profile is accepted and the default is `4444`. For `hdr_prores`, only `422`,
    `422 HQ` and `4444` are available and the default is `422 HQ` — `422 Proxy` and
    `422 LT` quantize too heavily to hold the HDR gradients, and 12-bit output is
    served by `hdr_pq_12bit_master` instead of `4444 XQ`.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Gen4_5ContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Veo3_1(TypedDict, total=False):
    model: Required[Literal["veo3.1"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Text describing what should not appear in the output video."""

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Veo3_1Fast(TypedDict, total=False):
    model: Required[Literal["veo3.1_fast"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]]
    """The resolution of the output video."""

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Text describing what should not appear in the output video."""

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Hailuo3(TypedDict, total=False):
    model: Required[Literal["hailuo3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

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


class Happyhorse1_0(TypedDict, total=False):
    model: Required[Literal["happyhorse_1_0"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 2500 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    ratio: Literal[
        "1280:720",
        "720:1280",
        "960:960",
        "1108:832",
        "832:1108",
        "1920:1080",
        "1080:1920",
        "1440:1440",
        "1662:1248",
        "1248:1662",
    ]
    """The resolution of the output video."""


class Seedance2(TypedDict, total=False):
    model: Required[Literal["seedance2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A non-empty text prompt up to 3500 characters describing what should appear in
    the output.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
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

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A non-empty text prompt up to 3500 characters describing what should appear in
    the output.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
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

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A non-empty text prompt up to 3500 characters describing what should appear in
    the output.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
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
    """A non-empty text prompt describing the video to generate."""

    duration: int
    """The duration of the output video in seconds, as a whole number from 3 to 10."""

    ratio: Literal["1280:720", "720:1280"]
    """
    The aspect ratio of the output video: `1280:720` (landscape) or `720:1280`
    (portrait).
    """


class Seedance2_5(TypedDict, total=False):
    model: Required[Literal["seedance2_5"]]

    audio: bool
    """Whether to generate audio for the video."""

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
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


class GrokImagine1_5(TypedDict, total=False):
    model: Required[Literal["grok_imagine_1_5"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    duration: int
    """The number of seconds of duration for the output video."""

    ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3"]
    """The aspect ratio of the output video."""

    reference_audio: Annotated[Iterable[GrokImagine1_5ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    Audio references require at least one image reference, and each clip must be
    between 3 and 15 seconds.
    """

    references: Iterable[GrokImagine1_5Reference]
    """An optional array of image references.

    Referenced images can be addressed in the prompt as [Image 1], [Image 2], and so
    on. See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    resolution: Literal["480p", "720p", "1080p"]
    """The output resolution. Requests with image references are capped at 720p."""


class GrokImagine1_5ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to drive the output with the supplied audio.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class GrokImagine1_5Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Wan3(TypedDict, total=False):
    model: Required[Literal["wan3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    audio: bool
    """Whether to generate audio with the video."""

    duration: int
    """The number of seconds of duration for the output video."""

    ratio: Literal[
        "832:480",
        "720:544",
        "624:624",
        "544:720",
        "480:832",
        "1280:720",
        "1104:832",
        "960:960",
        "832:1104",
        "720:1280",
        "1920:1080",
        "1648:1248",
        "1440:1440",
        "1248:1648",
        "1080:1920",
        "auto_480p",
        "auto_720p",
        "auto_1080p",
    ]
    """The resolution of the output video, as `<width>:<height>`.

    Keyframe image-to-video requests must use `auto_480p`, `auto_720p`, or
    `auto_1080p` because their aspect ratio follows the first frame.
    """

    reference_audio: Annotated[Iterable[Wan3ReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    The total combined duration must not exceed 15 seconds.
    """

    references: Iterable[Wan3Reference]
    """An optional array of image references (up to 10).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Wan3ReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Wan3ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Wan3Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Wan3ReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class GeminiOmniFlash1_1(TypedDict, total=False):
    model: Required[Literal["gemini_omni_flash_1.1"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing the video to generate."""

    duration: Union[Literal["auto"], int]
    """The duration of the output video in seconds.

    Use "auto" to let the model choose a duration. Numeric durations must be between
    3 and 10 seconds.
    """

    ratio: Literal["640:360", "360:640", "1280:720", "720:1280", "1920:1080", "1080:1920", "3840:2160", "2160:3840"]
    """The resolution and aspect ratio of the output video."""

    references: Iterable[GeminiOmniFlash1_1Reference]

    reference_videos: Annotated[Iterable[GeminiOmniFlash1_1ReferenceVideo], PropertyInfo(alias="referenceVideos")]


class GeminiOmniFlash1_1Reference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class GeminiOmniFlash1_1ReferenceVideo(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Wan3Prime(TypedDict, total=False):
    model: Required[Literal["wan3_prime"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    audio: bool
    """Whether to generate audio with the video."""

    duration: int
    """The number of seconds of duration for the output video."""

    ratio: Literal[
        "832:480",
        "720:544",
        "624:624",
        "544:720",
        "480:832",
        "1280:720",
        "1104:832",
        "960:960",
        "832:1104",
        "720:1280",
        "1920:1080",
        "1648:1248",
        "1440:1440",
        "1248:1648",
        "1080:1920",
        "auto_480p",
        "auto_720p",
        "auto_1080p",
    ]
    """The resolution of the output video, as `<width>:<height>`.

    Keyframe image-to-video requests must use `auto_480p`, `auto_720p`, or
    `auto_1080p` because their aspect ratio follows the first frame.
    """

    reference_audio: Annotated[Iterable[Wan3PrimeReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """An optional array of audio references.

    The total combined duration must not exceed 15 seconds.
    """

    references: Iterable[Wan3PrimeReference]
    """An optional array of image references (up to 10).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """

    reference_videos: Annotated[Iterable[Wan3PrimeReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Wan3PrimeReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Wan3PrimeReference(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Wan3PrimeReferenceVideo(TypedDict, total=False):
    """
    A video reference allows the model to use the video as additional context for the output.
    """

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class H3Max(TypedDict, total=False):
    model: Required[Literal["h3_max"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_expansion_mode: Annotated[
        Literal["disabled", "balanced", "quality"], PropertyInfo(alias="promptExpansionMode")
    ]
    """How the model rewrites the prompt before generating.

    disabled keeps the prompt as written. balanced (the default) does a short
    rewrite. quality spends extra time rewriting for a stronger result.
    """

    resolution: Literal["480p", "768p"]
    """The output resolution. MiniMax H3 Max supports 480p and 768p."""

    seed: int
    """If unspecified, a random number is chosen.

    Identical results also need promptExpansionMode set to disabled; balanced and
    quality rewrite the prompt and will not repeat.
    """


TextToVideoCreateParams: TypeAlias = Union[
    Gen4_5,
    Veo3_1,
    Veo3_1Fast,
    Hailuo3,
    Happyhorse1_0,
    Seedance2,
    Seedance2Fast,
    Seedance2Mini,
    GeminiOmniFlash,
    Seedance2_5,
    GrokImagine1_5,
    Wan3,
    GeminiOmniFlash1_1,
    Wan3Prime,
    H3Max,
]
