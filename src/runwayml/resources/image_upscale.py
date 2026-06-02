# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import image_upscale_create_params
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
from .._base_client import make_request_options
from ..types.image_upscale_create_response import ImageUpscaleCreateResponse

__all__ = ["ImageUpscaleResource", "AsyncImageUpscaleResource"]


class ImageUpscaleResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> ImageUpscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImageUpscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageUpscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return ImageUpscaleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image_uri: str,
        model: Literal["magnific_precision_upscaler_v2"],
        flavor: Literal["sublime", "photo", "photo_denoiser"] | Omit = omit,
        scale_factor: Literal[2, 4, 8, 16] | Omit = omit,
        sharpen: int | Omit = omit,
        smart_grain: int | Omit = omit,
        ultra_detail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUpscaleCreateResponse:
        """Upscale an image with Magnific precision upscaling.

        Each input dimension must be
        between 300px and 8000px. Output width and height are the input dimensions
        multiplied by `scaleFactor` (default 2). Output width times height cannot exceed
        25,300,000 pixels (~25.3 million).

        Args:
          image_uri: A HTTPS URL.

          flavor: Optimization preset: `sublime` (illustration), `photo` (photographic), or
              `photo_denoiser` (noisy photos).

          scale_factor: Multiplies each input dimension to produce output width and height. Defaults
              to 2.

          sharpen: Sharpness intensity from 0 (none) to 100.

          smart_grain: Grain and texture enhancement from 0 to 100.

          ultra_detail: Fine detail enhancement from 0 to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/image_upscale",
            body=maybe_transform(
                {
                    "image_uri": image_uri,
                    "model": model,
                    "flavor": flavor,
                    "scale_factor": scale_factor,
                    "sharpen": sharpen,
                    "smart_grain": smart_grain,
                    "ultra_detail": ultra_detail,
                },
                image_upscale_create_params.ImageUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpscaleCreateResponse,
        )


class AsyncImageUpscaleResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncImageUpscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImageUpscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageUpscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncImageUpscaleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image_uri: str,
        model: Literal["magnific_precision_upscaler_v2"],
        flavor: Literal["sublime", "photo", "photo_denoiser"] | Omit = omit,
        scale_factor: Literal[2, 4, 8, 16] | Omit = omit,
        sharpen: int | Omit = omit,
        smart_grain: int | Omit = omit,
        ultra_detail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUpscaleCreateResponse:
        """Upscale an image with Magnific precision upscaling.

        Each input dimension must be
        between 300px and 8000px. Output width and height are the input dimensions
        multiplied by `scaleFactor` (default 2). Output width times height cannot exceed
        25,300,000 pixels (~25.3 million).

        Args:
          image_uri: A HTTPS URL.

          flavor: Optimization preset: `sublime` (illustration), `photo` (photographic), or
              `photo_denoiser` (noisy photos).

          scale_factor: Multiplies each input dimension to produce output width and height. Defaults
              to 2.

          sharpen: Sharpness intensity from 0 (none) to 100.

          smart_grain: Grain and texture enhancement from 0 to 100.

          ultra_detail: Fine detail enhancement from 0 to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/image_upscale",
            body=await async_maybe_transform(
                {
                    "image_uri": image_uri,
                    "model": model,
                    "flavor": flavor,
                    "scale_factor": scale_factor,
                    "sharpen": sharpen,
                    "smart_grain": smart_grain,
                    "ultra_detail": ultra_detail,
                },
                image_upscale_create_params.ImageUpscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpscaleCreateResponse,
        )


class ImageUpscaleResourceWithRawResponse:
    def __init__(self, image_upscale: ImageUpscaleResource) -> None:
        self._image_upscale = image_upscale

        self.create = to_raw_response_wrapper(
            image_upscale.create,
        )


class AsyncImageUpscaleResourceWithRawResponse:
    def __init__(self, image_upscale: AsyncImageUpscaleResource) -> None:
        self._image_upscale = image_upscale

        self.create = async_to_raw_response_wrapper(
            image_upscale.create,
        )


class ImageUpscaleResourceWithStreamingResponse:
    def __init__(self, image_upscale: ImageUpscaleResource) -> None:
        self._image_upscale = image_upscale

        self.create = to_streamed_response_wrapper(
            image_upscale.create,
        )


class AsyncImageUpscaleResourceWithStreamingResponse:
    def __init__(self, image_upscale: AsyncImageUpscaleResource) -> None:
        self._image_upscale = image_upscale

        self.create = async_to_streamed_response_wrapper(
            image_upscale.create,
        )
