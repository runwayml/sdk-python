# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ImageToVideoCreateParams",
    "Gen4_5",
    "Gen4_5PromptImagePromptImage",
    "Gen4_5ContentModeration",
    "Gen4Turbo",
    "Gen4TurboPromptImagePromptImage",
    "Gen4TurboContentModeration",
    "Veo3_1",
    "Veo3_1PromptImagePromptImage",
    "Veo3_1Fast",
    "Veo3_1FastPromptImagePromptImage",
    "Hailuo3",
    "Hailuo3ReferenceAudio",
    "Happyhorse1_0",
    "Happyhorse1_0PromptImagePromptImage",
    "Seedance2",
    "Seedance2PromptImagePromptImage",
    "Seedance2ReferenceAudio",
    "Seedance2Fast",
    "Seedance2FastPromptImagePromptImage",
    "Seedance2FastReferenceAudio",
    "Seedance2Mini",
    "Seedance2MiniPromptImagePromptImage",
    "Seedance2MiniReferenceAudio",
    "GeminiOmniFlash",
    "GeminiOmniFlashPromptImagePromptImage",
    "Seedance2_5",
    "Seedance2_5PromptImagePromptImage",
    "Seedance2_5ReferenceAudio",
    "GrokImagine1_5",
    "GrokImagine1_5PromptImagePromptImage",
]


class Gen4_5(TypedDict, total=False):
    duration: Required[int]
    """The number of seconds of duration for the output video.

    Must be an integer from 2 to 10.
    """

    model: Required[Literal["gen4.5"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Gen4_5PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672"]]
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
    separate .wav when the output has audio). Non-mp4 formats incur an additional
    per-second credit surcharge: 5 credits per second for `prores` and
    `png_sequence`, and 20 credits per second for every 10-bit and deeper profile
    (including the 12-bit, 16-bit, and EXR ones), rising to 40 credits per second
    when the output is larger than 4 megapixels (roughly 4K).
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


class Gen4_5PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Gen4_5ContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Gen4Turbo(TypedDict, total=False):
    model: Required[Literal["gen4_turbo"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Gen4TurboPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Gen4TurboContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

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

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Text describing what should not appear in the output video."""

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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


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

    audio: bool
    """Whether to generate audio for the video. Audio inclusion affects pricing."""

    duration: Literal[4, 6, 8]
    """The number of seconds of duration for the output video."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Text describing what should not appear in the output video."""

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
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Hailuo3(TypedDict, total=False):
    model: Required[Literal["hailuo3"]]

    prompt_image: Required[Annotated[Union[str, Iterable[object]], PropertyInfo(alias="promptImage")]]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
    """

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

    resolution: Literal["2K", "768P"]
    """The output resolution. MiniMax H3 supports 768P and 2K."""


class Hailuo3ReferenceAudio(TypedDict, total=False):
    """
    An audio reference allows the model to use the audio as additional context for the output.
    """

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class Happyhorse1_0(TypedDict, total=False):
    model: Required[Literal["happyhorse_1_0"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Happyhorse1_0PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    A string up to 2500 characters (measured in UTF-16 code units) describing motion
    or changes in the output video.
    """

    resolution: Literal["720P", "1080P"]
    """Output quality tier. Output aspect ratio follows the input image."""


class Happyhorse1_0PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2(TypedDict, total=False):
    model: Required[Literal["seedance2"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Seedance2PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
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


class Seedance2PromptImagePromptImage(TypedDict, total=False):
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


class Seedance2Fast(TypedDict, total=False):
    model: Required[Literal["seedance2_fast"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Seedance2FastPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
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


class Seedance2FastPromptImagePromptImage(TypedDict, total=False):
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


class Seedance2Mini(TypedDict, total=False):
    model: Required[Literal["seedance2_mini"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Seedance2MiniPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
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


class Seedance2MiniPromptImagePromptImage(TypedDict, total=False):
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


class GeminiOmniFlash(TypedDict, total=False):
    model: Required[Literal["gemini_omni_flash"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[GeminiOmniFlashPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image to use as the first frame of the output video.

    Gemini Omni Flash only supports a first frame.
    """

    duration: int
    """The duration of the output video in seconds, as a whole number from 3 to 10."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    An optional text prompt describing how the video should evolve from the first
    frame.
    """

    ratio: Literal["1280:720", "720:1280"]
    """
    The aspect ratio of the output video: `1280:720` (landscape) or `720:1280`
    (portrait).
    """


class GeminiOmniFlashPromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedance2_5(TypedDict, total=False):
    model: Required[Literal["seedance2_5"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Seedance2_5PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """The number of seconds of duration for the output video."""

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

    The total combined duration must not exceed 30 seconds.
    """


class Seedance2_5PromptImagePromptImage(TypedDict, total=False):
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


class GrokImagine1_5(TypedDict, total=False):
    model: Required[Literal["grok_imagine_1_5"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[GrokImagine1_5PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """An optional text prompt describing motion or changes in the output video."""

    resolution: Literal["480p", "720p", "1080p"]
    """The output resolution. Output aspect ratio follows the input image."""


class GrokImagine1_5PromptImagePromptImage(TypedDict, total=False):
    position: Required[Literal["first"]]
    """The position of the image in the output video.

    "first" will use the image as the first frame of the video.
    """

    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


ImageToVideoCreateParams: TypeAlias = Union[
    Gen4_5,
    Gen4Turbo,
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
]
