# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import ImageUpscaleCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImageUpscale:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        image_upscale = client.image_upscale.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        )
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        image_upscale = client.image_upscale.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
            flavor="sublime",
            scale_factor=2,
            sharpen=0,
            smart_grain=0,
            ultra_detail=0,
        )
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.image_upscale.with_raw_response.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image_upscale = response.parse()
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.image_upscale.with_streaming_response.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image_upscale = response.parse()
            assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImageUpscale:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        image_upscale = await async_client.image_upscale.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        )
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        image_upscale = await async_client.image_upscale.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
            flavor="sublime",
            scale_factor=2,
            sharpen=0,
            smart_grain=0,
            ultra_detail=0,
        )
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.image_upscale.with_raw_response.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image_upscale = await response.parse()
        assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.image_upscale.with_streaming_response.create(
            image_uri="https://example.com/image.jpg",
            model="magnific_precision_upscaler_v2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image_upscale = await response.parse()
            assert_matches_type(ImageUpscaleCreateResponse, image_upscale, path=["response"])

        assert cast(Any, response.is_closed) is True
