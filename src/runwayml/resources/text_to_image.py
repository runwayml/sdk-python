# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import text_to_image_create_params
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
from ..types.text_to_image_create_response import TextToImageCreateResponse

__all__ = ["TextToImageResource", "AsyncTextToImageResource"]


class TextToImageResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

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

    @overload
    def create(
        self,
        *,
        model: Literal["gen4_image_turbo"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage],
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of one to three images to be used as references for the generated image
              output.

          content_moderation: Settings that affect the behavior of the content moderation system.

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
        model: Literal["gen4_image"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        content_moderation: text_to_image_create_params.Gen4ImageContentModeration | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Gen4ImageReferenceImage] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          content_moderation: Settings that affect the behavior of the content moderation system.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

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
        model: Literal["gpt_image_2"],
        prompt_text: str,
        ratio: Literal[
            "2048:880",
            "1920:1088",
            "1920:1280",
            "1920:1440",
            "1920:1536",
            "1920:1920",
            "1536:1920",
            "1440:1920",
            "1280:1920",
            "1088:1920",
            "2912:1248",
            "2560:1440",
            "2560:1712",
            "2560:1920",
            "2560:2048",
            "2560:2560",
            "2048:2560",
            "1920:2560",
            "1712:2560",
            "1440:2560",
            "3840:1648",
            "3840:2160",
            "3504:2336",
            "3264:2448",
            "3200:2560",
            "2880:2880",
            "2560:3200",
            "2448:3264",
            "2336:3504",
            "2160:3840",
            "auto",
        ],
        background: Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2ReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 32,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick.
              `transparent` is not supported by this model.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output.

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
        model: Literal["gemini_image3_pro"],
        prompt_text: str,
        ratio: Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 5,500 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five of those images can pass `subject: "human"` to maintain
              character consistency, and up to nine of those images can pass
              `subject: "object"` with high-fidelity images of objects to include in the
              output.

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
        model: Literal["gemini_image3.1_flash"],
        prompt_text: str,
        ratio: Literal[
            "512:512",
            "416:624",
            "624:416",
            "432:592",
            "592:432",
            "448:576",
            "576:448",
            "384:672",
            "672:384",
            "768:336",
            "256:1024",
            "1024:256",
            "176:1408",
            "1408:176",
            "1024:1024",
            "832:1248",
            "1248:832",
            "864:1184",
            "1184:864",
            "896:1152",
            "1152:896",
            "768:1344",
            "1344:768",
            "1536:672",
            "512:2048",
            "2048:512",
            "352:2816",
            "2816:352",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "1024:4096",
            "4096:1024",
            "704:5632",
            "5632:704",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
            "2048:8192",
            "8192:2048",
            "1408:11264",
            "11264:1408",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToImageCreateResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five of those images can pass `subject: "human"` to maintain
              character consistency, and up to nine of those images can pass
              `subject: "object"` with high-fidelity images of objects to include in the
              output.

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
        model: Literal["gemini_2.5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
        ],
        reference_images: Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text", "ratio", "reference_images"], ["model", "prompt_text", "ratio"])
    def create(
        self,
        *,
        model: Literal["gen4_image_turbo"]
        | Literal["gen4_image"]
        | Literal["gpt_image_2"]
        | Literal["gemini_image3_pro"]
        | Literal["gemini_image3.1_flash"]
        | Literal["gemini_2.5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ]
        | Literal[
            "2048:880",
            "1920:1088",
            "1920:1280",
            "1920:1440",
            "1920:1536",
            "1920:1920",
            "1536:1920",
            "1440:1920",
            "1280:1920",
            "1088:1920",
            "2912:1248",
            "2560:1440",
            "2560:1712",
            "2560:1920",
            "2560:2048",
            "2560:2560",
            "2048:2560",
            "1920:2560",
            "1712:2560",
            "1440:2560",
            "3840:1648",
            "3840:2160",
            "3504:2336",
            "3264:2448",
            "3200:2560",
            "2880:2880",
            "2560:3200",
            "2448:3264",
            "2336:3504",
            "2160:3840",
            "auto",
        ]
        | Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
        ]
        | Literal[
            "512:512",
            "416:624",
            "624:416",
            "432:592",
            "592:432",
            "448:576",
            "576:448",
            "384:672",
            "672:384",
            "768:336",
            "256:1024",
            "1024:256",
            "176:1408",
            "1408:176",
            "1024:1024",
            "832:1248",
            "1248:832",
            "864:1184",
            "1184:864",
            "896:1152",
            "1152:896",
            "768:1344",
            "1344:768",
            "1536:672",
            "512:2048",
            "2048:512",
            "352:2816",
            "2816:352",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "1024:4096",
            "4096:1024",
            "704:5632",
            "5632:704",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
            "2048:8192",
            "8192:2048",
            "1408:11264",
            "11264:1408",
        ]
        | Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
        ],
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage]
        | Iterable[text_to_image_create_params.Gen4ImageReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage]
        | Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage]
        | Omit = omit,
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration
        | text_to_image_create_params.Gen4ImageContentModeration
        | Omit = omit,
        seed: int | Omit = omit,
        background: Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Literal[1, 4] | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/text_to_image",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "reference_images": reference_images,
                    "content_moderation": content_moderation,
                    "seed": seed,
                    "background": background,
                    "output_count": output_count,
                    "quality": quality,
                },
                text_to_image_create_params.TextToImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(TextToImageCreateResponse, self._client),
        )


class AsyncTextToImageResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

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

    @overload
    async def create(
        self,
        *,
        model: Literal["gen4_image_turbo"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage],
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of one to three images to be used as references for the generated image
              output.

          content_moderation: Settings that affect the behavior of the content moderation system.

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
        model: Literal["gen4_image"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ],
        content_moderation: text_to_image_create_params.Gen4ImageContentModeration | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Gen4ImageReferenceImage] | Omit = omit,
        seed: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          content_moderation: Settings that affect the behavior of the content moderation system.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

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
        model: Literal["gpt_image_2"],
        prompt_text: str,
        ratio: Literal[
            "2048:880",
            "1920:1088",
            "1920:1280",
            "1920:1440",
            "1920:1536",
            "1920:1920",
            "1536:1920",
            "1440:1920",
            "1280:1920",
            "1088:1920",
            "2912:1248",
            "2560:1440",
            "2560:1712",
            "2560:1920",
            "2560:2048",
            "2560:2560",
            "2048:2560",
            "1920:2560",
            "1712:2560",
            "1440:2560",
            "3840:1648",
            "3840:2160",
            "3504:2336",
            "3264:2448",
            "3200:2560",
            "2880:2880",
            "2560:3200",
            "2448:3264",
            "2336:3504",
            "2160:3840",
            "auto",
        ],
        background: Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2ReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 32,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick.
              `transparent` is not supported by this model.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output.

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
        model: Literal["gemini_image3_pro"],
        prompt_text: str,
        ratio: Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 5,500 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five of those images can pass `subject: "human"` to maintain
              character consistency, and up to nine of those images can pass
              `subject: "object"` with high-fidelity images of objects to include in the
              output.

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
        model: Literal["gemini_image3.1_flash"],
        prompt_text: str,
        ratio: Literal[
            "512:512",
            "416:624",
            "624:416",
            "432:592",
            "592:432",
            "448:576",
            "576:448",
            "384:672",
            "672:384",
            "768:336",
            "256:1024",
            "1024:256",
            "176:1408",
            "1408:176",
            "1024:1024",
            "832:1248",
            "1248:832",
            "864:1184",
            "1184:864",
            "896:1152",
            "1152:896",
            "768:1344",
            "1344:768",
            "1536:672",
            "512:2048",
            "2048:512",
            "352:2816",
            "2816:352",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "1024:4096",
            "4096:1024",
            "704:5632",
            "5632:704",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
            "2048:8192",
            "8192:2048",
            "1408:11264",
            "11264:1408",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToImageCreateResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five of those images can pass `subject: "human"` to maintain
              character consistency, and up to nine of those images can pass
              `subject: "object"` with high-fidelity images of objects to include in the
              output.

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
        model: Literal["gemini_2.5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
        ],
        reference_images: Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: A non-empty string up to 1000 characters (measured in UTF-16 code units). This
              should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt_text", "ratio", "reference_images"], ["model", "prompt_text", "ratio"])
    async def create(
        self,
        *,
        model: Literal["gen4_image_turbo"]
        | Literal["gen4_image"]
        | Literal["gpt_image_2"]
        | Literal["gemini_image3_pro"]
        | Literal["gemini_image3.1_flash"]
        | Literal["gemini_2.5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1080:1080",
            "1168:880",
            "1360:768",
            "1440:1080",
            "1080:1440",
            "1808:768",
            "1920:1080",
            "1080:1920",
            "2112:912",
            "1280:720",
            "720:1280",
            "720:720",
            "960:720",
            "720:960",
            "1680:720",
        ]
        | Literal[
            "2048:880",
            "1920:1088",
            "1920:1280",
            "1920:1440",
            "1920:1536",
            "1920:1920",
            "1536:1920",
            "1440:1920",
            "1280:1920",
            "1088:1920",
            "2912:1248",
            "2560:1440",
            "2560:1712",
            "2560:1920",
            "2560:2048",
            "2560:2560",
            "2048:2560",
            "1920:2560",
            "1712:2560",
            "1440:2560",
            "3840:1648",
            "3840:2160",
            "3504:2336",
            "3264:2448",
            "3200:2560",
            "2880:2880",
            "2560:3200",
            "2448:3264",
            "2336:3504",
            "2160:3840",
            "auto",
        ]
        | Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
        ]
        | Literal[
            "512:512",
            "416:624",
            "624:416",
            "432:592",
            "592:432",
            "448:576",
            "576:448",
            "384:672",
            "672:384",
            "768:336",
            "256:1024",
            "1024:256",
            "176:1408",
            "1408:176",
            "1024:1024",
            "832:1248",
            "1248:832",
            "864:1184",
            "1184:864",
            "896:1152",
            "1152:896",
            "768:1344",
            "1344:768",
            "1536:672",
            "512:2048",
            "2048:512",
            "352:2816",
            "2816:352",
            "2048:2048",
            "1696:2528",
            "2528:1696",
            "1792:2400",
            "2400:1792",
            "1856:2304",
            "2304:1856",
            "1536:2752",
            "2752:1536",
            "3168:1344",
            "1024:4096",
            "4096:1024",
            "704:5632",
            "5632:704",
            "4096:4096",
            "3392:5056",
            "5056:3392",
            "3584:4800",
            "4800:3584",
            "3712:4608",
            "4608:3712",
            "3072:5504",
            "5504:3072",
            "6336:2688",
            "2048:8192",
            "8192:2048",
            "1408:11264",
            "11264:1408",
        ]
        | Literal[
            "1344:768",
            "768:1344",
            "1024:1024",
            "1184:864",
            "864:1184",
            "1536:672",
            "832:1248",
            "1248:832",
            "896:1152",
            "1152:896",
        ],
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage]
        | Iterable[text_to_image_create_params.Gen4ImageReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage]
        | Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage]
        | Omit = omit,
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration
        | text_to_image_create_params.Gen4ImageContentModeration
        | Omit = omit,
        seed: int | Omit = omit,
        background: Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Literal[1, 4] | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/text_to_image",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt_text": prompt_text,
                    "ratio": ratio,
                    "reference_images": reference_images,
                    "content_moderation": content_moderation,
                    "seed": seed,
                    "background": background,
                    "output_count": output_count,
                    "quality": quality,
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
