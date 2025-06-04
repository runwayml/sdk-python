# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoUpscaleCreateParams"]


class VideoUpscaleCreateParams(TypedDict, total=False):
    model: Required[Literal["upscale_v1"]]
    """The model variant to use."""

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL pointing to a video or a data URI containing a video.

    The video must be less than 4096px on each side. The video duration may not
    exceed 40 seconds. See [our docs](/assets/inputs#videos) on video inputs for
    more information.
    """
