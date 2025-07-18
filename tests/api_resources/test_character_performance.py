# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import CharacterPerformanceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCharacterPerformance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        character_performance = client.character_performance.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        )
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        character_performance = client.character_performance.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
            body_control=True,
            content_moderation={"public_figure_threshold": "auto"},
            expression_intensity=1,
            seed=0,
        )
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.character_performance.with_raw_response.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_performance = response.parse()
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.character_performance.with_streaming_response.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_performance = response.parse()
            assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCharacterPerformance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        character_performance = await async_client.character_performance.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        )
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        character_performance = await async_client.character_performance.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
            body_control=True,
            content_moderation={"public_figure_threshold": "auto"},
            expression_intensity=1,
            seed=0,
        )
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.character_performance.with_raw_response.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_performance = await response.parse()
        assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.character_performance.with_streaming_response.create(
            character={
                "type": "video",
                "uri": "https://example.com",
            },
            model="act_two",
            ratio="1280:720",
            reference={
                "type": "video",
                "uri": "https://example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_performance = await response.parse()
            assert_matches_type(CharacterPerformanceCreateResponse, character_performance, path=["response"])

        assert cast(Any, response.is_closed) is True
