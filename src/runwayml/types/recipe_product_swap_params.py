# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecipeProductSwapParams", "NewProductImage", "OriginalProductImage", "ReferenceVideo"]


class RecipeProductSwapParams(TypedDict, total=False):
    new_product_images: Required[Annotated[Iterable[NewProductImage], PropertyInfo(alias="newProductImages")]]
    """Reference images of the new product (1–10).

    Supply multiple angles when the reference video shows the product from different
    views — optionally label each with `view` ("front", "side", or "back"). A single
    pre-composed reference sheet is also supported (omit `view`). See
    [our docs](/assets/inputs#images) on image inputs.
    """

    original_product_image: Required[Annotated[OriginalProductImage, PropertyInfo(alias="originalProductImage")]]
    """Image of the original product being swapped out.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    reference_video: Required[Annotated[ReferenceVideo, PropertyInfo(alias="referenceVideo")]]
    """Reference video containing the product to swap.

    Duration must be between 1.8 and 15 seconds. See
    [our docs](/assets/inputs#videos) on video inputs.
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """Duration of the output video in seconds (4–15). Defaults to 10 seconds."""

    resolution: Literal["720p", "1080p"]
    """Output video resolution. Defaults to 720p."""


class NewProductImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""

    view: Literal["front", "side", "back"]
    """Optional view label for this reference (front, side, or back).

    Omit when supplying a single reference sheet or when view labels are unknown.
    """


class OriginalProductImage(TypedDict, total=False):
    """Image of the original product being swapped out.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""


class ReferenceVideo(TypedDict, total=False):
    """Reference video containing the product to swap.

    Duration must be between 1.8 and 15 seconds. See [our docs](/assets/inputs#videos) on video inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""
