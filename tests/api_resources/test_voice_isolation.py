# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import VoiceIsolationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoiceIsolation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        voice_isolation = client.voice_isolation.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        )
        assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.voice_isolation.with_raw_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_isolation = response.parse()
        assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.voice_isolation.with_streaming_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_isolation = response.parse()
            assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoiceIsolation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        voice_isolation = await async_client.voice_isolation.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        )
        assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voice_isolation.with_raw_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_isolation = await response.parse()
        assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voice_isolation.with_streaming_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_isolation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_isolation = await response.parse()
            assert_matches_type(VoiceIsolationCreateResponse, voice_isolation, path=["response"])

        assert cast(Any, response.is_closed) is True
