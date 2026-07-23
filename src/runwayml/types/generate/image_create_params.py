# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ImageCreateParams", "Input", "InputContentModeration", "InputReferenceImage"]


class ImageCreateParams(TypedDict, total=False):
    config_id: Required[Annotated[str, PropertyInfo(alias="configId")]]
    """The slug of a saved Model Router config to route this request with."""

    input: Required[Input]
    """Model-agnostic image generation input.

    The router selects a model and maps these options to it.
    """


class InputContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class InputReferenceImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""


class Input(TypedDict, total=False):
    """Model-agnostic image generation input.

    The router selects a model and maps these options to it.
    """

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text prompt describing the desired image."""

    aspect_ratio: Annotated[
        Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9", "2:3", "3:2", "4:5", "5:4"],
        PropertyInfo(alias="aspectRatio"),
    ]
    """Desired aspect ratio.

    Models that do not support the requested aspect are excluded.
    """

    content_moderation: Annotated[InputContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    output_count: Annotated[int, PropertyInfo(alias="outputCount")]
    """Number of images to generate (1–10).

    Models that cannot produce the exact count are excluded and cost scales with
    this value.
    """

    reference_images: Annotated[Iterable[InputReferenceImage], PropertyInfo(alias="referenceImages")]
    """Optional reference images for models that support them.

    Tags are assigned per model when omitted.
    """

    resolution: Literal["1k", "2k", "4k"]
    """Desired megapixel tier.

    Models that do not support the requested tier are excluded.
    """

    seed: int
    """A seed for reproducible generation.

    Only gen4_image and gen4_image_turbo accept this field.
    """
