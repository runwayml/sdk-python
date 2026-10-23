# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import text_to_image_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
        background: Literal["transparent", "opaque", "auto"] | Omit = omit,
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

          background: Background treatment. Defaults to `auto`, which lets the model pick. Use
              `transparent` to generate a PNG with an alpha-channel background.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag.

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
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: This should describe in detail what should appear in the output.

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
        model: Literal["muse_image"],
        prompt_text: str,
        ratio: Literal[
            "2352:1008",
            "2016:1152",
            "1920:1280",
            "1792:1344",
            "1600:1600",
            "1344:1792",
            "1280:1920",
            "1152:2016",
            "auto",
        ],
        output_count: int | Omit = omit,
        output_format: Literal["webp", "png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.MuseImageReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose the framing from the prompt.

          output_count: The number of images to generate. Each image costs 1 credit.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Up to 10 images to guide the generation. When provided, the model edits and
              combines them as your prompt describes instead of generating from the prompt
              alone.

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
        model: Literal["seedream5_pro"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1296:864",
            "864:1296",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2720:1530",
            "1530:2720",
            "2496:1664",
            "1664:2496",
            "auto_1k",
            "auto_2k",
        ],
        grounding: bool | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5ProReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string up to 4,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use
              `auto_1k` or `auto_2k` to let the model pick aspect ratio at a fixed resolution
              tier.

          grounding: When true, enable live web search so the model can use current brand, trend, or
              event context. Default false for deterministic output.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: An array of reference images for multi-image fusion and interactive editing.
              Reference by upload order in prompt text (Figure 1, Figure 2, etc.).

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
        model: Literal["seedream5_lite"],
        prompt_text: str,
        ratio: Union[
            Literal[
                "2048:2048",
                "2304:1728",
                "1728:2304",
                "2848:1600",
                "1600:2848",
                "2496:1664",
                "1664:2496",
                "3136:1344",
                "3072:3072",
                "3456:2592",
                "2592:3456",
                "4096:2304",
                "2304:4096",
                "3744:2496",
                "2496:3744",
                "4704:2016",
            ],
            str,
        ],
        grounding: bool | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5LiteReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string up to 4,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Also
              accepts freeform sizes whose width\\**height is between 3686400 and 16777216
              pixels.

          grounding: When true, enable live web search so the model can use current brand, trend, or
              event context. Default false for deterministic output.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: An array of reference images for multi-image fusion and interactive editing.
              Reference by upload order in prompt text (Figure 1, Figure 2, etc.).

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
        model: Literal["grok_imagine_image_2"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1248:576",
            "576:1248",
            "1280:576",
            "576:1280",
            "1408:704",
            "704:1408",
            "2048:2048",
            "2816:1584",
            "1584:2816",
            "2368:1776",
            "1776:2368",
            "2496:1664",
            "1664:2496",
            "2912:1344",
            "1344:2912",
            "3200:1440",
            "1440:3200",
            "2912:1456",
            "1456:2912",
            "auto_1k",
            "auto_2k",
        ],
        edit: bool | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GrokImagineImage2ReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. 2K ratios
              cost 2 additional credits per image. Use `auto_1k` or `auto_2k` to pick a
              resolution tier and let the model choose the framing from the prompt.

          edit: When true with exactly one reference image, edit that image directly instead of
              using it as a loose visual reference. With several reference images the prompt
              describes how they should be edited or combined. Requires at least one reference
              image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          quality: How much rendering effort the model spends on the output. Defaults to `medium`;
              `low` is faster and costs 2 fewer credits per image.

          reference_images: Up to 3 images to guide the generation. Reference them from `promptText` to
              describe how each should be used. Each adds 1 credit to the generation.

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
        model: Literal["gemini_image3.1_flash_lite"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3_1FlashLiteReferenceImage] | Omit = omit,
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
          prompt_text: This should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five can pass `subject: "human"` and up to nine can pass
              `subject: "object"`.

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
          prompt_text: This should describe in detail what should appear in the output.

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
        model: Literal["gpt_image_2_5_flare"],
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
        quality: Literal["low", "medium", "high", "xhigh", "max"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2_5FlareReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag. Each reference image adds 1 credit
              per generated image.

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
        model: Literal["gpt_image_2_5_sunburst"],
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
        background: Literal["transparent", "opaque", "auto"] | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high", "xhigh", "max"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2_5SunburstReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick. Use
              `transparent` to generate a PNG with an alpha-channel background.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag. Each reference image adds 1 credit
              per generated image.

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
        model: Literal["bria_fibo_1_5"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "2048:2048",
            "1536:2304",
            "2304:1536",
            "1536:2048",
            "2048:1536",
            "1536:1920",
            "1920:1536",
            "1152:2048",
            "2048:1152",
        ],
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.BriaFibo1_5ReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. 1MP sizes
              cost 5 credits per image and 4MP sizes 10.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Up to 1 image to guide the generation. The prompt describes how the output
              should build on it.

          seed: If unspecified, a random number is chosen. Using the same seed with an identical
              request reproduces the same image.

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
        model: Literal["bria_fibo_edit_1_5"],
        prompt_text: str,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        ratio: Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "auto",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.BriaFiboEdit1_5ReferenceImage] | Omit = omit,
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
          prompt_text: An instruction describing how to edit the reference images.

          output_format: The file format of the output image. Defaults to png.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Omit it or
              use `auto` to keep the framing of the first reference image. Choosing a size
              requires at least 2 reference images; a single image always keeps its own
              framing.

          reference_images: 1 to 4 images to edit. With several, the instruction describes how to combine
              them.

          seed: If unspecified, a random number is chosen. Using the same seed with an identical
              request reproduces the same image.

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
        model: Literal["ideogram_4_0"],
        prompt_text: str,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high"] | Omit = omit,
        ratio: Literal[
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "3072:1280",
            "1280:3072",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Ideogram4_0ReferenceImage] | Omit = omit,
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
          prompt_text: Describe the image to generate, or how to remix the reference image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          quality: How much rendering effort the model spends on each image. `low` costs 4 credits
              per image, `medium` 7 and `high` 11.

          ratio: The resolution of the output image, expressed as `<width>:<height>`.

          reference_images: An image to remix. The prompt describes how the output should differ from it.

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
        model: Literal["ideogram_4_5"],
        prompt_text: str,
        mask_uri: str | Omit = omit,
        output_count: int | Omit = omit,
        precise_edit: bool | Omit = omit,
        quality: Literal["very_low", "low", "medium", "high"] | Omit = omit,
        ratio: Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1120:896",
            "896:1120",
            "1440:720",
            "720:1440",
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "2240:1792",
            "1792:2240",
            "2880:1440",
            "1440:2880",
            "1024:576",
            "576:1024",
            "1408:704",
            "704:1408",
            "auto",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Ideogram4_5ReferenceImage] | Omit = omit,
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
          prompt_text: Describe the image to generate, or the changes to make to the reference images.

          mask_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          precise_edit: When true, edit the first reference image while preserving its composition and
              dimensions. Requires at least one reference image.

          quality: How much rendering effort the model spends on each image. Defaults to `medium`
              (8 credits per image) when generating from reference images and `high` (25
              credits) otherwise, including `preciseEdit`. `low` costs 4 credits and
              `very_low` 1; `very_low` requires reference images and is not available with
              `preciseEdit`.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Omit it or
              use `auto` to let the model choose. With reference images, widescreen 1K sizes
              are `1024:576`, `576:1024`, `1408:704`, `704:1408` instead of `1280:720`,
              `720:1280`, `1440:720`, `720:1440`. Not available with `maskUri` or
              `preciseEdit`, which keep the size of the first reference image.

          reference_images: Up to 5 images to guide the generation. With `maskUri` or `preciseEdit`, the
              first image is the one being edited and the rest are references.

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
        model: Literal["seedream5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1248:832",
            "832:1248",
            "1568:672",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2848:1600",
            "1600:2848",
            "2496:1664",
            "1664:2496",
            "3136:1344",
            "auto_1k",
            "auto_2k",
        ],
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5FlashReferenceImage] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use
              `auto_1k` or `auto_2k` to let the model pick the aspect ratio at a fixed
              resolution tier.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Images to edit or combine. Refer to them in the prompt by upload order (Figure
              1, Figure 2, and so on).

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
        model: Literal["nano_banana_2.1"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
            "512:2064",
            "2064:512",
            "352:2928",
            "2928:352",
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
            "1024:4128",
            "4128:1024",
            "704:5856",
            "5856:704",
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
            "2048:8256",
            "8256:2048",
            "1408:11712",
            "11712:1408",
        ],
        output_count: int | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.NanoBanana2_1ReferenceImage] | Omit = omit,
        thinking_level: Literal["minimal", "medium", "high"] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          reference_images: Up to 14 images to edit, combine, or use as references for the output.

          thinking_level: How much the model reasons about the prompt before generating. Defaults to
              medium.

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
        model: Literal["recraft_v4_1_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1536:768",
            "768:1536",
            "1280:832",
            "832:1280",
            "1216:896",
            "896:1216",
            "1152:896",
            "896:1152",
            "832:1344",
            "1280:896",
            "896:1280",
            "1344:768",
            "768:1344",
        ],
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["webp", "png"] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The output dimensions, expressed as `<width>:<height>`.

          background_color: A preferred background color as a six-digit hex string.

          colors: Preferred colors as six-digit hex strings.

          output_count: The number of images to generate. Each image is billed separately.

          output_format: The output file format. Defaults to webp.

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
        model: Literal["recraft_v4_1_vector"],
        prompt_text: str,
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
        ratio: Literal["1024:1024", "1216:896", "896:1216", "1344:768", "768:1344"] | Omit = omit,
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
          prompt_text: Describe the vector illustration you want to generate.

          background_color: The preferred background color as a six-digit hex value. This is a generation
              hint, not an exact color constraint; the generated background may use a
              different shade.

          colors: Preferred colors as six-digit hex values, such as #FF8800.

          ratio: The width and height declared by the output SVG. Vector artwork can be scaled
              after generation.

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
          prompt_text: This should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "prompt_text", "ratio", "reference_images"],
        ["model", "prompt_text", "ratio"],
        ["model", "prompt_text"],
    )
    def create(
        self,
        *,
        model: Literal["gen4_image_turbo"]
        | Literal["gen4_image"]
        | Literal["gpt_image_2"]
        | Literal["gemini_image3.1_flash"]
        | Literal["muse_image"]
        | Literal["seedream5_pro"]
        | Literal["seedream5_lite"]
        | Literal["grok_imagine_image_2"]
        | Literal["gemini_image3.1_flash_lite"]
        | Literal["gemini_image3_pro"]
        | Literal["gpt_image_2_5_flare"]
        | Literal["gpt_image_2_5_sunburst"]
        | Literal["bria_fibo_1_5"]
        | Literal["bria_fibo_edit_1_5"]
        | Literal["ideogram_4_0"]
        | Literal["ideogram_4_5"]
        | Literal["seedream5_flash"]
        | Literal["nano_banana_2.1"]
        | Literal["recraft_v4_1_flash"]
        | Literal["recraft_v4_1_vector"]
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
            "2352:1008",
            "2016:1152",
            "1920:1280",
            "1792:1344",
            "1600:1600",
            "1344:1792",
            "1280:1920",
            "1152:2016",
            "auto",
        ]
        | Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1296:864",
            "864:1296",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2720:1530",
            "1530:2720",
            "2496:1664",
            "1664:2496",
            "auto_1k",
            "auto_2k",
        ]
        | Union[
            Literal[
                "2048:2048",
                "2304:1728",
                "1728:2304",
                "2848:1600",
                "1600:2848",
                "2496:1664",
                "1664:2496",
                "3136:1344",
                "3072:3072",
                "3456:2592",
                "2592:3456",
                "4096:2304",
                "2304:4096",
                "3744:2496",
                "2496:3744",
                "4704:2016",
            ],
            str,
        ]
        | Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1248:576",
            "576:1248",
            "1280:576",
            "576:1280",
            "1408:704",
            "704:1408",
            "2048:2048",
            "2816:1584",
            "1584:2816",
            "2368:1776",
            "1776:2368",
            "2496:1664",
            "1664:2496",
            "2912:1344",
            "1344:2912",
            "3200:1440",
            "1440:3200",
            "2912:1456",
            "1456:2912",
            "auto_1k",
            "auto_2k",
        ]
        | Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
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
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "2048:2048",
            "1536:2304",
            "2304:1536",
            "1536:2048",
            "2048:1536",
            "1536:1920",
            "1920:1536",
            "1152:2048",
            "2048:1152",
        ]
        | Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "auto",
        ]
        | Literal[
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "3072:1280",
            "1280:3072",
        ]
        | Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1120:896",
            "896:1120",
            "1440:720",
            "720:1440",
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "2240:1792",
            "1792:2240",
            "2880:1440",
            "1440:2880",
            "1024:576",
            "576:1024",
            "1408:704",
            "704:1408",
            "auto",
        ]
        | Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1248:832",
            "832:1248",
            "1568:672",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2848:1600",
            "1600:2848",
            "2496:1664",
            "1664:2496",
            "3136:1344",
            "auto_1k",
            "auto_2k",
        ]
        | Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
            "512:2064",
            "2064:512",
            "352:2928",
            "2928:352",
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
            "1024:4128",
            "4128:1024",
            "704:5856",
            "5856:704",
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
            "2048:8256",
            "8256:2048",
            "1408:11712",
            "11712:1408",
        ]
        | Literal[
            "1024:1024",
            "1536:768",
            "768:1536",
            "1280:832",
            "832:1280",
            "1216:896",
            "896:1216",
            "1152:896",
            "896:1152",
            "832:1344",
            "1280:896",
            "896:1280",
            "1344:768",
            "768:1344",
        ]
        | Literal["1024:1024", "1216:896", "896:1216", "1344:768", "768:1344"]
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
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage]
        | Iterable[text_to_image_create_params.Gen4ImageReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage]
        | Iterable[text_to_image_create_params.MuseImageReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5ProReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5LiteReferenceImage]
        | Iterable[text_to_image_create_params.GrokImagineImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashLiteReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2_5FlareReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2_5SunburstReferenceImage]
        | Iterable[text_to_image_create_params.BriaFibo1_5ReferenceImage]
        | Iterable[text_to_image_create_params.BriaFiboEdit1_5ReferenceImage]
        | Iterable[text_to_image_create_params.Ideogram4_0ReferenceImage]
        | Iterable[text_to_image_create_params.Ideogram4_5ReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5FlashReferenceImage]
        | Iterable[text_to_image_create_params.NanoBanana2_1ReferenceImage]
        | Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage]
        | Omit = omit,
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration
        | text_to_image_create_params.Gen4ImageContentModeration
        | Omit = omit,
        seed: int | Omit = omit,
        background: Literal["transparent", "opaque", "auto"] | Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Literal[1, 4] | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"]
        | Literal["low", "medium"]
        | Literal["low", "medium", "high", "xhigh", "max"]
        | Literal["low", "medium", "high"]
        | Literal["very_low", "low", "medium", "high"]
        | Omit = omit,
        output_format: Literal["webp", "png", "jpeg"] | Literal["png", "jpeg"] | Literal["webp", "png"] | Omit = omit,
        grounding: bool | Omit = omit,
        edit: bool | Omit = omit,
        mask_uri: str | Omit = omit,
        precise_edit: bool | Omit = omit,
        thinking_level: Literal["minimal", "medium", "high"] | Omit = omit,
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
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
                    "output_format": output_format,
                    "grounding": grounding,
                    "edit": edit,
                    "mask_uri": mask_uri,
                    "precise_edit": precise_edit,
                    "thinking_level": thinking_level,
                    "background_color": background_color,
                    "colors": colors,
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
        background: Literal["transparent", "opaque", "auto"] | Omit = omit,
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

          background: Background treatment. Defaults to `auto`, which lets the model pick. Use
              `transparent` to generate a PNG with an alpha-channel background.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag.

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
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate images from text and/or image(s)

        Args:
          prompt_text: This should describe in detail what should appear in the output.

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
        model: Literal["muse_image"],
        prompt_text: str,
        ratio: Literal[
            "2352:1008",
            "2016:1152",
            "1920:1280",
            "1792:1344",
            "1600:1600",
            "1344:1792",
            "1280:1920",
            "1152:2016",
            "auto",
        ],
        output_count: int | Omit = omit,
        output_format: Literal["webp", "png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.MuseImageReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose the framing from the prompt.

          output_count: The number of images to generate. Each image costs 1 credit.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Up to 10 images to guide the generation. When provided, the model edits and
              combines them as your prompt describes instead of generating from the prompt
              alone.

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
        model: Literal["seedream5_pro"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1296:864",
            "864:1296",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2720:1530",
            "1530:2720",
            "2496:1664",
            "1664:2496",
            "auto_1k",
            "auto_2k",
        ],
        grounding: bool | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5ProReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string up to 4,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use
              `auto_1k` or `auto_2k` to let the model pick aspect ratio at a fixed resolution
              tier.

          grounding: When true, enable live web search so the model can use current brand, trend, or
              event context. Default false for deterministic output.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: An array of reference images for multi-image fusion and interactive editing.
              Reference by upload order in prompt text (Figure 1, Figure 2, etc.).

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
        model: Literal["seedream5_lite"],
        prompt_text: str,
        ratio: Union[
            Literal[
                "2048:2048",
                "2304:1728",
                "1728:2304",
                "2848:1600",
                "1600:2848",
                "2496:1664",
                "1664:2496",
                "3136:1344",
                "3072:3072",
                "3456:2592",
                "2592:3456",
                "4096:2304",
                "2304:4096",
                "3744:2496",
                "2496:3744",
                "4704:2016",
            ],
            str,
        ],
        grounding: bool | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5LiteReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string up to 4,000 characters describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Also
              accepts freeform sizes whose width\\**height is between 3686400 and 16777216
              pixels.

          grounding: When true, enable live web search so the model can use current brand, trend, or
              event context. Default false for deterministic output.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: An array of reference images for multi-image fusion and interactive editing.
              Reference by upload order in prompt text (Figure 1, Figure 2, etc.).

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
        model: Literal["grok_imagine_image_2"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1248:576",
            "576:1248",
            "1280:576",
            "576:1280",
            "1408:704",
            "704:1408",
            "2048:2048",
            "2816:1584",
            "1584:2816",
            "2368:1776",
            "1776:2368",
            "2496:1664",
            "1664:2496",
            "2912:1344",
            "1344:2912",
            "3200:1440",
            "1440:3200",
            "2912:1456",
            "1456:2912",
            "auto_1k",
            "auto_2k",
        ],
        edit: bool | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GrokImagineImage2ReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. 2K ratios
              cost 2 additional credits per image. Use `auto_1k` or `auto_2k` to pick a
              resolution tier and let the model choose the framing from the prompt.

          edit: When true with exactly one reference image, edit that image directly instead of
              using it as a loose visual reference. With several reference images the prompt
              describes how they should be edited or combined. Requires at least one reference
              image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          quality: How much rendering effort the model spends on the output. Defaults to `medium`;
              `low` is faster and costs 2 fewer credits per image.

          reference_images: Up to 3 images to guide the generation. Reference them from `promptText` to
              describe how each should be used. Each adds 1 credit to the generation.

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
        model: Literal["gemini_image3.1_flash_lite"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
        ],
        output_count: Literal[1, 4] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GeminiImage3_1FlashLiteReferenceImage] | Omit = omit,
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
          prompt_text: This should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation. Up to four images can be generated at
              once.

          reference_images: An array of up to 14 images to be used as references for the generated image
              output. Up to five can pass `subject: "human"` and up to nine can pass
              `subject: "object"`.

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
          prompt_text: This should describe in detail what should appear in the output.

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
        model: Literal["gpt_image_2_5_flare"],
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
        quality: Literal["low", "medium", "high", "xhigh", "max"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2_5FlareReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag. Each reference image adds 1 credit
              per generated image.

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
        model: Literal["gpt_image_2_5_sunburst"],
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
        background: Literal["transparent", "opaque", "auto"] | Omit = omit,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high", "xhigh", "max"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.GptImage2_5SunburstReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty string describing the desired image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use `auto`
              to let the model choose.

          background: Background treatment. Defaults to `auto`, which lets the model pick. Use
              `transparent` to generate a PNG with an alpha-channel background.

          output_count: The number of images to generate (1-10). Increasing this number will affect the
              number of credits consumed by the generation.

          quality: Rendering quality. Higher qualities consume more credits. Defaults to `high`.

          reference_images: An array of up to 16 images to be used as references for the generated image
              output. No two images may share the same tag. Each reference image adds 1 credit
              per generated image.

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
        model: Literal["bria_fibo_1_5"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "2048:2048",
            "1536:2304",
            "2304:1536",
            "1536:2048",
            "2048:1536",
            "1536:1920",
            "1920:1536",
            "1152:2048",
            "2048:1152",
        ],
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.BriaFibo1_5ReferenceImage] | Omit = omit,
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
          prompt_text: A non-empty text prompt describing what should appear in the output image.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. 1MP sizes
              cost 5 credits per image and 4MP sizes 10.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Up to 1 image to guide the generation. The prompt describes how the output
              should build on it.

          seed: If unspecified, a random number is chosen. Using the same seed with an identical
              request reproduces the same image.

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
        model: Literal["bria_fibo_edit_1_5"],
        prompt_text: str,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        ratio: Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "auto",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.BriaFiboEdit1_5ReferenceImage] | Omit = omit,
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
          prompt_text: An instruction describing how to edit the reference images.

          output_format: The file format of the output image. Defaults to png.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Omit it or
              use `auto` to keep the framing of the first reference image. Choosing a size
              requires at least 2 reference images; a single image always keeps its own
              framing.

          reference_images: 1 to 4 images to edit. With several, the instruction describes how to combine
              them.

          seed: If unspecified, a random number is chosen. Using the same seed with an identical
              request reproduces the same image.

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
        model: Literal["ideogram_4_0"],
        prompt_text: str,
        output_count: int | Omit = omit,
        quality: Literal["low", "medium", "high"] | Omit = omit,
        ratio: Literal[
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "3072:1280",
            "1280:3072",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Ideogram4_0ReferenceImage] | Omit = omit,
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
          prompt_text: Describe the image to generate, or how to remix the reference image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          quality: How much rendering effort the model spends on each image. `low` costs 4 credits
              per image, `medium` 7 and `high` 11.

          ratio: The resolution of the output image, expressed as `<width>:<height>`.

          reference_images: An image to remix. The prompt describes how the output should differ from it.

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
        model: Literal["ideogram_4_5"],
        prompt_text: str,
        mask_uri: str | Omit = omit,
        output_count: int | Omit = omit,
        precise_edit: bool | Omit = omit,
        quality: Literal["very_low", "low", "medium", "high"] | Omit = omit,
        ratio: Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1120:896",
            "896:1120",
            "1440:720",
            "720:1440",
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "2240:1792",
            "1792:2240",
            "2880:1440",
            "1440:2880",
            "1024:576",
            "576:1024",
            "1408:704",
            "704:1408",
            "auto",
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Ideogram4_5ReferenceImage] | Omit = omit,
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
          prompt_text: Describe the image to generate, or the changes to make to the reference images.

          mask_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
              [our docs](/assets/inputs#images) on image inputs for more information.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          precise_edit: When true, edit the first reference image while preserving its composition and
              dimensions. Requires at least one reference image.

          quality: How much rendering effort the model spends on each image. Defaults to `medium`
              (8 credits per image) when generating from reference images and `high` (25
              credits) otherwise, including `preciseEdit`. `low` costs 4 credits and
              `very_low` 1; `very_low` requires reference images and is not available with
              `preciseEdit`.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Omit it or
              use `auto` to let the model choose. With reference images, widescreen 1K sizes
              are `1024:576`, `576:1024`, `1408:704`, `704:1408` instead of `1280:720`,
              `720:1280`, `1440:720`, `720:1440`. Not available with `maskUri` or
              `preciseEdit`, which keep the size of the first reference image.

          reference_images: Up to 5 images to guide the generation. With `maskUri` or `preciseEdit`, the
              first image is the one being edited and the rest are references.

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
        model: Literal["seedream5_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1248:832",
            "832:1248",
            "1568:672",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2848:1600",
            "1600:2848",
            "2496:1664",
            "1664:2496",
            "3136:1344",
            "auto_1k",
            "auto_2k",
        ],
        output_count: int | Omit = omit,
        output_format: Literal["png", "jpeg"] | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Seedream5FlashReferenceImage] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The resolution of the output image, expressed as `<width>:<height>`. Use
              `auto_1k` or `auto_2k` to let the model pick the aspect ratio at a fixed
              resolution tier.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          output_format: The file format of the output image. Defaults to png.

          reference_images: Images to edit or combine. Refer to them in the prompt by upload order (Figure
              1, Figure 2, and so on).

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
        model: Literal["nano_banana_2.1"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
            "512:2064",
            "2064:512",
            "352:2928",
            "2928:352",
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
            "1024:4128",
            "4128:1024",
            "704:5856",
            "5856:704",
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
            "2048:8256",
            "8256:2048",
            "1408:11712",
            "11712:1408",
        ],
        output_count: int | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.NanoBanana2_1ReferenceImage] | Omit = omit,
        thinking_level: Literal["minimal", "medium", "high"] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The resolution of the output image.

          output_count: The number of images to generate. Increasing this number will affect the number
              of credits consumed by the generation.

          reference_images: Up to 14 images to edit, combine, or use as references for the output.

          thinking_level: How much the model reasons about the prompt before generating. Defaults to
              medium.

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
        model: Literal["recraft_v4_1_flash"],
        prompt_text: str,
        ratio: Literal[
            "1024:1024",
            "1536:768",
            "768:1536",
            "1280:832",
            "832:1280",
            "1216:896",
            "896:1216",
            "1152:896",
            "896:1152",
            "832:1344",
            "1280:896",
            "896:1280",
            "1344:768",
            "768:1344",
        ],
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
        output_count: int | Omit = omit,
        output_format: Literal["webp", "png"] | Omit = omit,
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
          prompt_text: A description of the image you want to generate.

          ratio: The output dimensions, expressed as `<width>:<height>`.

          background_color: A preferred background color as a six-digit hex string.

          colors: Preferred colors as six-digit hex strings.

          output_count: The number of images to generate. Each image is billed separately.

          output_format: The output file format. Defaults to webp.

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
        model: Literal["recraft_v4_1_vector"],
        prompt_text: str,
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
        ratio: Literal["1024:1024", "1216:896", "896:1216", "1344:768", "768:1344"] | Omit = omit,
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
          prompt_text: Describe the vector illustration you want to generate.

          background_color: The preferred background color as a six-digit hex value. This is a generation
              hint, not an exact color constraint; the generated background may use a
              different shade.

          colors: Preferred colors as six-digit hex values, such as #FF8800.

          ratio: The width and height declared by the output SVG. Vector artwork can be scaled
              after generation.

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
          prompt_text: This should describe in detail what should appear in the output.

          ratio: The resolution of the output image.

          reference_images: An array of up to three images to be used as references for the generated image
              output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "prompt_text", "ratio", "reference_images"],
        ["model", "prompt_text", "ratio"],
        ["model", "prompt_text"],
    )
    async def create(
        self,
        *,
        model: Literal["gen4_image_turbo"]
        | Literal["gen4_image"]
        | Literal["gpt_image_2"]
        | Literal["gemini_image3.1_flash"]
        | Literal["muse_image"]
        | Literal["seedream5_pro"]
        | Literal["seedream5_lite"]
        | Literal["grok_imagine_image_2"]
        | Literal["gemini_image3.1_flash_lite"]
        | Literal["gemini_image3_pro"]
        | Literal["gpt_image_2_5_flare"]
        | Literal["gpt_image_2_5_sunburst"]
        | Literal["bria_fibo_1_5"]
        | Literal["bria_fibo_edit_1_5"]
        | Literal["ideogram_4_0"]
        | Literal["ideogram_4_5"]
        | Literal["seedream5_flash"]
        | Literal["nano_banana_2.1"]
        | Literal["recraft_v4_1_flash"]
        | Literal["recraft_v4_1_vector"]
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
            "2352:1008",
            "2016:1152",
            "1920:1280",
            "1792:1344",
            "1600:1600",
            "1344:1792",
            "1280:1920",
            "1152:2016",
            "auto",
        ]
        | Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1296:864",
            "864:1296",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2720:1530",
            "1530:2720",
            "2496:1664",
            "1664:2496",
            "auto_1k",
            "auto_2k",
        ]
        | Union[
            Literal[
                "2048:2048",
                "2304:1728",
                "1728:2304",
                "2848:1600",
                "1600:2848",
                "2496:1664",
                "1664:2496",
                "3136:1344",
                "3072:3072",
                "3456:2592",
                "2592:3456",
                "4096:2304",
                "2304:4096",
                "3744:2496",
                "2496:3744",
                "4704:2016",
            ],
            str,
        ]
        | Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1248:576",
            "576:1248",
            "1280:576",
            "576:1280",
            "1408:704",
            "704:1408",
            "2048:2048",
            "2816:1584",
            "1584:2816",
            "2368:1776",
            "1776:2368",
            "2496:1664",
            "1664:2496",
            "2912:1344",
            "1344:2912",
            "3200:1440",
            "1440:3200",
            "2912:1456",
            "1456:2912",
            "auto_1k",
            "auto_2k",
        ]
        | Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
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
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "2048:2048",
            "1536:2304",
            "2304:1536",
            "1536:2048",
            "2048:1536",
            "1536:1920",
            "1920:1536",
            "1152:2048",
            "2048:1152",
        ]
        | Literal[
            "1024:1024",
            "768:1152",
            "1152:768",
            "768:1024",
            "1024:768",
            "768:960",
            "960:768",
            "576:1024",
            "1024:576",
            "auto",
        ]
        | Literal[
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "3072:1280",
            "1280:3072",
        ]
        | Literal[
            "1024:1024",
            "1280:720",
            "720:1280",
            "1152:864",
            "864:1152",
            "1248:832",
            "832:1248",
            "1120:896",
            "896:1120",
            "1440:720",
            "720:1440",
            "2048:2048",
            "2560:1440",
            "1440:2560",
            "2304:1728",
            "1728:2304",
            "2496:1664",
            "1664:2496",
            "2240:1792",
            "1792:2240",
            "2880:1440",
            "1440:2880",
            "1024:576",
            "576:1024",
            "1408:704",
            "704:1408",
            "auto",
        ]
        | Literal[
            "1024:1024",
            "1184:896",
            "896:1184",
            "1376:768",
            "768:1376",
            "1248:832",
            "832:1248",
            "1568:672",
            "2048:2048",
            "2304:1728",
            "1728:2304",
            "2848:1600",
            "1600:2848",
            "2496:1664",
            "1664:2496",
            "3136:1344",
            "auto_1k",
            "auto_2k",
        ]
        | Literal[
            "1024:1024",
            "848:1264",
            "1264:848",
            "896:1200",
            "1200:896",
            "928:1152",
            "1152:928",
            "768:1376",
            "1376:768",
            "1584:672",
            "512:2064",
            "2064:512",
            "352:2928",
            "2928:352",
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
            "1024:4128",
            "4128:1024",
            "704:5856",
            "5856:704",
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
            "2048:8256",
            "8256:2048",
            "1408:11712",
            "11712:1408",
        ]
        | Literal[
            "1024:1024",
            "1536:768",
            "768:1536",
            "1280:832",
            "832:1280",
            "1216:896",
            "896:1216",
            "1152:896",
            "896:1152",
            "832:1344",
            "1280:896",
            "896:1280",
            "1344:768",
            "768:1344",
        ]
        | Literal["1024:1024", "1216:896", "896:1216", "1344:768", "768:1344"]
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
        ]
        | Omit = omit,
        reference_images: Iterable[text_to_image_create_params.Gen4ImageTurboReferenceImage]
        | Iterable[text_to_image_create_params.Gen4ImageReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashReferenceImage]
        | Iterable[text_to_image_create_params.MuseImageReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5ProReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5LiteReferenceImage]
        | Iterable[text_to_image_create_params.GrokImagineImage2ReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3_1FlashLiteReferenceImage]
        | Iterable[text_to_image_create_params.GeminiImage3ProReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2_5FlareReferenceImage]
        | Iterable[text_to_image_create_params.GptImage2_5SunburstReferenceImage]
        | Iterable[text_to_image_create_params.BriaFibo1_5ReferenceImage]
        | Iterable[text_to_image_create_params.BriaFiboEdit1_5ReferenceImage]
        | Iterable[text_to_image_create_params.Ideogram4_0ReferenceImage]
        | Iterable[text_to_image_create_params.Ideogram4_5ReferenceImage]
        | Iterable[text_to_image_create_params.Seedream5FlashReferenceImage]
        | Iterable[text_to_image_create_params.NanoBanana2_1ReferenceImage]
        | Iterable[text_to_image_create_params.Gemini2_5FlashReferenceImage]
        | Omit = omit,
        content_moderation: text_to_image_create_params.Gen4ImageTurboContentModeration
        | text_to_image_create_params.Gen4ImageContentModeration
        | Omit = omit,
        seed: int | Omit = omit,
        background: Literal["transparent", "opaque", "auto"] | Literal["opaque", "auto"] | Omit = omit,
        output_count: int | Literal[1, 4] | Omit = omit,
        quality: Literal["low", "medium", "high", "auto"]
        | Literal["low", "medium"]
        | Literal["low", "medium", "high", "xhigh", "max"]
        | Literal["low", "medium", "high"]
        | Literal["very_low", "low", "medium", "high"]
        | Omit = omit,
        output_format: Literal["webp", "png", "jpeg"] | Literal["png", "jpeg"] | Literal["webp", "png"] | Omit = omit,
        grounding: bool | Omit = omit,
        edit: bool | Omit = omit,
        mask_uri: str | Omit = omit,
        precise_edit: bool | Omit = omit,
        thinking_level: Literal["minimal", "medium", "high"] | Omit = omit,
        background_color: str | Omit = omit,
        colors: SequenceNotStr[str] | Omit = omit,
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
                    "output_format": output_format,
                    "grounding": grounding,
                    "edit": edit,
                    "mask_uri": mask_uri,
                    "precise_edit": precise_edit,
                    "thinking_level": thinking_level,
                    "background_color": background_color,
                    "colors": colors,
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
