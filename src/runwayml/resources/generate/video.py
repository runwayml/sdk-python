# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from runwayml.lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.generate import video_create_params
from ...types.generate.video_create_response import RoutedVideoDryRun, RoutedVideoTaskCreated

__all__ = ["VideoResource", "AsyncVideoResource"]


class VideoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VideoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config_id: str,
        input: video_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Start a video generation task using a saved Model Router config instead of
        naming a model.

        For a routing decision without creating a task, use `preview` instead.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic video generation input. Fields are optional; the router selects a
              model and maps these options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/generate/video",
            body=maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RoutedVideoTaskCreated, self._client),
        )

    def preview(
        self,
        *,
        config_id: str,
        input: video_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutedVideoDryRun:
        """
        Run Model Router selection for a video request without creating a task or
        billing a generation.

        Returns the same routing metadata as `create`, including the selected model and
        estimated cost. Prefer this over passing `dry_run` to `create`.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic video generation input. Fields are optional; the router selects a
              model and maps these options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/generate/video",
            body=maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                    "dry_run": True,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutedVideoDryRun,
        )


class AsyncVideoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVideoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config_id: str,
        input: video_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Start a video generation task using a saved Model Router config instead of
        naming a model.

        For a routing decision without creating a task, use `preview` instead.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic video generation input. Fields are optional; the router selects a
              model and maps these options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/generate/video",
            body=await async_maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RoutedVideoTaskCreated, self._client),
        )

    async def preview(
        self,
        *,
        config_id: str,
        input: video_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutedVideoDryRun:
        """
        Run Model Router selection for a video request without creating a task or
        billing a generation.

        Returns the same routing metadata as `create`, including the selected model and
        estimated cost. Prefer this over passing `dry_run` to `create`.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic video generation input. Fields are optional; the router selects a
              model and maps these options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/generate/video",
            body=await async_maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                    "dry_run": True,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutedVideoDryRun,
        )


class VideoResourceWithRawResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.create = to_raw_response_wrapper(
            video.create,
        )
        self.preview = to_raw_response_wrapper(
            video.preview,
        )


class AsyncVideoResourceWithRawResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_raw_response_wrapper(
            video.create,
        )
        self.preview = async_to_raw_response_wrapper(
            video.preview,
        )


class VideoResourceWithStreamingResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.create = to_streamed_response_wrapper(
            video.create,
        )
        self.preview = to_streamed_response_wrapper(
            video.preview,
        )


class AsyncVideoResourceWithStreamingResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_streamed_response_wrapper(
            video.create,
        )
        self.preview = async_to_streamed_response_wrapper(
            video.preview,
        )
