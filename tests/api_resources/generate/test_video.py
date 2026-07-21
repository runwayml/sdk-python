# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types.generate import VideoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        video = client.generate.video.create(
            config_id="n6_",
            input={},
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        video = client.generate.video.create(
            config_id="n6_",
            input={
                "aspect_ratio": "16:9",
                "audio": True,
                "content_moderation": {"public_figure_threshold": "auto"},
                "duration": 2,
                "keyframes": [
                    {
                        "seconds": 0,
                        "uri": "https://example.com/file",
                        "range": {
                            "end_seconds": 1,
                            "start_seconds": 0,
                        },
                    }
                ],
                "negative_prompt": "negativePrompt",
                "prompt_text": "x",
                "reference_audio": [{"uri": "https://example.com/file"}],
                "reference_images": [
                    {
                        "role": "first",
                        "uri": "https://example.com/file",
                    }
                ],
                "reference_videos": [
                    {
                        "role": "source",
                        "uri": "https://example.com/file",
                    }
                ],
                "resolution": "480p",
                "seed": 0,
            },
            dry_run=True,
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.generate.video.with_raw_response.create(
            config_id="n6_",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.generate.video.with_streaming_response.create(
            config_id="n6_",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoCreateResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        video = await async_client.generate.video.create(
            config_id="n6_",
            input={},
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        video = await async_client.generate.video.create(
            config_id="n6_",
            input={
                "aspect_ratio": "16:9",
                "audio": True,
                "content_moderation": {"public_figure_threshold": "auto"},
                "duration": 2,
                "keyframes": [
                    {
                        "seconds": 0,
                        "uri": "https://example.com/file",
                        "range": {
                            "end_seconds": 1,
                            "start_seconds": 0,
                        },
                    }
                ],
                "negative_prompt": "negativePrompt",
                "prompt_text": "x",
                "reference_audio": [{"uri": "https://example.com/file"}],
                "reference_images": [
                    {
                        "role": "first",
                        "uri": "https://example.com/file",
                    }
                ],
                "reference_videos": [
                    {
                        "role": "source",
                        "uri": "https://example.com/file",
                    }
                ],
                "resolution": "480p",
                "seed": 0,
            },
            dry_run=True,
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.generate.video.with_raw_response.create(
            config_id="n6_",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.generate.video.with_streaming_response.create(
            config_id="n6_",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoCreateResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True
