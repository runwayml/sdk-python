# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from runwayml.lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)

from ..types import (
    recipe_product_ad_params,
    recipe_product_ugc_params,
    recipe_product_swap_params,
    recipe_multi_shot_video_params,
    recipe_marketing_stock_image_params,
    recipe_product_campaign_image_params,
)
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
from .._base_client import make_request_options
from ..types.recipe_product_ad_response import RecipeProductAdResponse
from ..types.recipe_product_ugc_response import RecipeProductUgcResponse
from ..types.recipe_product_swap_response import RecipeProductSwapResponse
from ..types.recipe_multi_shot_video_response import RecipeMultiShotVideoResponse
from ..types.recipe_marketing_stock_image_response import RecipeMarketingStockImageResponse
from ..types.recipe_product_campaign_image_response import RecipeProductCampaignImageResponse

__all__ = ["RecipesResource", "AsyncRecipesResource"]


class RecipesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecipesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecipesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecipesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return RecipesResourceWithStreamingResponse(self)

    def marketing_stock_image(
        self,
        *,
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        reference_image: recipe_marketing_stock_image_params.ReferenceImage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate a polished marketing stock image from a text brief and optional brand
        logo image.

        Args:
          prompt: Marketing image brief. Describe the subject, audience, channel, desired mood,
              setting, and any constraints.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          reference_image: Optional brand logo image to guide the generated marketing stock image. See
              [our docs](/assets/inputs#images) on image inputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/recipes/marketing_stock_image",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "version": version,
                    "reference_image": reference_image,
                },
                recipe_marketing_stock_image_params.RecipeMarketingStockImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeMarketingStockImageResponse, self._client),
        )

    @overload
    def multi_shot_video(
        self,
        *,
        mode: Literal["auto"],
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant0FirstFrame | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate a multi-cut video from a story prompt (auto mode) or a custom shot list
        (custom mode).

        Args:
          mode: Workflow mode. `auto` decomposes a story prompt into exactly 5 shots.

          prompt: Story prompt for auto mode.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Total duration of the output video in seconds. Defaults to 10 seconds.

          first_frame: Optional image used as the first frame of the output video. See
              [our docs](/assets/inputs#images) on image inputs.

          ratio: Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`,
              `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`,
              `1440:1440`) use the pro tier. Defaults to `1280:720`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def multi_shot_video(
        self,
        *,
        mode: Literal["custom"],
        shots: Iterable[recipe_multi_shot_video_params.Variant1Shot],
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant1FirstFrame | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate a multi-cut video from a story prompt (auto mode) or a custom shot list
        (custom mode).

        Args:
          mode: Workflow mode. `custom` polishes a user-provided shot list of 3–5 shots.

          shots: Shot list for custom mode (3–5 shots). Per-shot durations must sum to
              `duration`.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Total duration of the output video in seconds. Defaults to 10 seconds.

          first_frame: Optional image used as the first frame of the output video. See
              [our docs](/assets/inputs#images) on image inputs.

          ratio: Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`,
              `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`,
              `1440:1440`) use the pro tier. Defaults to `1280:720`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["mode", "prompt", "version"], ["mode", "shots", "version"])
    def multi_shot_video(
        self,
        *,
        mode: Literal["auto"] | Literal["custom"],
        prompt: str | Omit = omit,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant0FirstFrame
        | recipe_multi_shot_video_params.Variant1FirstFrame
        | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        shots: Iterable[recipe_multi_shot_video_params.Variant1Shot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/recipes/multi_shot_video",
            body=maybe_transform(
                {
                    "mode": mode,
                    "prompt": prompt,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "first_frame": first_frame,
                    "ratio": ratio,
                    "shots": shots,
                },
                recipe_multi_shot_video_params.RecipeMultiShotVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeMultiShotVideoResponse, self._client),
        )

    def product_ad(
        self,
        *,
        product_images: Iterable[recipe_product_ad_params.ProductImage],
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        product_info: str | Omit = omit,
        ratio: Literal[
            "1280:720", "720:1280", "960:960", "834:1112", "1920:1080", "1080:1920", "1440:1440", "1248:1664"
        ]
        | Omit = omit,
        style_images: Iterable[recipe_product_ad_params.StyleImage] | Omit = omit,
        user_concept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate a cinematic product ad from product images, optional style references,
        product info, and creative direction.

        Args:
          product_images: Product images (1–10). Multiple angles of the same product. All images inform
              product analysis and reference generation; only the first image is used as the
              primary product reference in the storyboard grid. See
              [our docs](/assets/inputs#images) on image inputs.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 10 seconds.

          product_info: Optional product description and specifications to inform creative direction and
              which product elements to highlight.

          ratio: The resolution of the output video.

          style_images: Optional style reference images (0–4). Defines the visual treatment (lighting,
              palette, mood). Treated as a moodboard when multiple are provided.

          user_concept: Optional creative direction describing brand voice, product framing, scene
              specifics, lighting, camera motion, and narrative.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/recipes/product_ad",
            body=maybe_transform(
                {
                    "product_images": product_images,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "product_info": product_info,
                    "ratio": ratio,
                    "style_images": style_images,
                    "user_concept": user_concept,
                },
                recipe_product_ad_params.RecipeProductAdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeProductAdResponse, self._client),
        )

    def product_campaign_image(
        self,
        *,
        image: recipe_product_campaign_image_params.Image,
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate four fashion campaign images from a product image and style brief.

        Args:
          image: Product image to preserve across the generated campaign. See
              [our docs](/assets/inputs#images) on image inputs.

          prompt: Style / creative brief for the fashion campaign, e.g. "High-key fashion
              editorial, gorpcore-meets-blokecore-meets-Y2K".

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/recipes/product_campaign_image",
            body=maybe_transform(
                {
                    "image": image,
                    "prompt": prompt,
                    "version": version,
                },
                recipe_product_campaign_image_params.RecipeProductCampaignImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeProductCampaignImageResponse, self._client),
        )

    def product_swap(
        self,
        *,
        new_product_images: Iterable[recipe_product_swap_params.NewProductImage],
        original_product_image: recipe_product_swap_params.OriginalProductImage,
        reference_video: recipe_product_swap_params.ReferenceVideo,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        resolution: Literal["720p", "1080p"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Replace the product in a reference video with a new product, preserving camera
        motion, lighting, and scene composition.

        Args:
          new_product_images: Reference images of the new product (1–10). Supply multiple angles when the
              reference video shows the product from different views — optionally label each
              with `view` ("front", "side", or "back"). A single pre-composed reference sheet
              is also supported (omit `view`). See [our docs](/assets/inputs#images) on image
              inputs.

          original_product_image: Image of the original product being swapped out. See
              [our docs](/assets/inputs#images) on image inputs.

          reference_video: Reference video containing the product to swap. Duration must be between 1.8 and
              15 seconds. See [our docs](/assets/inputs#videos) on video inputs.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 10 seconds.

          resolution: Output video resolution. Defaults to 720p.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/recipes/product_swap",
            body=maybe_transform(
                {
                    "new_product_images": new_product_images,
                    "original_product_image": original_product_image,
                    "reference_video": reference_video,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "resolution": resolution,
                },
                recipe_product_swap_params.RecipeProductSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeProductSwapResponse, self._client),
        )

    def product_ugc(
        self,
        *,
        character_image: recipe_product_ugc_params.CharacterImage,
        product_image: recipe_product_ugc_params.ProductImage,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        product_info: str | Omit = omit,
        ratio: Literal["720:1280", "1080:1920"] | Omit = omit,
        user_concept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        Generate a vertical user-generated content ad from a character image, product
        image, product details, and optional creative direction.

        Args:
          character_image: Image of the character who will appear on camera in the UGC video. Aspect ratio
              (width / height) must be between 0.4 and 4. See
              [our docs](/assets/inputs#images) for image input requirements.

          product_image: Image of the product being promoted. Aspect ratio (width / height) must be
              between 0.4 and 4. See [our docs](/assets/inputs#images) for image input
              requirements.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 15 seconds.

          product_info: Product details and creative brief — what the product is, key benefits, and any
              specifics the script should reference.

          ratio: The resolution of the output video.

          user_concept: Optional creative direction for the UGC video — tone, voice register, specific
              message, or an entire dialog script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/recipes/product_ugc",
            body=maybe_transform(
                {
                    "character_image": character_image,
                    "product_image": product_image,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "product_info": product_info,
                    "ratio": ratio,
                    "user_concept": user_concept,
                },
                recipe_product_ugc_params.RecipeProductUgcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(RecipeProductUgcResponse, self._client),
        )


class AsyncRecipesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecipesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecipesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecipesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncRecipesResourceWithStreamingResponse(self)

    async def marketing_stock_image(
        self,
        *,
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        reference_image: recipe_marketing_stock_image_params.ReferenceImage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate a polished marketing stock image from a text brief and optional brand
        logo image.

        Args:
          prompt: Marketing image brief. Describe the subject, audience, channel, desired mood,
              setting, and any constraints.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          reference_image: Optional brand logo image to guide the generated marketing stock image. See
              [our docs](/assets/inputs#images) on image inputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/recipes/marketing_stock_image",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "version": version,
                    "reference_image": reference_image,
                },
                recipe_marketing_stock_image_params.RecipeMarketingStockImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeMarketingStockImageResponse, self._client),
        )

    @overload
    async def multi_shot_video(
        self,
        *,
        mode: Literal["auto"],
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant0FirstFrame | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate a multi-cut video from a story prompt (auto mode) or a custom shot list
        (custom mode).

        Args:
          mode: Workflow mode. `auto` decomposes a story prompt into exactly 5 shots.

          prompt: Story prompt for auto mode.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Total duration of the output video in seconds. Defaults to 10 seconds.

          first_frame: Optional image used as the first frame of the output video. See
              [our docs](/assets/inputs#images) on image inputs.

          ratio: Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`,
              `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`,
              `1440:1440`) use the pro tier. Defaults to `1280:720`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def multi_shot_video(
        self,
        *,
        mode: Literal["custom"],
        shots: Iterable[recipe_multi_shot_video_params.Variant1Shot],
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant1FirstFrame | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate a multi-cut video from a story prompt (auto mode) or a custom shot list
        (custom mode).

        Args:
          mode: Workflow mode. `custom` polishes a user-provided shot list of 3–5 shots.

          shots: Shot list for custom mode (3–5 shots). Per-shot durations must sum to
              `duration`.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Total duration of the output video in seconds. Defaults to 10 seconds.

          first_frame: Optional image used as the first frame of the output video. See
              [our docs](/assets/inputs#images) on image inputs.

          ratio: Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`,
              `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`,
              `1440:1440`) use the pro tier. Defaults to `1280:720`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["mode", "prompt", "version"], ["mode", "shots", "version"])
    async def multi_shot_video(
        self,
        *,
        mode: Literal["auto"] | Literal["custom"],
        prompt: str | Omit = omit,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: Literal[5, 10, 15] | Omit = omit,
        first_frame: recipe_multi_shot_video_params.Variant0FirstFrame
        | recipe_multi_shot_video_params.Variant1FirstFrame
        | Omit = omit,
        ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"] | Omit = omit,
        shots: Iterable[recipe_multi_shot_video_params.Variant1Shot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/recipes/multi_shot_video",
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "prompt": prompt,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "first_frame": first_frame,
                    "ratio": ratio,
                    "shots": shots,
                },
                recipe_multi_shot_video_params.RecipeMultiShotVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeMultiShotVideoResponse, self._client),
        )

    async def product_ad(
        self,
        *,
        product_images: Iterable[recipe_product_ad_params.ProductImage],
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        product_info: str | Omit = omit,
        ratio: Literal[
            "1280:720", "720:1280", "960:960", "834:1112", "1920:1080", "1080:1920", "1440:1440", "1248:1664"
        ]
        | Omit = omit,
        style_images: Iterable[recipe_product_ad_params.StyleImage] | Omit = omit,
        user_concept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate a cinematic product ad from product images, optional style references,
        product info, and creative direction.

        Args:
          product_images: Product images (1–10). Multiple angles of the same product. All images inform
              product analysis and reference generation; only the first image is used as the
              primary product reference in the storyboard grid. See
              [our docs](/assets/inputs#images) on image inputs.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 10 seconds.

          product_info: Optional product description and specifications to inform creative direction and
              which product elements to highlight.

          ratio: The resolution of the output video.

          style_images: Optional style reference images (0–4). Defines the visual treatment (lighting,
              palette, mood). Treated as a moodboard when multiple are provided.

          user_concept: Optional creative direction describing brand voice, product framing, scene
              specifics, lighting, camera motion, and narrative.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/recipes/product_ad",
            body=await async_maybe_transform(
                {
                    "product_images": product_images,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "product_info": product_info,
                    "ratio": ratio,
                    "style_images": style_images,
                    "user_concept": user_concept,
                },
                recipe_product_ad_params.RecipeProductAdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeProductAdResponse, self._client),
        )

    async def product_campaign_image(
        self,
        *,
        image: recipe_product_campaign_image_params.Image,
        prompt: str,
        version: Literal["2026-06", "unsafe-latest"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate four fashion campaign images from a product image and style brief.

        Args:
          image: Product image to preserve across the generated campaign. See
              [our docs](/assets/inputs#images) on image inputs.

          prompt: Style / creative brief for the fashion campaign, e.g. "High-key fashion
              editorial, gorpcore-meets-blokecore-meets-Y2K".

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/recipes/product_campaign_image",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "prompt": prompt,
                    "version": version,
                },
                recipe_product_campaign_image_params.RecipeProductCampaignImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeProductCampaignImageResponse, self._client),
        )

    async def product_swap(
        self,
        *,
        new_product_images: Iterable[recipe_product_swap_params.NewProductImage],
        original_product_image: recipe_product_swap_params.OriginalProductImage,
        reference_video: recipe_product_swap_params.ReferenceVideo,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        resolution: Literal["720p", "1080p"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Replace the product in a reference video with a new product, preserving camera
        motion, lighting, and scene composition.

        Args:
          new_product_images: Reference images of the new product (1–10). Supply multiple angles when the
              reference video shows the product from different views — optionally label each
              with `view` ("front", "side", or "back"). A single pre-composed reference sheet
              is also supported (omit `view`). See [our docs](/assets/inputs#images) on image
              inputs.

          original_product_image: Image of the original product being swapped out. See
              [our docs](/assets/inputs#images) on image inputs.

          reference_video: Reference video containing the product to swap. Duration must be between 1.8 and
              15 seconds. See [our docs](/assets/inputs#videos) on video inputs.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 10 seconds.

          resolution: Output video resolution. Defaults to 720p.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/recipes/product_swap",
            body=await async_maybe_transform(
                {
                    "new_product_images": new_product_images,
                    "original_product_image": original_product_image,
                    "reference_video": reference_video,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "resolution": resolution,
                },
                recipe_product_swap_params.RecipeProductSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeProductSwapResponse, self._client),
        )

    async def product_ugc(
        self,
        *,
        character_image: recipe_product_ugc_params.CharacterImage,
        product_image: recipe_product_ugc_params.ProductImage,
        version: Literal["2026-06", "unsafe-latest"],
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        product_info: str | Omit = omit,
        ratio: Literal["720:1280", "1080:1920"] | Omit = omit,
        user_concept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        Generate a vertical user-generated content ad from a character image, product
        image, product details, and optional creative direction.

        Args:
          character_image: Image of the character who will appear on camera in the UGC video. Aspect ratio
              (width / height) must be between 0.4 and 4. See
              [our docs](/assets/inputs#images) for image input requirements.

          product_image: Image of the product being promoted. Aspect ratio (width / height) must be
              between 0.4 and 4. See [our docs](/assets/inputs#images) for image input
              requirements.

          version: Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or
              "unsafe-latest" to track the newest stable version (may break without notice).

          audio: Whether to generate audio for the video.

          duration: Duration of the output video in seconds (4–15). Defaults to 15 seconds.

          product_info: Product details and creative brief — what the product is, key benefits, and any
              specifics the script should reference.

          ratio: The resolution of the output video.

          user_concept: Optional creative direction for the UGC video — tone, voice register, specific
              message, or an entire dialog script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/recipes/product_ugc",
            body=await async_maybe_transform(
                {
                    "character_image": character_image,
                    "product_image": product_image,
                    "version": version,
                    "audio": audio,
                    "duration": duration,
                    "product_info": product_info,
                    "ratio": ratio,
                    "user_concept": user_concept,
                },
                recipe_product_ugc_params.RecipeProductUgcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(RecipeProductUgcResponse, self._client),
        )


class RecipesResourceWithRawResponse:
    def __init__(self, recipes: RecipesResource) -> None:
        self._recipes = recipes

        self.marketing_stock_image = to_raw_response_wrapper(
            recipes.marketing_stock_image,
        )
        self.multi_shot_video = to_raw_response_wrapper(
            recipes.multi_shot_video,
        )
        self.product_ad = to_raw_response_wrapper(
            recipes.product_ad,
        )
        self.product_campaign_image = to_raw_response_wrapper(
            recipes.product_campaign_image,
        )
        self.product_swap = to_raw_response_wrapper(
            recipes.product_swap,
        )
        self.product_ugc = to_raw_response_wrapper(
            recipes.product_ugc,
        )


class AsyncRecipesResourceWithRawResponse:
    def __init__(self, recipes: AsyncRecipesResource) -> None:
        self._recipes = recipes

        self.marketing_stock_image = async_to_raw_response_wrapper(
            recipes.marketing_stock_image,
        )
        self.multi_shot_video = async_to_raw_response_wrapper(
            recipes.multi_shot_video,
        )
        self.product_ad = async_to_raw_response_wrapper(
            recipes.product_ad,
        )
        self.product_campaign_image = async_to_raw_response_wrapper(
            recipes.product_campaign_image,
        )
        self.product_swap = async_to_raw_response_wrapper(
            recipes.product_swap,
        )
        self.product_ugc = async_to_raw_response_wrapper(
            recipes.product_ugc,
        )


class RecipesResourceWithStreamingResponse:
    def __init__(self, recipes: RecipesResource) -> None:
        self._recipes = recipes

        self.marketing_stock_image = to_streamed_response_wrapper(
            recipes.marketing_stock_image,
        )
        self.multi_shot_video = to_streamed_response_wrapper(
            recipes.multi_shot_video,
        )
        self.product_ad = to_streamed_response_wrapper(
            recipes.product_ad,
        )
        self.product_campaign_image = to_streamed_response_wrapper(
            recipes.product_campaign_image,
        )
        self.product_swap = to_streamed_response_wrapper(
            recipes.product_swap,
        )
        self.product_ugc = to_streamed_response_wrapper(
            recipes.product_ugc,
        )


class AsyncRecipesResourceWithStreamingResponse:
    def __init__(self, recipes: AsyncRecipesResource) -> None:
        self._recipes = recipes

        self.marketing_stock_image = async_to_streamed_response_wrapper(
            recipes.marketing_stock_image,
        )
        self.multi_shot_video = async_to_streamed_response_wrapper(
            recipes.multi_shot_video,
        )
        self.product_ad = async_to_streamed_response_wrapper(
            recipes.product_ad,
        )
        self.product_campaign_image = async_to_streamed_response_wrapper(
            recipes.product_campaign_image,
        )
        self.product_swap = async_to_streamed_response_wrapper(
            recipes.product_swap,
        )
        self.product_ugc = async_to_streamed_response_wrapper(
            recipes.product_ugc,
        )
