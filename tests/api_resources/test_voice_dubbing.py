# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import VoiceDubbingCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoiceDubbing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        voice_dubbing = client.voice_dubbing.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        )
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        voice_dubbing = client.voice_dubbing.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
            disable_voice_cloning=True,
            drop_background_audio=True,
            num_speakers=9007199254740991,
        )
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.voice_dubbing.with_raw_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_dubbing = response.parse()
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.voice_dubbing.with_streaming_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_dubbing = response.parse()
            assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoiceDubbing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        voice_dubbing = await async_client.voice_dubbing.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        )
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        voice_dubbing = await async_client.voice_dubbing.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
            disable_voice_cloning=True,
            drop_background_audio=True,
            num_speakers=9007199254740991,
        )
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voice_dubbing.with_raw_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_dubbing = await response.parse()
        assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voice_dubbing.with_streaming_response.create(
            audio_uri="https://example.com/audio.mp3",
            model="eleven_voice_dubbing",
            target_lang="en",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_dubbing = await response.parse()
            assert_matches_type(VoiceDubbingCreateResponse, voice_dubbing, path=["response"])

        assert cast(Any, response.is_closed) is True
