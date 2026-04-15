# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import SpeechToSpeechCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeechToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        speech_to_speech = client.speech_to_speech.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        speech_to_speech = client.speech_to_speech.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
            remove_background_noise=True,
        )
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.speech_to_speech.with_raw_response.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_speech = response.parse()
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.speech_to_speech.with_streaming_response.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_speech = response.parse()
            assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeechToSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        speech_to_speech = await async_client.speech_to_speech.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        speech_to_speech = await async_client.speech_to_speech.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
            remove_background_noise=True,
        )
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.speech_to_speech.with_raw_response.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_speech = await response.parse()
        assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.speech_to_speech.with_streaming_response.create(
            media={
                "type": "audio",
                "uri": "https://example.com/file",
            },
            model="eleven_multilingual_sts_v2",
            voice={
                "preset_id": "Maya",
                "type": "runway-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_speech = await response.parse()
            assert_matches_type(SpeechToSpeechCreateResponse, speech_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True
