# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import VideoUpscaleCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideoUpscale:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        video_upscale = client.video_upscale.create(
            model="upscale_v1",
            video_uri="https://example.com",
        )
        assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.video_upscale.with_raw_response.create(
            model="upscale_v1",
            video_uri="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_upscale = response.parse()
        assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.video_upscale.with_streaming_response.create(
            model="upscale_v1",
            video_uri="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_upscale = response.parse()
            assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideoUpscale:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        video_upscale = await async_client.video_upscale.create(
            model="upscale_v1",
            video_uri="https://example.com",
        )
        assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.video_upscale.with_raw_response.create(
            model="upscale_v1",
            video_uri="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_upscale = await response.parse()
        assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.video_upscale.with_streaming_response.create(
            model="upscale_v1",
            video_uri="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_upscale = await response.parse()
            assert_matches_type(VideoUpscaleCreateResponse, video_upscale, path=["response"])

        assert cast(Any, response.is_closed) is True
