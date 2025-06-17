# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import video_upscale_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)
from .._base_client import make_request_options
from ..types.video_upscale_create_response import VideoUpscaleCreateResponse

__all__ = ["VideoUpscaleResource", "AsyncVideoUpscaleResource"]


class VideoUpscaleResource(SyncAPIResource):
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
        model: Literal["upscale_v1"],
        video_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewTaskCreatedResponse:
        """This endpoint will start a new task to upscale a video.

        Videos will be upscaled
        by a factor of 4X, capped at a maximum of 4096px along each side.

        Args:
          model: The model variant to use.

          video_uri: A HTTPS URL pointing to a video or a data URI containing a video. The video must
              be less than 4096px on each side. The video duration may not exceed 40 seconds.
              See [our docs](/assets/inputs#videos) on video inputs for more information.

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
                },
                video_upscale_create_params.VideoUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VideoUpscaleCreateResponse, self._client),
        )


class AsyncVideoUpscaleResource(AsyncAPIResource):
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
        model: Literal["upscale_v1"],
        video_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncNewTaskCreatedResponse:
        """This endpoint will start a new task to upscale a video.

        Videos will be upscaled
        by a factor of 4X, capped at a maximum of 4096px along each side.

        Args:
          model: The model variant to use.

          video_uri: A HTTPS URL pointing to a video or a data URI containing a video. The video must
              be less than 4096px on each side. The video duration may not exceed 40 seconds.
              See [our docs](/assets/inputs#videos) on video inputs for more information.

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
                },
                video_upscale_create_params.VideoUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VideoUpscaleCreateResponse, self._client),
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
