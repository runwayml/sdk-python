# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import character_performance_create_params
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
from ..types.character_performance_create_response import CharacterPerformanceCreateResponse

__all__ = ["CharacterPerformanceResource", "AsyncCharacterPerformanceResource"]


class CharacterPerformanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CharacterPerformanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return CharacterPerformanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CharacterPerformanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return CharacterPerformanceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        character: character_performance_create_params.Character,
        model: Literal["act_two"],
        ratio: Literal["1280:720", "720:1280", "960:960", "1104:832", "832:1104", "1584:672"],
        reference: character_performance_create_params.Reference,
        body_control: bool | NotGiven = NOT_GIVEN,
        content_moderation: character_performance_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        expression_intensity: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to control a character's facial expressions
        and body movements using a reference video.

        Args:
          character: The character to control. You can either provide a video or an image. A visually
              recognizable face must be visible and stay within the frame.

          model: The model variant to use.

          ratio: The resolution of the output video.

          body_control: A boolean indicating whether to enable body control. When enabled, non-facial
              movements and gestures will be applied to the character in addition to facial
              expressions.

          content_moderation: Settings that affect the behavior of the content moderation system.

          expression_intensity: An integer between 1 and 5 (inclusive). A larger value increases the intensity
              of the character's expression.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/character_performance",
            body=maybe_transform(
                {
                    "character": character,
                    "model": model,
                    "ratio": ratio,
                    "reference": reference,
                    "body_control": body_control,
                    "content_moderation": content_moderation,
                    "expression_intensity": expression_intensity,
                    "seed": seed,
                },
                character_performance_create_params.CharacterPerformanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(CharacterPerformanceCreateResponse, self._client),
        )


class AsyncCharacterPerformanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCharacterPerformanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCharacterPerformanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCharacterPerformanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncCharacterPerformanceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        character: character_performance_create_params.Character,
        model: Literal["act_two"],
        ratio: Literal["1280:720", "720:1280", "960:960", "1104:832", "832:1104", "1584:672"],
        reference: character_performance_create_params.Reference,
        body_control: bool | NotGiven = NOT_GIVEN,
        content_moderation: character_performance_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        expression_intensity: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to control a character's facial expressions
        and body movements using a reference video.

        Args:
          character: The character to control. You can either provide a video or an image. A visually
              recognizable face must be visible and stay within the frame.

          model: The model variant to use.

          ratio: The resolution of the output video.

          body_control: A boolean indicating whether to enable body control. When enabled, non-facial
              movements and gestures will be applied to the character in addition to facial
              expressions.

          content_moderation: Settings that affect the behavior of the content moderation system.

          expression_intensity: An integer between 1 and 5 (inclusive). A larger value increases the intensity
              of the character's expression.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/character_performance",
            body=await async_maybe_transform(
                {
                    "character": character,
                    "model": model,
                    "ratio": ratio,
                    "reference": reference,
                    "body_control": body_control,
                    "content_moderation": content_moderation,
                    "expression_intensity": expression_intensity,
                    "seed": seed,
                },
                character_performance_create_params.CharacterPerformanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(CharacterPerformanceCreateResponse, self._client),
        )


class CharacterPerformanceResourceWithRawResponse:
    def __init__(self, character_performance: CharacterPerformanceResource) -> None:
        self._character_performance = character_performance

        self.create = to_raw_response_wrapper(
            character_performance.create,
        )


class AsyncCharacterPerformanceResourceWithRawResponse:
    def __init__(self, character_performance: AsyncCharacterPerformanceResource) -> None:
        self._character_performance = character_performance

        self.create = async_to_raw_response_wrapper(
            character_performance.create,
        )


class CharacterPerformanceResourceWithStreamingResponse:
    def __init__(self, character_performance: CharacterPerformanceResource) -> None:
        self._character_performance = character_performance

        self.create = to_streamed_response_wrapper(
            character_performance.create,
        )


class AsyncCharacterPerformanceResourceWithStreamingResponse:
    def __init__(self, character_performance: AsyncCharacterPerformanceResource) -> None:
        self._character_performance = character_performance

        self.create = async_to_streamed_response_wrapper(
            character_performance.create,
        )
