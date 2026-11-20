# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import VideoToHdrCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideoToHdr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        video_to_hdr = client.video_to_hdr.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        )
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        video_to_hdr = client.video_to_hdr.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
            output_format="hdr10",
            prores_profile="422",
        )
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.video_to_hdr.with_raw_response.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_to_hdr = response.parse()
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.video_to_hdr.with_streaming_response.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_to_hdr = response.parse()
            assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideoToHdr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        video_to_hdr = await async_client.video_to_hdr.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        )
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        video_to_hdr = await async_client.video_to_hdr.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
            output_format="hdr10",
            prores_profile="422",
        )
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.video_to_hdr.with_raw_response.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_to_hdr = await response.parse()
        assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.video_to_hdr.with_streaming_response.create(
            model="ruby",
            video_uri="https://example.com/video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_to_hdr = await response.parse()
            assert_matches_type(VideoToHdrCreateResponse, video_to_hdr, path=["response"])

        assert cast(Any, response.is_closed) is True
