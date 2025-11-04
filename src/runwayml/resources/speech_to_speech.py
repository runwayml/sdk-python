# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import speech_to_speech_create_params
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
from ..lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)
from .._base_client import make_request_options
from ..types.speech_to_speech_create_response import SpeechToSpeechCreateResponse

__all__ = ["SpeechToSpeechResource", "AsyncSpeechToSpeechResource"]


class SpeechToSpeechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SpeechToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return SpeechToSpeechResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        media: speech_to_speech_create_params.Media,
        model: Literal["eleven_multilingual_sts_v2"],
        voice: speech_to_speech_create_params.Voice,
        remove_background_noise: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to convert speech from one voice to another
        in audio or video.

        Args:
          media: The media to use as a source for the dialogue for the generated speech.

          voice: A voice preset from the RunwayML API.

          remove_background_noise: Whether to remove background noise from the generated speech.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/speech_to_speech",
            body=maybe_transform(
                {
                    "media": media,
                    "model": model,
                    "voice": voice,
                    "remove_background_noise": remove_background_noise,
                },
                speech_to_speech_create_params.SpeechToSpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=create_waitable_resource(SpeechToSpeechCreateResponse, self._client),
        )


class AsyncSpeechToSpeechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncSpeechToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncSpeechToSpeechResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        media: speech_to_speech_create_params.Media,
        model: Literal["eleven_multilingual_sts_v2"],
        voice: speech_to_speech_create_params.Voice,
        remove_background_noise: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to convert speech from one voice to another
        in audio or video.

        Args:
          media: The media to use as a source for the dialogue for the generated speech.

          voice: A voice preset from the RunwayML API.

          remove_background_noise: Whether to remove background noise from the generated speech.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/speech_to_speech",
            body=await async_maybe_transform(
                {
                    "media": media,
                    "model": model,
                    "voice": voice,
                    "remove_background_noise": remove_background_noise,
                },
                speech_to_speech_create_params.SpeechToSpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=create_async_waitable_resource(SpeechToSpeechCreateResponse, self._client),
        )


class SpeechToSpeechResourceWithRawResponse:
    def __init__(self, speech_to_speech: SpeechToSpeechResource) -> None:
        self._speech_to_speech = speech_to_speech

        self.create = to_raw_response_wrapper(
            speech_to_speech.create,
        )


class AsyncSpeechToSpeechResourceWithRawResponse:
    def __init__(self, speech_to_speech: AsyncSpeechToSpeechResource) -> None:
        self._speech_to_speech = speech_to_speech

        self.create = async_to_raw_response_wrapper(
            speech_to_speech.create,
        )


class SpeechToSpeechResourceWithStreamingResponse:
    def __init__(self, speech_to_speech: SpeechToSpeechResource) -> None:
        self._speech_to_speech = speech_to_speech

        self.create = to_streamed_response_wrapper(
            speech_to_speech.create,
        )


class AsyncSpeechToSpeechResourceWithStreamingResponse:
    def __init__(self, speech_to_speech: AsyncSpeechToSpeechResource) -> None:
        self._speech_to_speech = speech_to_speech

        self.create = async_to_streamed_response_wrapper(
            speech_to_speech.create,
        )
