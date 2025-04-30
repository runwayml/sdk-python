# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import image_to_video_create_params
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
from .._base_client import make_request_options
from ..types.image_to_video_create_response import ImageToVideoCreateResponse

__all__ = ["ImageToVideoResource", "AsyncImageToVideoResource"]


class ImageToVideoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImageToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return ImageToVideoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["gen4_turbo", "gen3a_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672", "1280:768", "768:1280"],
        duration: Literal[5, 10] | NotGiven = NOT_GIVEN,
        prompt_text: str | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageToVideoCreateResponse:
        """
        This endpoint will start a new task to generate a video from an image prompt.

        Args:
          model: The model variant to use.

          prompt_image: A HTTPS URL or data URI containing an encoded image to be used as the first
              frame of the generated video. See [our docs](/assets/inputs#images) on image
              inputs for more information.

          ratio: The resolution of the output video.

              `gen4_turbo` supports the following values:

              - `1280:720`
              - `720:1280`
              - `1104:832`
              - `832:1104`
              - `960:960`
              - `1584:672`

              `gen3a_turbo` supports the following values:

              - `1280:768`
              - `768:1280`

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 UTF-16 code points in length (that is,
              `promptText.length === 1000` in JavaScript). This should describe in detail what
              should appear in the output.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/image_to_video",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_image": prompt_image,
                    "ratio": ratio,
                    "duration": duration,
                    "prompt_text": prompt_text,
                    "seed": seed,
                },
                image_to_video_create_params.ImageToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageToVideoCreateResponse,
        )


class AsyncImageToVideoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImageToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncImageToVideoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["gen4_turbo", "gen3a_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672", "1280:768", "768:1280"],
        duration: Literal[5, 10] | NotGiven = NOT_GIVEN,
        prompt_text: str | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageToVideoCreateResponse:
        """
        This endpoint will start a new task to generate a video from an image prompt.

        Args:
          model: The model variant to use.

          prompt_image: A HTTPS URL or data URI containing an encoded image to be used as the first
              frame of the generated video. See [our docs](/assets/inputs#images) on image
              inputs for more information.

          ratio: The resolution of the output video.

              `gen4_turbo` supports the following values:

              - `1280:720`
              - `720:1280`
              - `1104:832`
              - `832:1104`
              - `960:960`
              - `1584:672`

              `gen3a_turbo` supports the following values:

              - `1280:768`
              - `768:1280`

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 UTF-16 code points in length (that is,
              `promptText.length === 1000` in JavaScript). This should describe in detail what
              should appear in the output.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/image_to_video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_image": prompt_image,
                    "ratio": ratio,
                    "duration": duration,
                    "prompt_text": prompt_text,
                    "seed": seed,
                },
                image_to_video_create_params.ImageToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageToVideoCreateResponse,
        )


class ImageToVideoResourceWithRawResponse:
    def __init__(self, image_to_video: ImageToVideoResource) -> None:
        self._image_to_video = image_to_video

        self.create = to_raw_response_wrapper(
            image_to_video.create,
        )


class AsyncImageToVideoResourceWithRawResponse:
    def __init__(self, image_to_video: AsyncImageToVideoResource) -> None:
        self._image_to_video = image_to_video

        self.create = async_to_raw_response_wrapper(
            image_to_video.create,
        )


class ImageToVideoResourceWithStreamingResponse:
    def __init__(self, image_to_video: ImageToVideoResource) -> None:
        self._image_to_video = image_to_video

        self.create = to_streamed_response_wrapper(
            image_to_video.create,
        )


class AsyncImageToVideoResourceWithStreamingResponse:
    def __init__(self, image_to_video: AsyncImageToVideoResource) -> None:
        self._image_to_video = image_to_video

        self.create = async_to_streamed_response_wrapper(
            image_to_video.create,
        )
