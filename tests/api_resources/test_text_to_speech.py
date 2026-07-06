# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import TextToSpeechCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: RunwayML) -> None:
        text_to_speech = client.text_to_speech.create(
            model="seed_audio",
            prompt_text="x",
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: RunwayML) -> None:
        text_to_speech = client.text_to_speech.create(
            model="seed_audio",
            prompt_text="x",
            loudness_rate=-50,
            output_format="wav",
            pitch_rate=-12,
            sample_rate=8000,
            speech_rate=-50,
            voice={
                "audio_uri": "https://example.com/file",
                "type": "reference-audio",
            },
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: RunwayML) -> None:
        response = client.text_to_speech.with_raw_response.create(
            model="seed_audio",
            prompt_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: RunwayML) -> None:
        with client.text_to_speech.with_streaming_response.create(
            model="seed_audio",
            prompt_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: RunwayML) -> None:
        text_to_speech = client.text_to_speech.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: RunwayML) -> None:
        response = client.text_to_speech.with_raw_response.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: RunwayML) -> None:
        with client.text_to_speech.with_streaming_response.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_speech = await async_client.text_to_speech.create(
            model="seed_audio",
            prompt_text="x",
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_speech = await async_client.text_to_speech.create(
            model="seed_audio",
            prompt_text="x",
            loudness_rate=-50,
            output_format="wav",
            pitch_rate=-12,
            sample_rate=8000,
            speech_rate=-50,
            voice={
                "audio_uri": "https://example.com/file",
                "type": "reference-audio",
            },
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_speech.with_raw_response.create(
            model="seed_audio",
            prompt_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_speech.with_streaming_response.create(
            model="seed_audio",
            prompt_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        text_to_speech = await async_client.text_to_speech.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_speech.with_raw_response.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_speech.with_streaming_response.create(
            model="eleven_multilingual_v2",
            prompt_text="x",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechCreateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True
