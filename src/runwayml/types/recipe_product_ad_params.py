# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecipeProductAdParams", "ProductImage", "StyleImage"]


class RecipeProductAdParams(TypedDict, total=False):
    product_images: Required[Annotated[Iterable[ProductImage], PropertyInfo(alias="productImages")]]
    """Product images (1–10).

    Multiple angles of the same product. All images inform product analysis and
    reference generation; only the first image is used as the primary product
    reference in the storyboard grid. See [our docs](/assets/inputs#images) on image
    inputs.
    """

    version: Required[Literal["2026-06", "2026-07", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-07") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """Duration of the output video in seconds (4–15). Defaults to 10 seconds."""

    product_info: Annotated[str, PropertyInfo(alias="productInfo")]
    """
    Optional product description and specifications to inform creative direction and
    which product elements to highlight.
    """

    ratio: Literal["1280:720", "720:1280", "960:960", "834:1112", "1920:1080", "1080:1920", "1440:1440", "1248:1664"]
    """The resolution of the output video."""

    style_images: Annotated[Iterable[StyleImage], PropertyInfo(alias="styleImages")]
    """Optional style reference images (0–4).

    Defines the visual treatment (lighting, palette, mood). Treated as a moodboard
    when multiple are provided.
    """

    user_concept: Annotated[str, PropertyInfo(alias="userConcept")]
    """
    Optional creative direction describing brand voice, product framing, scene
    specifics, lighting, camera motion, and narrative.
    """


class ProductImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""


class StyleImage(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""
