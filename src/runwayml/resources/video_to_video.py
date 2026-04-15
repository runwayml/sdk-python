# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import video_to_video_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
    """These endpoints all kick off tasks to create generations."""

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

    @overload
    def create(
        self,
        *,
        model: Literal["gen4_aleph"],
        prompt_text: str,
        video_uri: str,
        content_moderation: video_to_video_create_params.Gen4AlephContentModeration | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Gen4AlephReference] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          video_uri: A HTTPS URL.

          content_moderation: Settings that affect the behavior of the content moderation system.

          ratio: Deprecated. This field is ignored. The resolution of the output video is
              determined by the input video.

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
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["seedance2"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        output_count: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        references: Union[str, Iterable[video_to_video_create_params.Seedance2ReferencesPromptImage]] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoToVideoCreateResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video. Must be an integer from
              4 to 15.

          output_count: The number of video generations to produce.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output video.

          ratio: The resolution of the output video.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of up to 3 video references. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text", "video_uri"], ["model", "prompt_video"])
    def create(
        self,
        *,
        model: Literal["gen4_aleph"] | Literal["seedance2"],
        prompt_text: str | Omit = omit,
        video_uri: str | Omit = omit,
        content_moderation: video_to_video_create_params.Gen4AlephContentModeration | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Gen4AlephReference]
        | Union[str, Iterable[video_to_video_create_params.Seedance2ReferencesPromptImage]]
        | Omit = omit,
        seed: int | Omit = omit,
        prompt_video: str | Omit = omit,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        output_count: int | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoToVideoCreateResponse:
        return self._post(
            "/v1/video_to_video",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "ratio": ratio,
                    "references": references,
                    "seed": seed,
                    "prompt_video": prompt_video,
                    "audio": audio,
                    "duration": duration,
                    "output_count": output_count,
                    "reference_videos": reference_videos,
                },
                video_to_video_create_params.VideoToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VideoToVideoCreateResponse, self._client),
        )


class AsyncVideoToVideoResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

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

    @overload
    async def create(
        self,
        *,
        model: Literal["gen4_aleph"],
        prompt_text: str,
        video_uri: str,
        content_moderation: video_to_video_create_params.Gen4AlephContentModeration | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Gen4AlephReference] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          video_uri: A HTTPS URL.

          content_moderation: Settings that affect the behavior of the content moderation system.

          ratio: Deprecated. This field is ignored. The resolution of the output video is
              determined by the input video.

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
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["seedance2"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        output_count: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        references: Union[str, Iterable[video_to_video_create_params.Seedance2ReferencesPromptImage]] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoToVideoCreateResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video. Must be an integer from
              4 to 15.

          output_count: The number of video generations to produce.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output video.

          ratio: The resolution of the output video.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of up to 3 video references. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text", "video_uri"], ["model", "prompt_video"])
    async def create(
        self,
        *,
        model: Literal["gen4_aleph"] | Literal["seedance2"],
        prompt_text: str | Omit = omit,
        video_uri: str | Omit = omit,
        content_moderation: video_to_video_create_params.Gen4AlephContentModeration | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "1104:832", "960:960", "832:1104", "1584:672", "848:480", "640:480"]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Gen4AlephReference]
        | Union[str, Iterable[video_to_video_create_params.Seedance2ReferencesPromptImage]]
        | Omit = omit,
        seed: int | Omit = omit,
        prompt_video: str | Omit = omit,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        output_count: int | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoToVideoCreateResponse:
        return await self._post(
            "/v1/video_to_video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "ratio": ratio,
                    "references": references,
                    "seed": seed,
                    "prompt_video": prompt_video,
                    "audio": audio,
                    "duration": duration,
                    "output_count": output_count,
                    "reference_videos": reference_videos,
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
