# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import SoundEffectCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSoundEffect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        sound_effect = client.sound_effect.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        )
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        sound_effect = client.sound_effect.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
            duration=0.5,
            loop=True,
        )
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.sound_effect.with_raw_response.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sound_effect = response.parse()
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.sound_effect.with_streaming_response.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sound_effect = response.parse()
            assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSoundEffect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        sound_effect = await async_client.sound_effect.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        )
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        sound_effect = await async_client.sound_effect.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
            duration=0.5,
            loop=True,
        )
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.sound_effect.with_raw_response.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sound_effect = await response.parse()
        assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.sound_effect.with_streaming_response.create(
            model="eleven_text_to_sound_v2",
            prompt_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sound_effect = await response.parse()
            assert_matches_type(SoundEffectCreateResponse, sound_effect, path=["response"])

        assert cast(Any, response.is_closed) is True
