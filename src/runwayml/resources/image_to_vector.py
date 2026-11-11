# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..types import image_to_vector_create_params
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
    AwaitableTaskResponseMixin,
    AsyncAwaitableTaskResponseMixin,
    create_waitable_resource,
    create_async_waitable_resource,
)
from .._base_client import make_request_options
from ..types.image_to_vector_create_response import ImageToVectorCreateResponse

__all__ = [
    "ImageToVectorResource",
    "AsyncImageToVectorResource",
    "WaitableImageToVectorCreateResponse",
    "AsyncWaitableImageToVectorCreateResponse",
]


class WaitableImageToVectorCreateResponse(ImageToVectorCreateResponse, AwaitableTaskResponseMixin): ...


class AsyncWaitableImageToVectorCreateResponse(ImageToVectorCreateResponse, AsyncAwaitableTaskResponseMixin): ...


class ImageToVectorResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> ImageToVectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImageToVectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageToVectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return ImageToVectorResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image_uri: str,
        model: Literal["ideogram_vector"],
        vectorization_mode: Literal["simple", "default"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaitableImageToVectorCreateResponse:
        """
        Convert a source image into a scalable SVG.

        Args:
          image_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          vectorization_mode: Use simple for fewer shapes, or default to retain more detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/image_to_vector",
            body=maybe_transform(
                {
                    "image_uri": image_uri,
                    "model": model,
                    "vectorization_mode": vectorization_mode,
                },
                image_to_vector_create_params.ImageToVectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Type[WaitableImageToVectorCreateResponse],
                create_waitable_resource(WaitableImageToVectorCreateResponse, self._client),
            ),
        )


class AsyncImageToVectorResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncImageToVectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImageToVectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageToVectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncImageToVectorResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image_uri: str,
        model: Literal["ideogram_vector"],
        vectorization_mode: Literal["simple", "default"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncWaitableImageToVectorCreateResponse:
        """
        Convert a source image into a scalable SVG.

        Args:
          image_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          vectorization_mode: Use simple for fewer shapes, or default to retain more detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/image_to_vector",
            body=await async_maybe_transform(
                {
                    "image_uri": image_uri,
                    "model": model,
                    "vectorization_mode": vectorization_mode,
                },
                image_to_vector_create_params.ImageToVectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Type[AsyncWaitableImageToVectorCreateResponse],
                create_async_waitable_resource(AsyncWaitableImageToVectorCreateResponse, self._client),
            ),
        )


class ImageToVectorResourceWithRawResponse:
    def __init__(self, image_to_vector: ImageToVectorResource) -> None:
        self._image_to_vector = image_to_vector

        self.create = to_raw_response_wrapper(
            image_to_vector.create,
        )


class AsyncImageToVectorResourceWithRawResponse:
    def __init__(self, image_to_vector: AsyncImageToVectorResource) -> None:
        self._image_to_vector = image_to_vector

        self.create = async_to_raw_response_wrapper(
            image_to_vector.create,
        )


class ImageToVectorResourceWithStreamingResponse:
    def __init__(self, image_to_vector: ImageToVectorResource) -> None:
        self._image_to_vector = image_to_vector

        self.create = to_streamed_response_wrapper(
            image_to_vector.create,
        )


class AsyncImageToVectorResourceWithStreamingResponse:
    def __init__(self, image_to_vector: AsyncImageToVectorResource) -> None:
        self._image_to_vector = image_to_vector

        self.create = async_to_streamed_response_wrapper(
            image_to_vector.create,
        )
