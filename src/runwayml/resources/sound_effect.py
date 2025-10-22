# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import sound_effect_create_params
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
from ..types.sound_effect_create_response import SoundEffectCreateResponse

__all__ = ["SoundEffectResource", "AsyncSoundEffectResource"]


class SoundEffectResource(SyncAPIResource):
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
    ) -> NewTaskCreatedResponse:
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
        return self._post(
            "/v1/sound_effect",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "duration": duration,
                    "loop": loop,
                },
                sound_effect_create_params.SoundEffectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(SoundEffectCreateResponse, self._client),
        )


class AsyncSoundEffectResource(AsyncAPIResource):
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
    ) -> AsyncNewTaskCreatedResponse:
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
        return await self._post(
            "/v1/sound_effect",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "duration": duration,
                    "loop": loop,
                },
                sound_effect_create_params.SoundEffectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(SoundEffectCreateResponse, self._client),
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
