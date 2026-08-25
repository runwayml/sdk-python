# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.generate import image_create_params
from ...types.generate.image_create_response import ImageCreateResponse

__all__ = ["ImageResource", "AsyncImageResource"]


class ImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return ImageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config_id: str,
        input: image_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageCreateResponse:
        """
        Start an image generation task using a saved Model Router config instead of
        naming a model.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic image generation input. The router selects a model and maps these
              options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/generate/image",
            body=maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageCreateResponse,
        )


class AsyncImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncImageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config_id: str,
        input: image_create_params.Input,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageCreateResponse:
        """
        Start an image generation task using a saved Model Router config instead of
        naming a model.

        Args:
          config_id: The slug of a saved Model Router config to route this request with.

          input: Model-agnostic image generation input. The router selects a model and maps these
              options to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/generate/image",
            body=await async_maybe_transform(
                {
                    "config_id": config_id,
                    "input": input,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageCreateResponse,
        )


class ImageResourceWithRawResponse:
    def __init__(self, image: ImageResource) -> None:
        self._image = image

        self.create = to_raw_response_wrapper(
            image.create,
        )


class AsyncImageResourceWithRawResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_raw_response_wrapper(
            image.create,
        )


class ImageResourceWithStreamingResponse:
    def __init__(self, image: ImageResource) -> None:
        self._image = image

        self.create = to_streamed_response_wrapper(
            image.create,
        )


class AsyncImageResourceWithStreamingResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_streamed_response_wrapper(
            image.create,
        )
