# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import text_to_music_create_params
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
from ..types.text_to_music_create_response import TextToMusicCreateResponse

__all__ = ["TextToMusicResource", "AsyncTextToMusicResource"]


class TextToMusicResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> TextToMusicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TextToMusicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextToMusicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return TextToMusicResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["eleven_music_v2_5"],
        prompt_text: str,
        duration: int | Omit = omit,
        instrumental: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToMusicCreateResponse:
        """
        This endpoint will start a new task to generate a song or instrumental track
        from a text description.

        Args:
          prompt_text: A description of the track to generate, such as its genre, mood, instruments,
              and vocals. Prompts that name specific artists or songs are rejected.

          duration: The length of the track in whole seconds. You are billed for the requested
              length.

          instrumental: When true, the track has no vocals. When omitted, the model decides from the
              prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/text_to_music",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "duration": duration,
                    "instrumental": instrumental,
                },
                text_to_music_create_params.TextToMusicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextToMusicCreateResponse,
        )


class AsyncTextToMusicResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncTextToMusicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextToMusicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextToMusicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncTextToMusicResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["eleven_music_v2_5"],
        prompt_text: str,
        duration: int | Omit = omit,
        instrumental: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToMusicCreateResponse:
        """
        This endpoint will start a new task to generate a song or instrumental track
        from a text description.

        Args:
          prompt_text: A description of the track to generate, such as its genre, mood, instruments,
              and vocals. Prompts that name specific artists or songs are rejected.

          duration: The length of the track in whole seconds. You are billed for the requested
              length.

          instrumental: When true, the track has no vocals. When omitted, the model decides from the
              prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/text_to_music",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "duration": duration,
                    "instrumental": instrumental,
                },
                text_to_music_create_params.TextToMusicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextToMusicCreateResponse,
        )


class TextToMusicResourceWithRawResponse:
    def __init__(self, text_to_music: TextToMusicResource) -> None:
        self._text_to_music = text_to_music

        self.create = to_raw_response_wrapper(
            text_to_music.create,
        )


class AsyncTextToMusicResourceWithRawResponse:
    def __init__(self, text_to_music: AsyncTextToMusicResource) -> None:
        self._text_to_music = text_to_music

        self.create = async_to_raw_response_wrapper(
            text_to_music.create,
        )


class TextToMusicResourceWithStreamingResponse:
    def __init__(self, text_to_music: TextToMusicResource) -> None:
        self._text_to_music = text_to_music

        self.create = to_streamed_response_wrapper(
            text_to_music.create,
        )


class AsyncTextToMusicResourceWithStreamingResponse:
    def __init__(self, text_to_music: AsyncTextToMusicResource) -> None:
        self._text_to_music = text_to_music

        self.create = async_to_streamed_response_wrapper(
            text_to_music.create,
        )
