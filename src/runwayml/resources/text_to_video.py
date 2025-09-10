# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import text_to_video_create_params
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
from ..types.text_to_video_create_response import TextToVideoCreateResponse

__all__ = ["TextToVideoResource", "AsyncTextToVideoResource"]


class TextToVideoResource(SyncAPIResource):
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

    def create(
        self,
        *,
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"],
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: Veo 3 videos must be 8 seconds long.

          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: A string representing the aspect ratio of the output video.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/text_to_video",
            body=maybe_transform(
                {
                    "duration": duration,
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "seed": seed,
                },
                text_to_video_create_params.TextToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(TextToVideoCreateResponse, self._client),
        )


class AsyncTextToVideoResource(AsyncAPIResource):
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

    async def create(
        self,
        *,
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_text: str,
        ratio: Literal["1280:720", "720:1280"],
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a text prompt.

        Args:
          duration: Veo 3 videos must be 8 seconds long.

          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: A string representing the aspect ratio of the output video.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/text_to_video",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "seed": seed,
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
