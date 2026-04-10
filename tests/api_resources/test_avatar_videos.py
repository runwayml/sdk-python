# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import AvatarVideoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatarVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        avatar_video = client.avatar_videos.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        avatar_video = client.avatar_videos.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.avatar_videos.with_raw_response.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_video = response.parse()
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.avatar_videos.with_streaming_response.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_video = response.parse()
            assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvatarVideos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        avatar_video = await async_client.avatar_videos.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        avatar_video = await async_client.avatar_videos.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatar_videos.with_raw_response.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_video = await response.parse()
        assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatar_videos.with_streaming_response.create(
            avatar={
                "preset_id": "game-character",
                "type": "runway-preset",
            },
            model="gwm1_avatars",
            speech={
                "audio": "https://example.com/file",
                "type": "audio",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_video = await response.parse()
            assert_matches_type(AvatarVideoCreateResponse, avatar_video, path=["response"])

        assert cast(Any, response.is_closed) is True
