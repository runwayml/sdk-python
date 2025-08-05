# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TextToImageCreateParams", "ContentModeration", "ReferenceImage"]


class TextToImageCreateParams(TypedDict, total=False):
    model: Required[Literal["gen4_image", "gen4_image_turbo"]]
    """The model variant to use."""

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    ratio: Required[
        Literal[
            "1920:1080",
            "1080:1920",
            "1024:1024",
            "1360:768",
            "1080:1080",
            "1168:880",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ]
    ]
    """The resolution of the output image(s)."""

    content_moderation: Annotated[ContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    reference_images: Annotated[Iterable[ReferenceImage], PropertyInfo(alias="referenceImages")]
    """
    An array of up to three images to be used as references for the generated image
    output.

    For `gen4_image_turbo`, _at least one_ reference image is required.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """


class ContentModeration(TypedDict, total=False):
    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class ReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """
    A HTTPS URL or data URI containing an encoded image to be used as reference for
    the generated output image. See [our docs](/assets/inputs#images) on image
    inputs for more information.
    """

    tag: str
    """A name used to refer to the image reference, from 3 to 16 characters in length.

    Tags must be alphanumeric (plus underscores) and start with a letter. You can
    refer to the reference image's tag in the prompt text with at-mention syntax:
    `@tag`. Tags are case-sensitive.
    """
