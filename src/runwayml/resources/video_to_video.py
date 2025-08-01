# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import video_to_video_create_params
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
from ..types.video_to_video_create_response import VideoToVideoCreateResponse

__all__ = ["VideoToVideoResource", "AsyncVideoToVideoResource"]


class VideoToVideoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VideoToVideoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["gen4_aleph"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"],
        video_uri: str,
        content_moderation: video_to_video_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        references: Iterable[video_to_video_create_params.Reference] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          video_uri: A HTTPS URL pointing to a video or a data URI containing a video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          content_moderation: Settings that affect the behavior of the content moderation system.

          references: An array of references. Currently up to one reference is supported. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/video_to_video",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "references": references,
                    "seed": seed,
                },
                video_to_video_create_params.VideoToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VideoToVideoCreateResponse, self._client),
        )


class AsyncVideoToVideoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVideoToVideoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["gen4_aleph"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"],
        video_uri: str,
        content_moderation: video_to_video_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        references: Iterable[video_to_video_create_params.Reference] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          video_uri: A HTTPS URL pointing to a video or a data URI containing a video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          content_moderation: Settings that affect the behavior of the content moderation system.

          references: An array of references. Currently up to one reference is supported. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/video_to_video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "references": references,
                    "seed": seed,
                },
                video_to_video_create_params.VideoToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VideoToVideoCreateResponse, self._client),
        )


class VideoToVideoResourceWithRawResponse:
    def __init__(self, video_to_video: VideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = to_raw_response_wrapper(
            video_to_video.create,
        )


class AsyncVideoToVideoResourceWithRawResponse:
    def __init__(self, video_to_video: AsyncVideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = async_to_raw_response_wrapper(
            video_to_video.create,
        )


class VideoToVideoResourceWithStreamingResponse:
    def __init__(self, video_to_video: VideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = to_streamed_response_wrapper(
            video_to_video.create,
        )


class AsyncVideoToVideoResourceWithStreamingResponse:
    def __init__(self, video_to_video: AsyncVideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = async_to_streamed_response_wrapper(
            video_to_video.create,
        )
