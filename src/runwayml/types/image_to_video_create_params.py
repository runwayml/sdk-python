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
    "KlingO3_4k",
    "KlingO3_4kPromptImagePromptImage",
    "KlingO3_4kProviderSettings",
    "KlingO3_4kProviderSettingsMultiPrompt",
    "KlingO3_4kReferencesReferenceImage",
    "Hailuo3",
    "Hailuo3PromptImagePromptImage",
    "Hailuo3ReferenceAudio",
    "Kling3_0_4k",
    "Kling3_0_4kPromptImagePromptImage",
    "Kling3_0_4kProviderSettings",
    "Kling3_0_4kProviderSettingsMultiPrompt",
    "Happyhorse1_0",
    "Happyhorse1_0PromptImagePromptImage",
    "Kling2_5TurboPro",
    "Kling2_5TurboProPromptImagePromptImage",
    "Kling3_0Pro",
    "Kling3_0ProPromptImagePromptImage",
    "Kling3_0ProProviderSettings",
    "Kling3_0ProProviderSettingsMultiPrompt",
    "Kling3_0Standard",
    "Kling3_0StandardPromptImagePromptImage",
    "Kling3_0StandardProviderSettings",
    "Kling3_0StandardProviderSettingsMultiPrompt",
    "KlingO3Pro",
    "KlingO3ProPromptImagePromptImage",
    "KlingO3ProProviderSettings",
    "KlingO3ProProviderSettingsMultiPrompt",
    "KlingO3ProReferencesReferenceImage",
    "KlingO3Standard",
    "KlingO3StandardPromptImagePromptImage",
    "KlingO3StandardProviderSettings",
    "KlingO3StandardProviderSettingsMultiPrompt",
    "KlingO3StandardReferencesReferenceImage",
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
    "GrokImagine1_5",
    "GrokImagine1_5PromptImagePromptImage",
    "Wan3",
    "Wan3PromptImagePromptImage",
    "Wan3ReferenceAudio",
    "Wan3ReferenceVideo",
    "GeminiOmniFlash1_1",
    "GeminiOmniFlash1_1PromptImagePromptImage",
    "Wan3Prime",
    "Wan3PrimePromptImagePromptImage",
    "Wan3PrimeReferenceAudio",
    "Wan3PrimeReferenceVideo",
    "H3Max",
    "H3MaxPromptImagePromptImage",
    "Seedance2_5",
    "Seedance2_5PromptImagePromptImage",
    "Seedance2_5ReferenceAudio",
    "GrokImagine1_5Lite",
    "GrokImagine1_5LitePromptImagePromptImage",
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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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


class KlingO3_4k(TypedDict, total=False):
    model: Required[Literal["klingO3_4k"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[KlingO3_4kPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[KlingO3_4kProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["3840:2160", "2160:3840", "2880:2880"]
    """The resolution of the output video."""

    references: Union[str, Iterable[KlingO3_4kReferencesReferenceImage]]
    """An optional array of reference images (up to 7).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3_4kPromptImagePromptImage(TypedDict, total=False):
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


class KlingO3_4kProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3_4kProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

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


class KlingO3_4kReferencesReferenceImage(TypedDict, total=False):
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

    prompt_image: Required[
        Annotated[Union[str, Iterable[Hailuo3PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
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

    resolution: Literal["768p", "2k", "768P", "2K"]
    """The output resolution. Hailuo 3.0 supports 768p and 2k.

    - `768P` - Deprecated: Use "768p" instead.
    - `2K` - Deprecated: Use "2k" instead.
    """


class Hailuo3PromptImagePromptImage(TypedDict, total=False):
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


class Kling3_0_4k(TypedDict, total=False):
    model: Required[Literal["kling3.0_4k"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Kling3_0_4kPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    cfg_scale: Annotated[float, PropertyInfo(alias="cfgScale")]
    """Creativity/freedom scale for generation.

    0 gives the model maximum creative freedom, 1 makes it follow the prompt most
    strictly. Defaults to 0.5.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[Kling3_0_4kProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["3840:2160", "2160:3840", "2880:2880"]
    """The resolution of the output video."""


class Kling3_0_4kPromptImagePromptImage(TypedDict, total=False):
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


class Kling3_0_4kProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class Kling3_0_4kProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

    multi_prompt: Annotated[Iterable[Kling3_0_4kProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
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

    resolution: Literal["720p", "1080p", "720P", "1080P"]
    """Output quality tier. Output aspect ratio follows the input image.

    - `720P` - Deprecated: Use "720p" instead.
    - `1080P` - Deprecated: Use "1080p" instead.
    """


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


class Kling2_5TurboPro(TypedDict, total=False):
    model: Required[Literal["kling2.5_turbo_pro"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Kling2_5TurboProPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    Image for the first frame of the output video, or an array with first and
    optionally last frames. Output aspect ratio follows the input image; `ratio` is
    not supported on image-to-video. See [image inputs](/assets/inputs#images) for
    file size limits.
    """

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing what should appear in the output video."""

    cfg_scale: Annotated[float, PropertyInfo(alias="cfgScale")]
    """Creativity/freedom scale for generation.

    0 gives the model maximum creative freedom, 1 makes it follow the prompt most
    strictly. Defaults to 0.5.
    """

    duration: Literal[5, 10]
    """The duration of the output video in seconds. Defaults to 5."""


class Kling2_5TurboProPromptImagePromptImage(TypedDict, total=False):
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


class Kling3_0Pro(TypedDict, total=False):
    model: Required[Literal["kling3.0_pro"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Kling3_0ProPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    cfg_scale: Annotated[float, PropertyInfo(alias="cfgScale")]
    """Creativity/freedom scale for generation.

    0 gives the model maximum creative freedom, 1 makes it follow the prompt most
    strictly. Defaults to 0.5.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[Kling3_0ProProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["1920:1080", "1080:1920", "1440:1440"]
    """The resolution of the output video."""


class Kling3_0ProPromptImagePromptImage(TypedDict, total=False):
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


class Kling3_0ProProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class Kling3_0ProProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

    multi_prompt: Annotated[Iterable[Kling3_0ProProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
    """


class Kling3_0Standard(TypedDict, total=False):
    model: Required[Literal["kling3.0_standard"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Kling3_0StandardPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    cfg_scale: Annotated[float, PropertyInfo(alias="cfgScale")]
    """Creativity/freedom scale for generation.

    0 gives the model maximum creative freedom, 1 makes it follow the prompt most
    strictly. Defaults to 0.5.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[Kling3_0StandardProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["1280:720", "720:1280", "960:960"]
    """The resolution of the output video."""


class Kling3_0StandardPromptImagePromptImage(TypedDict, total=False):
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


class Kling3_0StandardProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class Kling3_0StandardProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

    multi_prompt: Annotated[Iterable[Kling3_0StandardProviderSettingsMultiPrompt], PropertyInfo(alias="multiPrompt")]
    """An array of prompt segments for multishot video generation.

    Each segment has its own prompt and duration. Total duration across all segments
    must be between 3 and 15 seconds. `promptText` is still required when `shotType`
    is `"intelligence"`.
    """

    shot_type: Annotated[Literal["intelligence", "customize"], PropertyInfo(alias="shotType")]
    """Shot transition type for multishot videos.

    Defaults to "customize" when multiPrompt is provided.
    """


class KlingO3Pro(TypedDict, total=False):
    model: Required[Literal["klingO3_pro"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[KlingO3ProPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[KlingO3ProProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["1920:1080", "1080:1920", "1440:1440"]
    """The resolution of the output video."""

    references: Union[str, Iterable[KlingO3ProReferencesReferenceImage]]
    """An optional array of reference images (up to 7).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3ProPromptImagePromptImage(TypedDict, total=False):
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


class KlingO3ProProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3ProProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

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


class KlingO3ProReferencesReferenceImage(TypedDict, total=False):
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

    prompt_image: Required[
        Annotated[Union[str, Iterable[KlingO3StandardPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    You may specify an image to use as the first frame of the output video, or an
    array with a first frame and optionally a last frame. When both keyframes are
    provided, output aspect ratio follows the first frame. See
    [image inputs](/assets/inputs#images) for file size limits.
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing what should appear in the output video."""

    provider_settings: Annotated[KlingO3StandardProviderSettings, PropertyInfo(alias="providerSettings")]
    """Provider-specific settings for multishot video generation."""

    ratio: Literal["1280:720", "720:1280", "960:960"]
    """The resolution of the output video."""

    references: Union[str, Iterable[KlingO3StandardReferencesReferenceImage]]
    """An optional array of reference images (up to 7).

    See [our docs](/assets/inputs#images) on image inputs for more information.
    """


class KlingO3StandardPromptImagePromptImage(TypedDict, total=False):
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


class KlingO3StandardProviderSettingsMultiPrompt(TypedDict, total=False):
    duration: Required[int]
    """Duration in seconds for this segment."""

    prompt: Required[str]
    """The text prompt for this segment."""


class KlingO3StandardProviderSettings(TypedDict, total=False):
    """Provider-specific settings for multishot video generation."""

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


class KlingO3StandardReferencesReferenceImage(TypedDict, total=False):
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

    prompt_image: Required[
        Annotated[Union[str, Iterable[Seedance2PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
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


class GrokImagine1_5(TypedDict, total=False):
    model: Required[Literal["grok_imagine_1_5"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[GrokImagine1_5PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """The start frame of the output video.

    The output keeps its aspect ratio, which (width / height) must be between 0.4
    and 2.5. See [our docs](/assets/inputs#images) for image input requirements.
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


class Wan3(TypedDict, total=False):
    model: Required[Literal["wan3"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Wan3PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
    """

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

    reference_videos: Annotated[Iterable[Wan3ReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Wan3PromptImagePromptImage(TypedDict, total=False):
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

    prompt_image: Required[
        Annotated[Union[str, Iterable[GeminiOmniFlash1_1PromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    An image to use as the first frame, or an array containing a first frame and
    optional last frame.
    """

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """
    A non-empty text prompt describing how the video should evolve between the
    provided frames.
    """

    duration: Union[Literal["auto"], int]
    """The duration of the output video in seconds.

    Use "auto" to let the model choose a duration. Numeric durations must be between
    3 and 10 seconds.
    """

    ratio: Literal["640:360", "360:640", "1280:720", "720:1280", "1920:1080", "1080:1920", "3840:2160", "2160:3840"]
    """The resolution and aspect ratio of the output video."""


class GeminiOmniFlash1_1PromptImagePromptImage(TypedDict, total=False):
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


class Wan3Prime(TypedDict, total=False):
    model: Required[Literal["wan3_prime"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[Wan3PrimePromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """An image or array of images.

    Use position `first`/`last` for keyframe mode, or omit position for reference
    images. The two modes cannot be mixed.
    """

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

    reference_videos: Annotated[Iterable[Wan3PrimeReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """An optional array of video references.

    The combined duration across all video references must not exceed 15 seconds.
    See [our docs](/assets/inputs#videos) on video inputs for more information.
    """


class Wan3PrimePromptImagePromptImage(TypedDict, total=False):
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

    prompt_image: Required[
        Annotated[Union[str, Iterable[H3MaxPromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """
    An image to use as the first frame, or an array with a first frame and
    optionally a last frame. A last frame requires a first frame. Each image must be
    at least 256 pixels on both sides.
    """

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


class H3MaxPromptImagePromptImage(TypedDict, total=False):
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

    draft: bool
    """Generate a cheap 480p preview instead of a full-quality video.

    The returned task ID can later be enhanced to a 1080p video with the same
    content by passing it as `draftTaskId` to `text_to_video`. Drafts can be
    enhanced within 7 days of creation. Defaults to false.
    """

    duration: Union[int, Literal["auto"]]
    """Seconds of video to generate, or `auto` to let the model choose.

    `auto` is billed at the variant maximum up front; unused credits are refunded
    after the generation finishes.
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

    The total combined duration must not exceed 30 seconds.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
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

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """


class GrokImagine1_5Lite(TypedDict, total=False):
    model: Required[Literal["grok_imagine_1_5_lite"]]

    prompt_image: Required[
        Annotated[Union[str, Iterable[GrokImagine1_5LitePromptImagePromptImage]], PropertyInfo(alias="promptImage")]
    ]
    """The start frame of the output video.

    The output keeps its aspect ratio, which (width / height) must be between 0.4
    and 2.5. See [our docs](/assets/inputs#images) for image input requirements.
    """

    duration: int
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """An optional text prompt describing motion or changes in the output video."""

    ratio: Literal["auto_480p", "auto_720p", "auto_1080p"]
    """The resolution of the output video.

    The output keeps the input image's aspect ratio. `auto_1080p` is rendered at
    720p and upscaled.
    """


class GrokImagine1_5LitePromptImagePromptImage(TypedDict, total=False):
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
    KlingO3_4k,
    Hailuo3,
    Kling3_0_4k,
    Happyhorse1_0,
    Kling2_5TurboPro,
    Kling3_0Pro,
    Kling3_0Standard,
    KlingO3Pro,
    KlingO3Standard,
    Seedance2,
    Seedance2Fast,
    Seedance2Mini,
    GeminiOmniFlash,
    GrokImagine1_5,
    Wan3,
    GeminiOmniFlash1_1,
    Wan3Prime,
    H3Max,
    Seedance2_5,
    GrokImagine1_5Lite,
]
