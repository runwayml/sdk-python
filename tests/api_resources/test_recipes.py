# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import (
    RecipeProductAdResponse,
    RecipeProductUgcResponse,
    RecipeProductSwapResponse,
    RecipeAdLocalizationResponse,
    RecipeMultiShotVideoResponse,
    RecipeMarketingStockImageResponse,
    RecipeProductCampaignImageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecipes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ad_localization(self, client: RunwayML) -> None:
        recipe = client.recipes.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        )
        assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_ad_localization(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_ad_localization(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_marketing_stock_image(self, client: RunwayML) -> None:
        recipe = client.recipes.marketing_stock_image(
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    def test_method_marketing_stock_image_with_all_params(self, client: RunwayML) -> None:
        recipe = client.recipes.marketing_stock_image(
            prompt="x",
            version="2026-06",
            output_count=1,
            quality="low",
            reference_image={"uri": "https://example.com/file"},
        )
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_marketing_stock_image(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.marketing_stock_image(
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_marketing_stock_image(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.marketing_stock_image(
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_multi_shot_video_overload_1(self, client: RunwayML) -> None:
        recipe = client.recipes.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_method_multi_shot_video_with_all_params_overload_1(self, client: RunwayML) -> None:
        recipe = client.recipes.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
            audio=True,
            duration=5,
            first_frame={"uri": "https://example.com/file"},
            ratio="1280:720",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_multi_shot_video_overload_1(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_multi_shot_video_overload_1(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_multi_shot_video_overload_2(self, client: RunwayML) -> None:
        recipe = client.recipes.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_method_multi_shot_video_with_all_params_overload_2(self, client: RunwayML) -> None:
        recipe = client.recipes.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
            audio=True,
            duration=5,
            first_frame={"uri": "https://example.com/file"},
            ratio="1280:720",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_multi_shot_video_overload_2(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_multi_shot_video_overload_2(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_product_ad(self, client: RunwayML) -> None:
        recipe = client.recipes.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        )
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    def test_method_product_ad_with_all_params(self, client: RunwayML) -> None:
        recipe = client.recipes.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
            audio=True,
            duration=4,
            product_info="productInfo",
            ratio="1280:720",
            style_images=[{"uri": "https://example.com/file"}],
            user_concept="userConcept",
        )
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_product_ad(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_product_ad(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_product_campaign_image(self, client: RunwayML) -> None:
        recipe = client.recipes.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_product_campaign_image(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_product_campaign_image(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_product_swap(self, client: RunwayML) -> None:
        recipe = client.recipes.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        )
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    def test_method_product_swap_with_all_params(self, client: RunwayML) -> None:
        recipe = client.recipes.product_swap(
            new_product_images=[
                {
                    "uri": "https://example.com/file",
                    "view": "front",
                }
            ],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
            audio=True,
            duration=4,
            resolution="720p",
        )
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_product_swap(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_product_swap(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_product_ugc(self, client: RunwayML) -> None:
        recipe = client.recipes.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        )
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    def test_method_product_ugc_with_all_params(self, client: RunwayML) -> None:
        recipe = client.recipes.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
            audio=True,
            duration=4,
            product_info="productInfo",
            ratio="720:1280",
            user_concept="userConcept",
        )
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    def test_raw_response_product_ugc(self, client: RunwayML) -> None:
        response = client.recipes.with_raw_response.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = response.parse()
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    def test_streaming_response_product_ugc(self, client: RunwayML) -> None:
        with client.recipes.with_streaming_response.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = response.parse()
            assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecipes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_ad_localization(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        )
        assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_ad_localization(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_ad_localization(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.ad_localization(
            reference_image={"uri": "https://example.com/file"},
            target_language="ar",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeAdLocalizationResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_marketing_stock_image(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.marketing_stock_image(
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    async def test_method_marketing_stock_image_with_all_params(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.marketing_stock_image(
            prompt="x",
            version="2026-06",
            output_count=1,
            quality="low",
            reference_image={"uri": "https://example.com/file"},
        )
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_marketing_stock_image(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.marketing_stock_image(
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_marketing_stock_image(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.marketing_stock_image(
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeMarketingStockImageResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_multi_shot_video_overload_1(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_method_multi_shot_video_with_all_params_overload_1(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
            audio=True,
            duration=5,
            first_frame={"uri": "https://example.com/file"},
            ratio="1280:720",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_multi_shot_video_overload_1(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_multi_shot_video_overload_1(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.multi_shot_video(
            mode="auto",
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_multi_shot_video_overload_2(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_method_multi_shot_video_with_all_params_overload_2(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
            audio=True,
            duration=5,
            first_frame={"uri": "https://example.com/file"},
            ratio="1280:720",
        )
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_multi_shot_video_overload_2(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_multi_shot_video_overload_2(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.multi_shot_video(
            mode="custom",
            shots=[
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
                {
                    "duration": 1,
                    "prompt": "xxx",
                },
            ],
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeMultiShotVideoResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_product_ad(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        )
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    async def test_method_product_ad_with_all_params(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
            audio=True,
            duration=4,
            product_info="productInfo",
            ratio="1280:720",
            style_images=[{"uri": "https://example.com/file"}],
            user_concept="userConcept",
        )
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_product_ad(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_product_ad(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.product_ad(
            product_images=[{"uri": "https://example.com/file"}],
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeProductAdResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_product_campaign_image(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        )
        assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_product_campaign_image(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_product_campaign_image(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.product_campaign_image(
            image={"uri": "https://example.com/file"},
            prompt="x",
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeProductCampaignImageResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_product_swap(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        )
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    async def test_method_product_swap_with_all_params(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_swap(
            new_product_images=[
                {
                    "uri": "https://example.com/file",
                    "view": "front",
                }
            ],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
            audio=True,
            duration=4,
            resolution="720p",
        )
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_product_swap(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_product_swap(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.product_swap(
            new_product_images=[{"uri": "https://example.com/file"}],
            original_product_image={"uri": "https://example.com/file"},
            reference_video={"uri": "https://example.com/file"},
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeProductSwapResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_product_ugc(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        )
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    async def test_method_product_ugc_with_all_params(self, async_client: AsyncRunwayML) -> None:
        recipe = await async_client.recipes.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
            audio=True,
            duration=4,
            product_info="productInfo",
            ratio="720:1280",
            user_concept="userConcept",
        )
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    async def test_raw_response_product_ugc(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.recipes.with_raw_response.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipe = await response.parse()
        assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

    @parametrize
    async def test_streaming_response_product_ugc(self, async_client: AsyncRunwayML) -> None:
        async with async_client.recipes.with_streaming_response.product_ugc(
            character_image={"uri": "https://example.com/file"},
            product_image={"uri": "https://example.com/file"},
            version="2026-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipe = await response.parse()
            assert_matches_type(RecipeProductUgcResponse, recipe, path=["response"])

        assert cast(Any, response.is_closed) is True
