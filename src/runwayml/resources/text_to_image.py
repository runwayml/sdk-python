# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import text_to_image_create_params
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
from ..types.text_to_image_create_response import TextToImageCreateResponse

__all__ = ["TextToImageResource", "AsyncTextToImageResource"]


class TextToImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TextToImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TextToImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextToImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return TextToImageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["gen4_image"],
        prompt_text: str,
        ratio: Literal[
            "1920:1080",
            "1080:1920",
            "1024:1024",
            "1360:768",
            "1080:1080",
            "1168:880",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        content_moderation: text_to_image_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        reference_images: Iterable[text_to_image_create_params.ReferenceImage] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text.

        Args:
          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image(s).

          content_moderation: Settings that affect the behavior of the content moderation system.

          reference_images: An array of images to be used as references for the generated image output. Up
              to three reference images can be provided.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/text_to_image",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "reference_images": reference_images,
                    "seed": seed,
                },
                text_to_image_create_params.TextToImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(TextToImageCreateResponse, self._client),
        )


class AsyncTextToImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTextToImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextToImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextToImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncTextToImageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["gen4_image"],
        prompt_text: str,
        ratio: Literal[
            "1920:1080",
            "1080:1920",
            "1024:1024",
            "1360:768",
            "1080:1080",
            "1168:880",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        content_moderation: text_to_image_create_params.ContentModeration | NotGiven = NOT_GIVEN,
        reference_images: Iterable[text_to_image_create_params.ReferenceImage] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text.

        Args:
          model: The model variant to use.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image(s).

          content_moderation: Settings that affect the behavior of the content moderation system.

          reference_images: An array of images to be used as references for the generated image output. Up
              to three reference images can be provided.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/text_to_image",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "reference_images": reference_images,
                    "seed": seed,
                },
                text_to_image_create_params.TextToImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(TextToImageCreateResponse, self._client),
        )


class TextToImageResourceWithRawResponse:
    def __init__(self, text_to_image: TextToImageResource) -> None:
        self._text_to_image = text_to_image

        self.create = to_raw_response_wrapper(
            text_to_image.create,
        )


class AsyncTextToImageResourceWithRawResponse:
    def __init__(self, text_to_image: AsyncTextToImageResource) -> None:
        self._text_to_image = text_to_image

        self.create = async_to_raw_response_wrapper(
            text_to_image.create,
        )


class TextToImageResourceWithStreamingResponse:
    def __init__(self, text_to_image: TextToImageResource) -> None:
        self._text_to_image = text_to_image

        self.create = to_streamed_response_wrapper(
            text_to_image.create,
        )


class AsyncTextToImageResourceWithStreamingResponse:
    def __init__(self, text_to_image: AsyncTextToImageResource) -> None:
        self._text_to_image = text_to_image

        self.create = async_to_streamed_response_wrapper(
            text_to_image.create,
        )
