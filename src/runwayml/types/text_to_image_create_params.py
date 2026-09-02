# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TextToImageCreateParams",
    "Gen4ImageTurbo",
    "Gen4ImageTurboReferenceImage",
    "Gen4ImageTurboContentModeration",
    "Gen4Image",
    "Gen4ImageContentModeration",
    "Gen4ImageReferenceImage",
    "GptImage2",
    "GptImage2ReferenceImage",
    "GeminiImage3Pro",
    "GeminiImage3ProReferenceImage",
    "GeminiImage3_1Flash",
    "GeminiImage3_1FlashReferenceImage",
    "MuseImage",
    "MuseImageReferenceImage",
    "Seedream5Pro",
    "Seedream5ProReferenceImage",
    "Seedream5Lite",
    "Seedream5LiteReferenceImage",
    "GrokImagineImage2",
    "GrokImagineImage2ReferenceImage",
    "Gemini2_5Flash",
    "Gemini2_5FlashReferenceImage",
]


class Gen4ImageTurbo(TypedDict, total=False):
    model: Required[Literal["gen4_image_turbo"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[
        Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ]
    ]
    """The resolution of the output image."""

    reference_images: Required[Annotated[Iterable[Gen4ImageTurboReferenceImage], PropertyInfo(alias="referenceImages")]]
    """
    An array of one to three images to be used as references for the generated image
    output.
    """

    content_moderation: Annotated[Gen4ImageTurboContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Gen4ImageTurboReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


class Gen4ImageTurboContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Gen4Image(TypedDict, total=False):
    model: Required[Literal["gen4_image"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[
        Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ]
    ]
    """The resolution of the output image."""

    content_moderation: Annotated[Gen4ImageContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    reference_images: Annotated[Iterable[Gen4ImageReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to three images to be used as references for the generated image
    output.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class Gen4ImageContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class Gen4ImageReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


class GptImage2(TypedDict, total=False):
    model: Required[Literal["gpt_image_2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 32,000 characters describing the desired image."""

    ratio: Required[
        Literal[
            "2048:880",
            "1920:1088",
            "1920:1280",
            "1920:1440",
            "1920:1536",
            "1920:1920",
            "1536:1920",
            "1440:1920",
            "1280:1920",
            "1088:1920",
            "2912:1248",
            "2560:1440",
            "2560:1712",
            "2560:1920",
            "2560:2048",
            "2560:2560",
            "2048:2560",
            "1920:2560",
            "1712:2560",
            "1440:2560",
            "3840:1648",
            "3840:2160",
            "3504:2336",
            "3264:2448",
            "3200:2560",
            "2880:2880",
            "2560:3200",
            "2448:3264",
            "2336:3504",
            "2160:3840",
            "auto",
        ]
    ]
    """The resolution of the output image, expressed as `<width>:<height>`.

    Use `auto` to let the model choose.
    """

    background: Literal["transparent", "opaque", "auto"]
    """Background treatment.

    Defaults to `auto`, which lets the model pick. Use `transparent` to generate a
    PNG with an alpha-channel background.
    """

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """The number of images to generate (1-10).

    Increasing this number will affect the number of credits consumed by the
    generation.
    """

    quality: Literal["low", "medium", "high", "auto"]
    """Rendering quality. Higher qualities consume more credits. Defaults to `high`."""

    reference_images: Annotated[Iterable[GptImage2ReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to 16 images to be used as references for the generated image
    output. No two images may share the same tag.
    """


class GptImage2ReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    tag: str
    """A tag to identify the reference image.

    This may be used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


class GeminiImage3Pro(TypedDict, total=False):
    model: Required[Literal["gemini_image3_pro"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """This should describe in detail what should appear in the output."""

    ratio: Required[
        Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
        ]
    ]
    """The resolution of the output image."""

    output_count: Annotated[Literal[1, 4], PropertyInfo(alias="outputCount")]
    """The number of images to generate.

    Increasing this number will affect the number of credits consumed by the
    generation. Up to four images can be generated at once.
    """

    reference_images: Annotated[Iterable[GeminiImage3ProReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to 14 images to be used as references for the generated image
    output. Up to five of those images can pass `subject: "human"` to maintain
    character consistency, and up to nine of those images can pass
    `subject: "object"` with high-fidelity images of objects to include in the
    output.
    """


class GeminiImage3ProReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    subject: Literal["object", "human"]
    """
    Whether this is a reference of a human subject (for character consistency) or an
    object that appears in the output.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


class GeminiImage3_1Flash(TypedDict, total=False):
    model: Required[Literal["gemini_image3.1_flash"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """This should describe in detail what should appear in the output."""

    ratio: Required[
        Literal[
            "512:512",
            "416:624",
            "624:416",
            "432:592",
            "592:432",
            "448:576",
            "576:448",
            "384:672",
            "672:384",
            "768:336",
            "256:1024",
            "1024:256",
            "176:1408",
            "1408:176",
            "1024:1024",
            "832:1248",
            "1248:832",
            "864:1184",
            "1184:864",
            "896:1152",
            "1152:896",
            "768:1344",
            "1344:768",
            "1536:672",
            "512:2048",
            "2048:512",
            "352:2816",
            "2816:352",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "1024:4096",
            "4096:1024",
            "704:5632",
            "5632:704",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
            "2048:8192",
            "8192:2048",
            "1408:11264",
            "11264:1408",
        ]
    ]
    """The resolution of the output image."""

    output_count: Annotated[Literal[1, 4], PropertyInfo(alias="outputCount")]
    """The number of images to generate.

    Increasing this number will affect the number of credits consumed by the
    generation. Up to four images can be generated at once.
    """

    reference_images: Annotated[Iterable[GeminiImage3_1FlashReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to 14 images to be used as references for the generated image
    output. Up to five of those images can pass `subject: "human"` to maintain
    character consistency, and up to nine of those images can pass
    `subject: "object"` with high-fidelity images of objects to include in the
    output.
    """


class GeminiImage3_1FlashReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    subject: Literal["object", "human"]
    """
    Whether this is a reference of a human subject (for character consistency) or an
    object that appears in the output.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


class MuseImage(TypedDict, total=False):
    model: Required[Literal["muse_image"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output image."""

    ratio: Required[
        Literal[
            "2352:1008",
            "2016:1152",
            "1920:1280",
            "1792:1344",
            "1600:1600",
            "1344:1792",
            "1280:1920",
            "1152:2016",
            "auto",
        ]
    ]
    """The resolution of the output image, expressed as `<width>:<height>`.

    Use `auto` to let the model choose the framing from the prompt.
    """

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """The number of images to generate. Each image costs 1 credit."""

    output_format: Annotated[Literal["webp", "png", "jpeg"], PropertyInfo(alias="outputFormat")]
    """The file format of the output image. Defaults to png."""

    reference_images: Annotated[Iterable[MuseImageReferenceImage], PropertyInfo(alias="referenceImages")]
    """Up to 10 images to guide the generation.

    When provided, the model edits and combines them as your prompt describes
    instead of generating from the prompt alone.
    """


class MuseImageReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedream5Pro(TypedDict, total=False):
    model: Required[Literal["seedream5_pro"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 4,000 characters describing the desired image."""

    ratio: Required[
        Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1296:864",
            "864:1296",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2720:1530",
            "1530:2720",
            "2496:1664",
            "1664:2496",
            "auto_1k",
            "auto_2k",
        ]
    ]
    """The resolution of the output image, expressed as `<width>:<height>`.

    Use `auto_1k` or `auto_2k` to let the model pick aspect ratio at a fixed
    resolution tier.
    """

    grounding: bool
    """
    When true, enable live web search so the model can use current brand, trend, or
    event context. Default false for deterministic output.
    """

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """The number of images to generate.

    Increasing this number will affect the number of credits consumed by the
    generation.
    """

    output_format: Annotated[Literal["png", "jpeg"], PropertyInfo(alias="outputFormat")]
    """The file format of the output image. Defaults to png."""

    reference_images: Annotated[Iterable[Seedream5ProReferenceImage], PropertyInfo(alias="referenceImages")]
    """An array of reference images for multi-image fusion and interactive editing.

    Reference by upload order in prompt text (Figure 1, Figure 2, etc.).
    """


class Seedream5ProReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Seedream5Lite(TypedDict, total=False):
    model: Required[Literal["seedream5_lite"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 4,000 characters describing the desired image."""

    ratio: Required[
        Union[
            Literal[
                "2048:2048",
                "2304:1728",
                "1728:2304",
                "2848:1600",
                "1600:2848",
                "2496:1664",
                "1664:2496",
                "3136:1344",
                "3072:3072",
                "3456:2592",
                "2592:3456",
                "4096:2304",
                "2304:4096",
                "3744:2496",
                "2496:3744",
                "4704:2016",
            ],
            str,
        ]
    ]
    """The resolution of the output image, expressed as `<width>:<height>`.

    Also accepts freeform sizes whose width\\**height is between 3686400 and 16777216
    pixels.
    """

    grounding: bool
    """
    When true, enable live web search so the model can use current brand, trend, or
    event context. Default false for deterministic output.
    """

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """The number of images to generate.

    Increasing this number will affect the number of credits consumed by the
    generation.
    """

    output_format: Annotated[Literal["png", "jpeg"], PropertyInfo(alias="outputFormat")]
    """The file format of the output image. Defaults to png."""

    reference_images: Annotated[Iterable[Seedream5LiteReferenceImage], PropertyInfo(alias="referenceImages")]
    """An array of reference images for multi-image fusion and interactive editing.

    Reference by upload order in prompt text (Figure 1, Figure 2, etc.).
    """


class Seedream5LiteReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class GrokImagineImage2(TypedDict, total=False):
    model: Required[Literal["grok_imagine_image_2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt describing what should appear in the output image."""

    ratio: Required[
        Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1248:576",
            "576:1248",
            "1280:576",
            "576:1280",
            "1408:704",
            "704:1408",
            "2048:2048",
            "2816:1584",
            "1584:2816",
            "2368:1776",
            "1776:2368",
            "2496:1664",
            "1664:2496",
            "2912:1344",
            "1344:2912",
            "3200:1440",
            "1440:3200",
            "2912:1456",
            "1456:2912",
            "auto_1k",
            "auto_2k",
        ]
    ]
    """The resolution of the output image, expressed as `<width>:<height>`.

    2K ratios cost 2 additional credits per image. Use `auto_1k` or `auto_2k` to
    pick a resolution tier and let the model choose the framing from the prompt.
    """

    edit: bool
    """
    When true with exactly one reference image, edit that image directly instead of
    using it as a loose visual reference. With several reference images the prompt
    describes how they should be edited or combined. Requires at least one reference
    image.
    """

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """The number of images to generate.

    Increasing this number will affect the number of credits consumed by the
    generation.
    """

    quality: Literal["low", "medium"]
    """How much rendering effort the model spends on the output.

    Defaults to `medium`; `low` is faster and costs 2 fewer credits per image.
    """

    reference_images: Annotated[Iterable[GrokImagineImage2ReferenceImage], PropertyInfo(alias="referenceImages")]
    """Up to 3 images to guide the generation.

    Reference them from `promptText` to describe how each should be used. Each adds
    1 credit to the generation.
    """


class GrokImagineImage2ReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """


class Gemini2_5Flash(TypedDict, total=False):
    model: Required[Literal["gemini_2.5_flash"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """This should describe in detail what should appear in the output."""

    ratio: Required[
        Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
        ]
    ]
    """The resolution of the output image."""

    reference_images: Annotated[Iterable[Gemini2_5FlashReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to three images to be used as references for the generated image
    output.
    """


class Gemini2_5FlashReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text. Must be 3-16 characters,
    start with a letter, and use only letters, digits, and underscores (no hyphens
    or other punctuation).
    """


TextToImageCreateParams: TypeAlias = Union[
    Gen4ImageTurbo,
    Gen4Image,
    GptImage2,
    GeminiImage3Pro,
    GeminiImage3_1Flash,
    MuseImage,
    Seedream5Pro,
    Seedream5Lite,
    GrokImagineImage2,
    Gemini2_5Flash,
]
