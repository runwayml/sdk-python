# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoUpscaleCreateParams", "MagnificVideoUpscalerCreative", "EnhanceFrameRate"]


class MagnificVideoUpscalerCreative(TypedDict, total=False):
    model: Required[Literal["magnific_video_upscaler_creative"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

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


class EnhanceFrameRate(TypedDict, total=False):
    model: Required[Literal["enhance_frame_rate"]]

    target_framerate: Required[
        Annotated[
            Literal["24", "25", "30", "48", "50", "60", "120", "23_98", "29_97", "59_94"],
            PropertyInfo(alias="targetFramerate"),
        ]
    ]
    """The output frame rate."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """


VideoUpscaleCreateParams: TypeAlias = Union[MagnificVideoUpscalerCreative, EnhanceFrameRate]
