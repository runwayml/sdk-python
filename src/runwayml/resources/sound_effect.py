# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import sound_effect_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sound_effect_create_response import SoundEffectCreateResponse

__all__ = ["SoundEffectResource", "AsyncSoundEffectResource"]


class SoundEffectResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> SoundEffectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SoundEffectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SoundEffectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return SoundEffectResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: Literal["seed_audio"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        reference_audios: SequenceNotStr[str] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        """
        This endpoint will start a new task to generate sound effects from a text
        description.

        Args:
          prompt_text: A non-empty text prompt. For text-to-speech, the words to speak. For
              text-to-audio, a scene description that can include voice direction, dialogue,
              music, and sound effects.

          loudness_rate: Relative output loudness. Negative is quieter, positive is louder; 0 is normal.

          output_format: Output audio container/format.

          pitch_rate: Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.

          reference_audios: Up to three reference audio clips. When provided, reference them in promptText
              as @Audio1, @Audio2, and @Audio3 in order.

          sample_rate: Output sample rate in Hz.

          speech_rate: Relative speech speed. Negative is slower, positive is faster; 0 is normal.

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
        model: Literal["eleven_text_to_sound_v2"],
        prompt_text: str,
        duration: float | Omit = omit,
        loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        """
        This endpoint will start a new task to generate sound effects from a text
        description.

        Args:
          prompt_text: A text description of the sound effect to generate.

          duration: The duration of the sound effect in seconds, between 0.5 and 30 seconds. If not
              provided, the duration will be determined automatically based on the text
              description.

          loop: Whether the output sound effect should be designed to loop seamlessly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text"])
    def create(
        self,
        *,
        model: Literal["seed_audio"] | Literal["eleven_text_to_sound_v2"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        reference_audios: SequenceNotStr[str] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        duration: float | Omit = omit,
        loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        return self._post(
            "/v1/sound_effect",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "loudness_rate": loudness_rate,
                    "output_format": output_format,
                    "pitch_rate": pitch_rate,
                    "reference_audios": reference_audios,
                    "sample_rate": sample_rate,
                    "speech_rate": speech_rate,
                    "duration": duration,
                    "loop": loop,
                },
                sound_effect_create_params.SoundEffectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SoundEffectCreateResponse,
        )


class AsyncSoundEffectResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncSoundEffectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSoundEffectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSoundEffectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncSoundEffectResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: Literal["seed_audio"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        reference_audios: SequenceNotStr[str] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        """
        This endpoint will start a new task to generate sound effects from a text
        description.

        Args:
          prompt_text: A non-empty text prompt. For text-to-speech, the words to speak. For
              text-to-audio, a scene description that can include voice direction, dialogue,
              music, and sound effects.

          loudness_rate: Relative output loudness. Negative is quieter, positive is louder; 0 is normal.

          output_format: Output audio container/format.

          pitch_rate: Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.

          reference_audios: Up to three reference audio clips. When provided, reference them in promptText
              as @Audio1, @Audio2, and @Audio3 in order.

          sample_rate: Output sample rate in Hz.

          speech_rate: Relative speech speed. Negative is slower, positive is faster; 0 is normal.

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
        model: Literal["eleven_text_to_sound_v2"],
        prompt_text: str,
        duration: float | Omit = omit,
        loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        """
        This endpoint will start a new task to generate sound effects from a text
        description.

        Args:
          prompt_text: A text description of the sound effect to generate.

          duration: The duration of the sound effect in seconds, between 0.5 and 30 seconds. If not
              provided, the duration will be determined automatically based on the text
              description.

          loop: Whether the output sound effect should be designed to loop seamlessly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text"])
    async def create(
        self,
        *,
        model: Literal["seed_audio"] | Literal["eleven_text_to_sound_v2"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        reference_audios: SequenceNotStr[str] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        duration: float | Omit = omit,
        loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SoundEffectCreateResponse:
        return await self._post(
            "/v1/sound_effect",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "loudness_rate": loudness_rate,
                    "output_format": output_format,
                    "pitch_rate": pitch_rate,
                    "reference_audios": reference_audios,
                    "sample_rate": sample_rate,
                    "speech_rate": speech_rate,
                    "duration": duration,
                    "loop": loop,
                },
                sound_effect_create_params.SoundEffectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SoundEffectCreateResponse,
        )


class SoundEffectResourceWithRawResponse:
    def __init__(self, sound_effect: SoundEffectResource) -> None:
        self._sound_effect = sound_effect

        self.create = to_raw_response_wrapper(
            sound_effect.create,
        )


class AsyncSoundEffectResourceWithRawResponse:
    def __init__(self, sound_effect: AsyncSoundEffectResource) -> None:
        self._sound_effect = sound_effect

        self.create = async_to_raw_response_wrapper(
            sound_effect.create,
        )


class SoundEffectResourceWithStreamingResponse:
    def __init__(self, sound_effect: SoundEffectResource) -> None:
        self._sound_effect = sound_effect

        self.create = to_streamed_response_wrapper(
            sound_effect.create,
        )


class AsyncSoundEffectResourceWithStreamingResponse:
    def __init__(self, sound_effect: AsyncSoundEffectResource) -> None:
        self._sound_effect = sound_effect

        self.create = async_to_streamed_response_wrapper(
            sound_effect.create,
        )
