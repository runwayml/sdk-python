# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageUpscaleCreateParams"]


class ImageUpscaleCreateParams(TypedDict, total=False):
    image_uri: Required[Annotated[str, PropertyInfo(alias="imageUri")]]
    """A HTTPS URL."""

    model: Required[Literal["magnific_precision_upscaler_v2"]]

    flavor: Literal["sublime", "photo", "photo_denoiser"]
    """
    Optimization preset: `sublime` (illustration), `photo` (photographic), or
    `photo_denoiser` (noisy photos).
    """

    scale_factor: Annotated[Literal[2, 4, 8, 16], PropertyInfo(alias="scaleFactor")]
    """Multiplies each input dimension to produce output width and height.

    Defaults to 2.
    """

    sharpen: int
    """Sharpness intensity from 0 (none) to 100."""

    smart_grain: Annotated[int, PropertyInfo(alias="smartGrain")]
    """Grain and texture enhancement from 0 to 100."""

    ultra_detail: Annotated[int, PropertyInfo(alias="ultraDetail")]
    """Fine detail enhancement from 0 to 100."""
