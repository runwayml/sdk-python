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
    """A HTTPS URL."""

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
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
    """A HTTPS URL."""

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
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

    background: Literal["opaque", "auto"]
    """Background treatment.

    Defaults to `auto`, which lets the model pick. `transparent` is not supported by
    this model.
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
    output.
    """


class GptImage2ReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""

    tag: str
    """A tag to identify the reference image.

    This may be used to reference the image in prompt text.
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
    """A HTTPS URL."""

    subject: Literal["object", "human"]
    """
    Whether this is a reference of a human subject (for character consistency) or an
    object that appears in the output.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
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
    """A HTTPS URL."""

    subject: Literal["object", "human"]
    """
    Whether this is a reference of a human subject (for character consistency) or an
    object that appears in the output.
    """

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
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
    """A HTTPS URL."""

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
    """


TextToImageCreateParams: TypeAlias = Union[
    Gen4ImageTurbo, Gen4Image, GptImage2, GeminiImage3Pro, GeminiImage3_1Flash, Gemini2_5Flash
]
