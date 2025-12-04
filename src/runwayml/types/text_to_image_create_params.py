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
    "Gemini3Pro",
    "Gemini3ProReferenceImage",
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


class Gemini3Pro(TypedDict, total=False):
    model: Required[Literal["gemini_3_pro"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

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

    reference_images: Annotated[Iterable[Gemini3ProReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to 14 images to be used as references for the generated image
    output. Up to five of those images can pass `subject: "human"` to maintain
    character consistency, and up to nine of those images can pass
    `subject: "object"` with high-fidelity images of objects to include in the
    output.
    """


class Gemini3ProReferenceImage(TypedDict, total=False):
    subject: Required[Literal["object", "human"]]
    """
    Whether this is a reference of a human subject (for character consistency) or an
    object that appears in the output.
    """

    uri: Required[str]
    """A HTTPS URL."""

    tag: str
    """A tag to identify the reference image.

    This is used to reference the image in prompt text.
    """


class Gemini2_5Flash(TypedDict, total=False):
    model: Required[Literal["gemini_2.5_flash"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

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


TextToImageCreateParams: TypeAlias = Union[Gen4ImageTurbo, Gen4Image, Gemini3Pro, Gemini2_5Flash]
