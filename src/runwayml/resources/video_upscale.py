# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import video_upscale_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.video_upscale_create_response import VideoUpscaleCreateResponse

__all__ = ["VideoUpscaleResource", "AsyncVideoUpscaleResource"]


class VideoUpscaleResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> VideoUpscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoUpscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoUpscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VideoUpscaleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["magnific_video_upscaler_creative"],
        video_uri: str,
        creativity: int | Omit = omit,
        flavor: Literal["vivid", "natural"] | Omit = omit,
        fps_boost: bool | Omit = omit,
        resolution: Literal["720p", "1k", "2k", "4k"] | Omit = omit,
        sharpen: int | Omit = omit,
        smart_grain: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUpscaleCreateResponse:
        """This endpoint starts a task to upscale a video.

        Set `model` to choose the
        upscaler.

        Args:
          video_uri: A HTTPS URL.

          creativity: How much AI-generated detail to add during upscaling, from 0 (faithful) to 100.

          flavor: Processing style: `vivid` for enhanced color and detail, `natural` for faithful
              reproduction.

          fps_boost: Whether to increase the output frame rate.

          resolution: Target output resolution from 720p to 4k. Defaults to `2k`.

          sharpen: Sharpness intensity from 0 (none) to 100.

          smart_grain: Grain and texture enhancement from 0 to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/video_upscale",
            body=maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "creativity": creativity,
                    "flavor": flavor,
                    "fps_boost": fps_boost,
                    "resolution": resolution,
                    "sharpen": sharpen,
                    "smart_grain": smart_grain,
                },
                video_upscale_create_params.VideoUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoUpscaleCreateResponse,
        )


class AsyncVideoUpscaleResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncVideoUpscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoUpscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoUpscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVideoUpscaleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["magnific_video_upscaler_creative"],
        video_uri: str,
        creativity: int | Omit = omit,
        flavor: Literal["vivid", "natural"] | Omit = omit,
        fps_boost: bool | Omit = omit,
        resolution: Literal["720p", "1k", "2k", "4k"] | Omit = omit,
        sharpen: int | Omit = omit,
        smart_grain: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUpscaleCreateResponse:
        """This endpoint starts a task to upscale a video.

        Set `model` to choose the
        upscaler.

        Args:
          video_uri: A HTTPS URL.

          creativity: How much AI-generated detail to add during upscaling, from 0 (faithful) to 100.

          flavor: Processing style: `vivid` for enhanced color and detail, `natural` for faithful
              reproduction.

          fps_boost: Whether to increase the output frame rate.

          resolution: Target output resolution from 720p to 4k. Defaults to `2k`.

          sharpen: Sharpness intensity from 0 (none) to 100.

          smart_grain: Grain and texture enhancement from 0 to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/video_upscale",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "creativity": creativity,
                    "flavor": flavor,
                    "fps_boost": fps_boost,
                    "resolution": resolution,
                    "sharpen": sharpen,
                    "smart_grain": smart_grain,
                },
                video_upscale_create_params.VideoUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoUpscaleCreateResponse,
        )


class VideoUpscaleResourceWithRawResponse:
    def __init__(self, video_upscale: VideoUpscaleResource) -> None:
        self._video_upscale = video_upscale

        self.create = to_raw_response_wrapper(
            video_upscale.create,
        )


class AsyncVideoUpscaleResourceWithRawResponse:
    def __init__(self, video_upscale: AsyncVideoUpscaleResource) -> None:
        self._video_upscale = video_upscale

        self.create = async_to_raw_response_wrapper(
            video_upscale.create,
        )


class VideoUpscaleResourceWithStreamingResponse:
    def __init__(self, video_upscale: VideoUpscaleResource) -> None:
        self._video_upscale = video_upscale

        self.create = to_streamed_response_wrapper(
            video_upscale.create,
        )


class AsyncVideoUpscaleResourceWithStreamingResponse:
    def __init__(self, video_upscale: AsyncVideoUpscaleResource) -> None:
        self._video_upscale = video_upscale

        self.create = async_to_streamed_response_wrapper(
            video_upscale.create,
        )
