# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import voice_dubbing_create_params
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
from ..types.voice_dubbing_create_response import VoiceDubbingCreateResponse

__all__ = ["VoiceDubbingResource", "AsyncVoiceDubbingResource"]


class VoiceDubbingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceDubbingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VoiceDubbingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceDubbingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VoiceDubbingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        audio_uri: str,
        model: Literal["eleven_voice_dubbing"],
        target_lang: Literal[
            "en",
            "hi",
            "pt",
            "zh",
            "es",
            "fr",
            "de",
            "ja",
            "ar",
            "ru",
            "ko",
            "id",
            "it",
            "nl",
            "tr",
            "pl",
            "sv",
            "fil",
            "ms",
            "ro",
            "uk",
            "el",
            "cs",
            "da",
            "fi",
            "bg",
            "hr",
            "sk",
            "ta",
        ],
        disable_voice_cloning: bool | Omit = omit,
        drop_background_audio: bool | Omit = omit,
        num_speakers: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to dub audio content to a target language.

        Args:
          audio_uri: A HTTPS URL.

          target_lang: The target language code to dub the audio to (e.g., "es" for Spanish, "fr" for
              French).

          disable_voice_cloning: Whether to disable voice cloning and use a generic voice instead.

          drop_background_audio: Whether to remove background audio from the dubbed output.

          num_speakers: The number of speakers in the audio. If not provided, it will be detected
              automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/voice_dubbing",
            body=maybe_transform(
                {
                    "audio_uri": audio_uri,
                    "model": model,
                    "target_lang": target_lang,
                    "disable_voice_cloning": disable_voice_cloning,
                    "drop_background_audio": drop_background_audio,
                    "num_speakers": num_speakers,
                },
                voice_dubbing_create_params.VoiceDubbingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VoiceDubbingCreateResponse, self._client),
        )


class AsyncVoiceDubbingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceDubbingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceDubbingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceDubbingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVoiceDubbingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        audio_uri: str,
        model: Literal["eleven_voice_dubbing"],
        target_lang: Literal[
            "en",
            "hi",
            "pt",
            "zh",
            "es",
            "fr",
            "de",
            "ja",
            "ar",
            "ru",
            "ko",
            "id",
            "it",
            "nl",
            "tr",
            "pl",
            "sv",
            "fil",
            "ms",
            "ro",
            "uk",
            "el",
            "cs",
            "da",
            "fi",
            "bg",
            "hr",
            "sk",
            "ta",
        ],
        disable_voice_cloning: bool | Omit = omit,
        drop_background_audio: bool | Omit = omit,
        num_speakers: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to dub audio content to a target language.

        Args:
          audio_uri: A HTTPS URL.

          target_lang: The target language code to dub the audio to (e.g., "es" for Spanish, "fr" for
              French).

          disable_voice_cloning: Whether to disable voice cloning and use a generic voice instead.

          drop_background_audio: Whether to remove background audio from the dubbed output.

          num_speakers: The number of speakers in the audio. If not provided, it will be detected
              automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/voice_dubbing",
            body=await async_maybe_transform(
                {
                    "audio_uri": audio_uri,
                    "model": model,
                    "target_lang": target_lang,
                    "disable_voice_cloning": disable_voice_cloning,
                    "drop_background_audio": drop_background_audio,
                    "num_speakers": num_speakers,
                },
                voice_dubbing_create_params.VoiceDubbingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VoiceDubbingCreateResponse, self._client),
        )


class VoiceDubbingResourceWithRawResponse:
    def __init__(self, voice_dubbing: VoiceDubbingResource) -> None:
        self._voice_dubbing = voice_dubbing

        self.create = to_raw_response_wrapper(
            voice_dubbing.create,
        )


class AsyncVoiceDubbingResourceWithRawResponse:
    def __init__(self, voice_dubbing: AsyncVoiceDubbingResource) -> None:
        self._voice_dubbing = voice_dubbing

        self.create = async_to_raw_response_wrapper(
            voice_dubbing.create,
        )


class VoiceDubbingResourceWithStreamingResponse:
    def __init__(self, voice_dubbing: VoiceDubbingResource) -> None:
        self._voice_dubbing = voice_dubbing

        self.create = to_streamed_response_wrapper(
            voice_dubbing.create,
        )


class AsyncVoiceDubbingResourceWithStreamingResponse:
    def __init__(self, voice_dubbing: AsyncVoiceDubbingResource) -> None:
        self._voice_dubbing = voice_dubbing

        self.create = async_to_streamed_response_wrapper(
            voice_dubbing.create,
        )
