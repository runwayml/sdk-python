# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types.generate import AudioCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        audio = client.generate.audio.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        audio = client.generate.audio.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
                "duration": 0.5,
                "loop": True,
                "reference_audios": [{"uri": "https://example.com/file"}],
                "voice": {
                    "preset_id": "Maya",
                    "type": "preset",
                },
            },
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.generate.audio.with_raw_response.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.generate.audio.with_streaming_response.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(AudioCreateResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudio:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        audio = await async_client.generate.audio.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        audio = await async_client.generate.audio.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
                "duration": 0.5,
                "loop": True,
                "reference_audios": [{"uri": "https://example.com/file"}],
                "voice": {
                    "preset_id": "Maya",
                    "type": "preset",
                },
            },
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.generate.audio.with_raw_response.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.generate.audio.with_streaming_response.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "type": "speech",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(AudioCreateResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True
