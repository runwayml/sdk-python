# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import text_to_video_create_params
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
from ..types.text_to_video_create_response import TextToVideoCreateResponse

__all__ = ["TextToVideoResource", "AsyncTextToVideoResource"]


class TextToVideoResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> TextToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TextToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return TextToVideoResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        duration: int,
        model: Literal["gen4.5"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"],
        content_moderation: text_to_video_create_params.Gen4_5ContentModeration | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: The number of seconds of duration for the output video. Must be an integer from
              2 to 10.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          content_moderation: Settings that affect the behavior of the content moderation system.

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
        model: Literal["veo3.1"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        audio: bool | Omit = omit,
        duration: Literal[4, 6, 8] | Omit = omit,
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video.

          negative_prompt: Text describing what should not appear in the output video.

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
        model: Literal["veo3.1_fast"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        audio: bool | Omit = omit,
        duration: Literal[4, 6, 8] | Omit = omit,
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video.

          negative_prompt: Text describing what should not appear in the output video.

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
        model: Literal["happyhorse_1_0"],
        prompt_text: str,
        duration: int | Omit = omit,
        ratio: Literal[
            "1280:720",
            "720:1280",
            "960:960",
            "1108:832",
            "832:1108",
            "1920:1080",
            "1080:1920",
            "1440:1440",
            "1662:1248",
            "1248:1662",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 2500 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video.

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
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Omit = omit,
        reference_audio: Iterable[text_to_video_create_params.Seedance2ReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2Reference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["seedance2_fast"],
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
        reference_audio: Iterable[text_to_video_create_params.Seedance2FastReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2FastReference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2FastReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["seedance2_mini"],
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
        reference_audio: Iterable[text_to_video_create_params.Seedance2MiniReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2MiniReference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2MiniReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["gemini_omni_flash"],
        prompt_text: str,
        duration: int | Omit = omit,
        ratio: Literal["1280:720", "720:1280"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt describing the video to generate.

          duration: The duration of the output video in seconds, as a whole number from 3 to 10.

          ratio: The aspect ratio of the output video: `1280:720` (landscape) or `720:1280`
              (portrait).

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
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          negative_prompt: Text describing what should not appear in the output video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["duration", "model", "prompt_text", "ratio"], ["model", "prompt_text", "ratio"], ["model", "prompt_text"]
    )
    def create(
        self,
        *,
        duration: int | Literal[4, 6, 8] | Literal[8] | Omit = omit,
        model: Literal["gen4.5"]
        | Literal["veo3.1"]
        | Literal["veo3.1_fast"]
        | Literal["happyhorse_1_0"]
        | Literal["seedance2"]
        | Literal["seedance2_fast"]
        | Literal["seedance2_mini"]
        | Literal["gemini_omni_flash"]
        | Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"]
        | Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]
        | Literal[
            "1280:720",
            "720:1280",
            "960:960",
            "1108:832",
            "832:1108",
            "1920:1080",
            "1080:1920",
            "1440:1440",
            "1662:1248",
            "1248:1662",
        ]
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
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
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
        content_moderation: text_to_video_create_params.Gen4_5ContentModeration | Omit = omit,
        seed: int | Omit = omit,
        audio: bool | Omit = omit,
        negative_prompt: str | Omit = omit,
        reference_audio: Iterable[text_to_video_create_params.Seedance2ReferenceAudio]
        | Iterable[text_to_video_create_params.Seedance2FastReferenceAudio]
        | Iterable[text_to_video_create_params.Seedance2MiniReferenceAudio]
        | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2Reference]
        | Iterable[text_to_video_create_params.Seedance2FastReference]
        | Iterable[text_to_video_create_params.Seedance2MiniReference]
        | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2ReferenceVideo]
        | Iterable[text_to_video_create_params.Seedance2FastReferenceVideo]
        | Iterable[text_to_video_create_params.Seedance2MiniReferenceVideo]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/text_to_video",
            body=maybe_transform(
                {
                    "duration": duration,
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "seed": seed,
                    "audio": audio,
                    "negative_prompt": negative_prompt,
                    "reference_audio": reference_audio,
                    "references": references,
                    "reference_videos": reference_videos,
                },
                text_to_video_create_params.TextToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(TextToVideoCreateResponse, self._client),
        )


class AsyncTextToVideoResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncTextToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncTextToVideoResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        duration: int,
        model: Literal["gen4.5"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"],
        content_moderation: text_to_video_create_params.Gen4_5ContentModeration | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: The number of seconds of duration for the output video. Must be an integer from
              2 to 10.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          content_moderation: Settings that affect the behavior of the content moderation system.

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
        model: Literal["veo3.1"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        audio: bool | Omit = omit,
        duration: Literal[4, 6, 8] | Omit = omit,
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video.

          negative_prompt: Text describing what should not appear in the output video.

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
        model: Literal["veo3.1_fast"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        audio: bool | Omit = omit,
        duration: Literal[4, 6, 8] | Omit = omit,
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          audio: Whether to generate audio for the video. Audio inclusion affects pricing.

          duration: The number of seconds of duration for the output video.

          negative_prompt: Text describing what should not appear in the output video.

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
        model: Literal["happyhorse_1_0"],
        prompt_text: str,
        duration: int | Omit = omit,
        ratio: Literal[
            "1280:720",
            "720:1280",
            "960:960",
            "1108:832",
            "832:1108",
            "1920:1080",
            "1080:1920",
            "1440:1440",
            "1662:1248",
            "1248:1662",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty string up to 2500 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video.

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
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Omit = omit,
        reference_audio: Iterable[text_to_video_create_params.Seedance2ReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2Reference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["seedance2_fast"],
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
        reference_audio: Iterable[text_to_video_create_params.Seedance2FastReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2FastReference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2FastReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["seedance2_mini"],
        prompt_text: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
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
        reference_audio: Iterable[text_to_video_create_params.Seedance2MiniReferenceAudio] | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2MiniReference] | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2MiniReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt up to 3500 characters describing what should appear in
              the output.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          ratio: The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

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
        model: Literal["gemini_omni_flash"],
        prompt_text: str,
        duration: int | Omit = omit,
        ratio: Literal["1280:720", "720:1280"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          prompt_text: A non-empty text prompt describing the video to generate.

          duration: The duration of the output video in seconds, as a whole number from 3 to 10.

          ratio: The aspect ratio of the output video: `1280:720` (landscape) or `720:1280`
              (portrait).

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
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        negative_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output video.

          negative_prompt: Text describing what should not appear in the output video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["duration", "model", "prompt_text", "ratio"], ["model", "prompt_text", "ratio"], ["model", "prompt_text"]
    )
    async def create(
        self,
        *,
        duration: int | Literal[4, 6, 8] | Literal[8] | Omit = omit,
        model: Literal["gen4.5"]
        | Literal["veo3.1"]
        | Literal["veo3.1_fast"]
        | Literal["happyhorse_1_0"]
        | Literal["seedance2"]
        | Literal["seedance2_fast"]
        | Literal["seedance2_mini"]
        | Literal["gemini_omni_flash"]
        | Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"]
        | Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]
        | Literal[
            "1280:720",
            "720:1280",
            "960:960",
            "1108:832",
            "832:1108",
            "1920:1080",
            "1080:1920",
            "1440:1440",
            "1662:1248",
            "1248:1662",
        ]
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
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
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
        content_moderation: text_to_video_create_params.Gen4_5ContentModeration | Omit = omit,
        seed: int | Omit = omit,
        audio: bool | Omit = omit,
        negative_prompt: str | Omit = omit,
        reference_audio: Iterable[text_to_video_create_params.Seedance2ReferenceAudio]
        | Iterable[text_to_video_create_params.Seedance2FastReferenceAudio]
        | Iterable[text_to_video_create_params.Seedance2MiniReferenceAudio]
        | Omit = omit,
        references: Iterable[text_to_video_create_params.Seedance2Reference]
        | Iterable[text_to_video_create_params.Seedance2FastReference]
        | Iterable[text_to_video_create_params.Seedance2MiniReference]
        | Omit = omit,
        reference_videos: Iterable[text_to_video_create_params.Seedance2ReferenceVideo]
        | Iterable[text_to_video_create_params.Seedance2FastReferenceVideo]
        | Iterable[text_to_video_create_params.Seedance2MiniReferenceVideo]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/text_to_video",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "seed": seed,
                    "audio": audio,
                    "negative_prompt": negative_prompt,
                    "reference_audio": reference_audio,
                    "references": references,
                    "reference_videos": reference_videos,
                },
                text_to_video_create_params.TextToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(TextToVideoCreateResponse, self._client),
        )


class TextToVideoResourceWithRawResponse:
    def __init__(self, text_to_video: TextToVideoResource) -> None:
        self._text_to_video = text_to_video

        self.create = to_raw_response_wrapper(
            text_to_video.create,
        )


class AsyncTextToVideoResourceWithRawResponse:
    def __init__(self, text_to_video: AsyncTextToVideoResource) -> None:
        self._text_to_video = text_to_video

        self.create = async_to_raw_response_wrapper(
            text_to_video.create,
        )


class TextToVideoResourceWithStreamingResponse:
    def __init__(self, text_to_video: TextToVideoResource) -> None:
        self._text_to_video = text_to_video

        self.create = to_streamed_response_wrapper(
            text_to_video.create,
        )


class AsyncTextToVideoResourceWithStreamingResponse:
    def __init__(self, text_to_video: AsyncTextToVideoResource) -> None:
        self._text_to_video = text_to_video

        self.create = async_to_streamed_response_wrapper(
            text_to_video.create,
        )
