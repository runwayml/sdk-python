# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecipeProductUgcParams", "CharacterImage", "ProductImage"]


class RecipeProductUgcParams(TypedDict, total=False):
    character_image: Required[Annotated[CharacterImage, PropertyInfo(alias="characterImage")]]
    """Image of the character who will appear on camera in the UGC video.

    Aspect ratio (width / height) must be between 0.4 and 4. See
    [our docs](/assets/inputs#images) for image input requirements.
    """

    product_image: Required[Annotated[ProductImage, PropertyInfo(alias="productImage")]]
    """Image of the product being promoted.

    Aspect ratio (width / height) must be between 0.4 and 4. See
    [our docs](/assets/inputs#images) for image input requirements.
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: int
    """Duration of the output video in seconds (4–15). Defaults to 15 seconds."""

    product_info: Annotated[str, PropertyInfo(alias="productInfo")]
    """
    Product details and creative brief — what the product is, key benefits, and any
    specifics the script should reference.
    """

    ratio: Literal["720:1280", "1080:1920"]
    """The resolution of the output video."""

    user_concept: Annotated[str, PropertyInfo(alias="userConcept")]
    """
    Optional creative direction for the UGC video — tone, voice register, specific
    message, or an entire dialog script.
    """


class CharacterImage(TypedDict, total=False):
    """Image of the character who will appear on camera in the UGC video.

    Aspect ratio (width / height) must be between 0.4 and 4. See [our docs](/assets/inputs#images) for image input requirements.
    """

    uri: Required[str]
    """A HTTPS URL."""


class ProductImage(TypedDict, total=False):
    """Image of the product being promoted.

    Aspect ratio (width / height) must be between 0.4 and 4. See [our docs](/assets/inputs#images) for image input requirements.
    """

    uri: Required[str]
    """A HTTPS URL."""
