# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import avatar_video_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.avatar_video_create_response import AvatarVideoCreateResponse

__all__ = ["AvatarVideosResource", "AsyncAvatarVideosResource"]


class AvatarVideosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AvatarVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AvatarVideosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        avatar: avatar_video_create_params.Avatar,
        model: Literal["gwm1_avatars"],
        speech: avatar_video_create_params.Speech,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """Start an asynchronous task to generate a video of an avatar speaking.

        Provide
        `speech` with `type: "audio"` (audio file) or `type: "text"` (text script for
        TTS). Poll `GET /v1/tasks/:id` to check progress and retrieve the output video
        URL once complete.

        Args:
          avatar: The avatar configuration for the session.

          model: The model to use for avatar video generation.

          speech: The speech source for avatar video generation. Either an audio file or text
              script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/avatar_videos",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "model": model,
                    "speech": speech,
                },
                avatar_video_create_params.AvatarVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(AvatarVideoCreateResponse, self._client),
        )


class AsyncAvatarVideosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncAvatarVideosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        avatar: avatar_video_create_params.Avatar,
        model: Literal["gwm1_avatars"],
        speech: avatar_video_create_params.Speech,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """Start an asynchronous task to generate a video of an avatar speaking.

        Provide
        `speech` with `type: "audio"` (audio file) or `type: "text"` (text script for
        TTS). Poll `GET /v1/tasks/:id` to check progress and retrieve the output video
        URL once complete.

        Args:
          avatar: The avatar configuration for the session.

          model: The model to use for avatar video generation.

          speech: The speech source for avatar video generation. Either an audio file or text
              script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/avatar_videos",
            body=await async_maybe_transform(
                {
                    "avatar": avatar,
                    "model": model,
                    "speech": speech,
                },
                avatar_video_create_params.AvatarVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(AvatarVideoCreateResponse, self._client),
        )


class AvatarVideosResourceWithRawResponse:
    def __init__(self, avatar_videos: AvatarVideosResource) -> None:
        self._avatar_videos = avatar_videos

        self.create = to_raw_response_wrapper(
            avatar_videos.create,
        )


class AsyncAvatarVideosResourceWithRawResponse:
    def __init__(self, avatar_videos: AsyncAvatarVideosResource) -> None:
        self._avatar_videos = avatar_videos

        self.create = async_to_raw_response_wrapper(
            avatar_videos.create,
        )


class AvatarVideosResourceWithStreamingResponse:
    def __init__(self, avatar_videos: AvatarVideosResource) -> None:
        self._avatar_videos = avatar_videos

        self.create = to_streamed_response_wrapper(
            avatar_videos.create,
        )


class AsyncAvatarVideosResourceWithStreamingResponse:
    def __init__(self, avatar_videos: AsyncAvatarVideosResource) -> None:
        self._avatar_videos = avatar_videos

        self.create = async_to_streamed_response_wrapper(
            avatar_videos.create,
        )
