# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoUpscaleCreateParams"]


class VideoUpscaleCreateParams(TypedDict, total=False):
    model: Required[Literal["magnific_video_upscaler_creative"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL."""

    creativity: int
    """How much AI-generated detail to add during upscaling, from 0 (faithful) to 100."""

    flavor: Literal["vivid", "natural"]
    """
    Processing style: `vivid` for enhanced color and detail, `natural` for faithful
    reproduction.
    """

    fps_boost: Annotated[bool, PropertyInfo(alias="fpsBoost")]
    """Whether to increase the output frame rate."""

    resolution: Literal["720p", "1k", "2k", "4k"]
    """Target output resolution from 720p to 4k. Defaults to `2k`."""

    sharpen: int
    """Sharpness intensity from 0 (none) to 100."""

    smart_grain: Annotated[int, PropertyInfo(alias="smartGrain")]
    """Grain and texture enhancement from 0 to 100."""
