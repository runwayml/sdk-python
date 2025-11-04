# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import voice_isolation_create_params
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
from ..types.voice_isolation_create_response import VoiceIsolationCreateResponse

__all__ = ["VoiceIsolationResource", "AsyncVoiceIsolationResource"]


class VoiceIsolationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceIsolationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VoiceIsolationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceIsolationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VoiceIsolationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        audio_uri: str,
        model: Literal["eleven_voice_isolation"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to isolate the voice from the background
        audio. Audio duration must be greater than 4.6 seconds and less than 3600
        seconds.

        Args:
          audio_uri: A HTTPS URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/voice_isolation",
            body=maybe_transform(
                {
                    "audio_uri": audio_uri,
                    "model": model,
                },
                voice_isolation_create_params.VoiceIsolationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VoiceIsolationCreateResponse, self._client),
        )


class AsyncVoiceIsolationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceIsolationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceIsolationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceIsolationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVoiceIsolationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        audio_uri: str,
        model: Literal["eleven_voice_isolation"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to isolate the voice from the background
        audio. Audio duration must be greater than 4.6 seconds and less than 3600
        seconds.

        Args:
          audio_uri: A HTTPS URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/voice_isolation",
            body=await async_maybe_transform(
                {
                    "audio_uri": audio_uri,
                    "model": model,
                },
                voice_isolation_create_params.VoiceIsolationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VoiceIsolationCreateResponse, self._client),
        )


class VoiceIsolationResourceWithRawResponse:
    def __init__(self, voice_isolation: VoiceIsolationResource) -> None:
        self._voice_isolation = voice_isolation

        self.create = to_raw_response_wrapper(
            voice_isolation.create,
        )


class AsyncVoiceIsolationResourceWithRawResponse:
    def __init__(self, voice_isolation: AsyncVoiceIsolationResource) -> None:
        self._voice_isolation = voice_isolation

        self.create = async_to_raw_response_wrapper(
            voice_isolation.create,
        )


class VoiceIsolationResourceWithStreamingResponse:
    def __init__(self, voice_isolation: VoiceIsolationResource) -> None:
        self._voice_isolation = voice_isolation

        self.create = to_streamed_response_wrapper(
            voice_isolation.create,
        )


class AsyncVoiceIsolationResourceWithStreamingResponse:
    def __init__(self, voice_isolation: AsyncVoiceIsolationResource) -> None:
        self._voice_isolation = voice_isolation

        self.create = async_to_streamed_response_wrapper(
            voice_isolation.create,
        )
