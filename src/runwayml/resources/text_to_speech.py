# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import text_to_speech_create_params
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
from ..types.text_to_speech_create_response import TextToSpeechCreateResponse

__all__ = ["TextToSpeechResource", "AsyncTextToSpeechResource"]


class TextToSpeechResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> TextToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TextToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return TextToSpeechResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: Literal["seed_audio"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        voice: text_to_speech_create_params.SeedAudioVoice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: A non-empty text prompt. For text-to-speech, the words to speak. For
              text-to-audio, a scene description that can include voice direction, dialogue,
              music, and sound effects.

          loudness_rate: Relative output loudness. Negative is quieter, positive is louder; 0 is normal.

          output_format: Output audio container/format.

          pitch_rate: Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.

          sample_rate: Output sample rate in Hz.

          speech_rate: Relative speech speed. Negative is slower, positive is faster; 0 is normal.

          voice: Clone from a single reference audio clip, then speak promptText in that voice.

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
        model: Literal["eleven_multilingual_v2"],
        prompt_text: str,
        voice: text_to_speech_create_params.ElevenMultilingualV2Voice,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          voice: A voice preset from the RunwayML API.

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
        model: Literal["eleven_v3"],
        prompt_text: str,
        voice: text_to_speech_create_params.ElevenV3Voice,
        apply_text_normalization: Literal["auto", "on", "off"] | Omit = omit,
        language_code: str | Omit = omit,
        seed: int | Omit = omit,
        similarity_boost: float | Omit = omit,
        speed: float | Omit = omit,
        stability: float | Omit = omit,
        style: float | Omit = omit,
        use_speaker_boost: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: The text to convert to speech. You can include expressive audio tags like
              [laughs] or [whispers] in the script.

          voice: A voice preset from the RunwayML API.

          apply_text_normalization: Text normalization mode: 'auto', 'on', or 'off' (e.g. spelling out numbers).

          language_code: ISO 639-1 language code to enforce pronunciation and normalization.

          seed: Optional seed for more deterministic output (0–4294967295). Not guaranteed.

          similarity_boost: How closely the output tracks the original speaker (0–1). Maps to ElevenLabs
              similarity_boost.

          speed: Speech speed multiplier (0.7–1.2). 1.0 is default; values below slow down and
              above speed up.

          stability: Voice stability (0–1). Lower values allow broader emotional range; higher values
              are steadier.

          style: Style exaggeration (0–1). Higher values amplify the speaker style.

          use_speaker_boost: Boost similarity to the original speaker at a small latency cost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text"], ["model", "prompt_text", "voice"])
    def create(
        self,
        *,
        model: Literal["seed_audio"] | Literal["eleven_multilingual_v2"] | Literal["eleven_v3"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        voice: text_to_speech_create_params.SeedAudioVoice
        | text_to_speech_create_params.ElevenMultilingualV2Voice
        | text_to_speech_create_params.ElevenV3Voice
        | Omit = omit,
        apply_text_normalization: Literal["auto", "on", "off"] | Omit = omit,
        language_code: str | Omit = omit,
        seed: int | Omit = omit,
        similarity_boost: float | Omit = omit,
        speed: float | Omit = omit,
        stability: float | Omit = omit,
        style: float | Omit = omit,
        use_speaker_boost: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/text_to_speech",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "loudness_rate": loudness_rate,
                    "output_format": output_format,
                    "pitch_rate": pitch_rate,
                    "sample_rate": sample_rate,
                    "speech_rate": speech_rate,
                    "voice": voice,
                    "apply_text_normalization": apply_text_normalization,
                    "language_code": language_code,
                    "seed": seed,
                    "similarity_boost": similarity_boost,
                    "speed": speed,
                    "stability": stability,
                    "style": style,
                    "use_speaker_boost": use_speaker_boost,
                },
                text_to_speech_create_params.TextToSpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(TextToSpeechCreateResponse, self._client),
        )


class AsyncTextToSpeechResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncTextToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncTextToSpeechResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: Literal["seed_audio"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        voice: text_to_speech_create_params.SeedAudioVoice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: A non-empty text prompt. For text-to-speech, the words to speak. For
              text-to-audio, a scene description that can include voice direction, dialogue,
              music, and sound effects.

          loudness_rate: Relative output loudness. Negative is quieter, positive is louder; 0 is normal.

          output_format: Output audio container/format.

          pitch_rate: Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.

          sample_rate: Output sample rate in Hz.

          speech_rate: Relative speech speed. Negative is slower, positive is faster; 0 is normal.

          voice: Clone from a single reference audio clip, then speak promptText in that voice.

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
        model: Literal["eleven_multilingual_v2"],
        prompt_text: str,
        voice: text_to_speech_create_params.ElevenMultilingualV2Voice,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          voice: A voice preset from the RunwayML API.

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
        model: Literal["eleven_v3"],
        prompt_text: str,
        voice: text_to_speech_create_params.ElevenV3Voice,
        apply_text_normalization: Literal["auto", "on", "off"] | Omit = omit,
        language_code: str | Omit = omit,
        seed: int | Omit = omit,
        similarity_boost: float | Omit = omit,
        speed: float | Omit = omit,
        stability: float | Omit = omit,
        style: float | Omit = omit,
        use_speaker_boost: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate speech from text.

        Args:
          prompt_text: The text to convert to speech. You can include expressive audio tags like
              [laughs] or [whispers] in the script.

          voice: A voice preset from the RunwayML API.

          apply_text_normalization: Text normalization mode: 'auto', 'on', or 'off' (e.g. spelling out numbers).

          language_code: ISO 639-1 language code to enforce pronunciation and normalization.

          seed: Optional seed for more deterministic output (0–4294967295). Not guaranteed.

          similarity_boost: How closely the output tracks the original speaker (0–1). Maps to ElevenLabs
              similarity_boost.

          speed: Speech speed multiplier (0.7–1.2). 1.0 is default; values below slow down and
              above speed up.

          stability: Voice stability (0–1). Lower values allow broader emotional range; higher values
              are steadier.

          style: Style exaggeration (0–1). Higher values amplify the speaker style.

          use_speaker_boost: Boost similarity to the original speaker at a small latency cost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text"], ["model", "prompt_text", "voice"])
    async def create(
        self,
        *,
        model: Literal["seed_audio"] | Literal["eleven_multilingual_v2"] | Literal["eleven_v3"],
        prompt_text: str,
        loudness_rate: int | Omit = omit,
        output_format: Literal["wav", "mp3", "ogg_opus"] | Omit = omit,
        pitch_rate: int | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000, 32000, 44100, 48000] | Omit = omit,
        speech_rate: int | Omit = omit,
        voice: text_to_speech_create_params.SeedAudioVoice
        | text_to_speech_create_params.ElevenMultilingualV2Voice
        | text_to_speech_create_params.ElevenV3Voice
        | Omit = omit,
        apply_text_normalization: Literal["auto", "on", "off"] | Omit = omit,
        language_code: str | Omit = omit,
        seed: int | Omit = omit,
        similarity_boost: float | Omit = omit,
        speed: float | Omit = omit,
        stability: float | Omit = omit,
        style: float | Omit = omit,
        use_speaker_boost: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/text_to_speech",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "loudness_rate": loudness_rate,
                    "output_format": output_format,
                    "pitch_rate": pitch_rate,
                    "sample_rate": sample_rate,
                    "speech_rate": speech_rate,
                    "voice": voice,
                    "apply_text_normalization": apply_text_normalization,
                    "language_code": language_code,
                    "seed": seed,
                    "similarity_boost": similarity_boost,
                    "speed": speed,
                    "stability": stability,
                    "style": style,
                    "use_speaker_boost": use_speaker_boost,
                },
                text_to_speech_create_params.TextToSpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(TextToSpeechCreateResponse, self._client),
        )


class TextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.create = to_raw_response_wrapper(
            text_to_speech.create,
        )


class AsyncTextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.create = async_to_raw_response_wrapper(
            text_to_speech.create,
        )


class TextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.create = to_streamed_response_wrapper(
            text_to_speech.create,
        )


class AsyncTextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.create = async_to_streamed_response_wrapper(
            text_to_speech.create,
        )
