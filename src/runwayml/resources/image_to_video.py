# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import image_to_video_create_params
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

    @overload
    def create(
        self,
        *,
        model: Literal["gen4_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672"],
        content_moderation: image_to_video_create_params.Gen4TurboContentModeration | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: A HTTPS URL.

          ratio: The resolution of the output video.

          content_moderation: Settings that affect the behavior of the content moderation system.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

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
        model: Literal["gen3a_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen3aTurboPromptImagePromptImage]],
        prompt_text: str,
        content_moderation: image_to_video_create_params.Gen3aTurboContentModeration | Omit = omit,
        duration: Literal[5, 10] | Omit = omit,
        ratio: Literal["768:1280", "1280:768"] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: A HTTPS URL.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          content_moderation: Settings that affect the behavior of the content moderation system.

          duration: The duration of the output video in seconds.

          ratio: The resolution of the output video.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

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
        model: Literal["veo3.1"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3_1PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        duration: Literal[4, 6, 8] | Omit = omit,
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: You may specify an image to use as the first frame of the output video, or an
              array with a first frame and optionally a last frame. This model does not
              support generating with only a last frame.

          ratio: The resolution of the output video.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

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
        model: Literal["veo3.1_fast"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3_1FastPromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        duration: Literal[4, 6, 8] | Omit = omit,
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: You may specify an image to use as the first frame of the output video, or an
              array with a first frame and optionally a last frame. This model does not
              support generating with only a last frame.

          ratio: The resolution of the output video.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

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
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          duration: The number of seconds of duration for the output video.

          prompt_image: A HTTPS URL.

          ratio: The resolution of the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "prompt_image", "ratio"],
        ["model", "prompt_image", "prompt_text"],
        ["duration", "model", "prompt_image", "ratio"],
    )
    def create(
        self,
        *,
        model: Literal["gen4_turbo"]
        | Literal["gen3a_turbo"]
        | Literal["veo3.1"]
        | Literal["veo3.1_fast"]
        | Literal["veo3"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Gen3aTurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3_1PromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3_1FastPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672"]
        | Literal["768:1280", "1280:768"]
        | Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]
        | Omit = omit,
        content_moderation: image_to_video_create_params.Gen4TurboContentModeration
        | image_to_video_create_params.Gen3aTurboContentModeration
        | Omit = omit,
        duration: int | Literal[5, 10] | Literal[4, 6, 8] | Literal[8] | Omit = omit,
        prompt_text: str | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/image_to_video",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_image": prompt_image,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "duration": duration,
                    "prompt_text": prompt_text,
                    "seed": seed,
                },
                image_to_video_create_params.ImageToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(ImageToVideoCreateResponse, self._client),
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

    @overload
    async def create(
        self,
        *,
        model: Literal["gen4_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672"],
        content_moderation: image_to_video_create_params.Gen4TurboContentModeration | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: A HTTPS URL.

          ratio: The resolution of the output video.

          content_moderation: Settings that affect the behavior of the content moderation system.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

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
        model: Literal["gen3a_turbo"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen3aTurboPromptImagePromptImage]],
        prompt_text: str,
        content_moderation: image_to_video_create_params.Gen3aTurboContentModeration | Omit = omit,
        duration: Literal[5, 10] | Omit = omit,
        ratio: Literal["768:1280", "1280:768"] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: A HTTPS URL.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          content_moderation: Settings that affect the behavior of the content moderation system.

          duration: The duration of the output video in seconds.

          ratio: The resolution of the output video.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

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
        model: Literal["veo3.1"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3_1PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        duration: Literal[4, 6, 8] | Omit = omit,
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: You may specify an image to use as the first frame of the output video, or an
              array with a first frame and optionally a last frame. This model does not
              support generating with only a last frame.

          ratio: The resolution of the output video.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

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
        model: Literal["veo3.1_fast"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3_1FastPromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        duration: Literal[4, 6, 8] | Omit = omit,
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          prompt_image: You may specify an image to use as the first frame of the output video, or an
              array with a first frame and optionally a last frame. This model does not
              support generating with only a last frame.

          ratio: The resolution of the output video.

          duration: The number of seconds of duration for the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

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
        duration: Literal[8],
        model: Literal["veo3"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Veo3PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1080:1920", "1920:1080"],
        prompt_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from an image.

        Args:
          duration: The number of seconds of duration for the output video.

          prompt_image: A HTTPS URL.

          ratio: The resolution of the output video.

          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "prompt_image", "ratio"],
        ["model", "prompt_image", "prompt_text"],
        ["duration", "model", "prompt_image", "ratio"],
    )
    async def create(
        self,
        *,
        model: Literal["gen4_turbo"]
        | Literal["gen3a_turbo"]
        | Literal["veo3.1"]
        | Literal["veo3.1_fast"]
        | Literal["veo3"],
        prompt_image: Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Gen4TurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Gen3aTurboPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3_1PromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3_1FastPromptImagePromptImage]]
        | Union[str, Iterable[image_to_video_create_params.Veo3PromptImagePromptImage]],
        ratio: Literal["1280:720", "720:1280", "1104:832", "832:1104", "960:960", "1584:672"]
        | Literal["768:1280", "1280:768"]
        | Literal["1280:720", "720:1280", "1080:1920", "1920:1080"]
        | Omit = omit,
        content_moderation: image_to_video_create_params.Gen4TurboContentModeration
        | image_to_video_create_params.Gen3aTurboContentModeration
        | Omit = omit,
        duration: int | Literal[5, 10] | Literal[4, 6, 8] | Literal[8] | Omit = omit,
        prompt_text: str | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/image_to_video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_image": prompt_image,
                    "ratio": ratio,
                    "content_moderation": content_moderation,
                    "duration": duration,
                    "prompt_text": prompt_text,
                    "seed": seed,
                },
                image_to_video_create_params.ImageToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(ImageToVideoCreateResponse, self._client),
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
