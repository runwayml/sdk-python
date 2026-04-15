# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import (
    VoiceListResponse,
    VoiceCreateResponse,
    VoicePreviewResponse,
    VoiceRetrieveResponse,
)
from runwayml.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        voice = client.voices.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        )
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        voice = client.voices.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
            description="x",
        )
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.voices.with_raw_response.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.voices.with_streaming_response.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceCreateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        voice = client.voices.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.voices.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.voices.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        voice = client.voices.list(
            limit=1,
        )
        assert_matches_type(SyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: RunwayML) -> None:
        voice = client.voices.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(SyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.voices.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(SyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.voices.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(SyncCursorPage[VoiceListResponse], voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RunwayML) -> None:
        voice = client.voices.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice is None

    @parametrize
    def test_raw_response_delete(self, client: RunwayML) -> None:
        response = client.voices.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert voice is None

    @parametrize
    def test_streaming_response_delete(self, client: RunwayML) -> None:
        with client.voices.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert voice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voices.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_preview(self, client: RunwayML) -> None:
        voice = client.voices.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(VoicePreviewResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: RunwayML) -> None:
        response = client.voices.with_raw_response.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoicePreviewResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: RunwayML) -> None:
        with client.voices.with_streaming_response.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoicePreviewResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        )
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
            description="x",
        )
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voices.with_raw_response.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceCreateResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voices.with_streaming_response.create(
            from_={
                "audio": "https://example.com/file",
                "type": "audio",
            },
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceCreateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voices.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voices.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.list(
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(AsyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voices.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(AsyncCursorPage[VoiceListResponse], voice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voices.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(AsyncCursorPage[VoiceListResponse], voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voices.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert voice is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voices.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert voice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voices.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_preview(self, async_client: AsyncRunwayML) -> None:
        voice = await async_client.voices.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(VoicePreviewResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.voices.with_raw_response.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoicePreviewResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncRunwayML) -> None:
        async with async_client.voices.with_streaming_response.preview(
            model="eleven_ttv_v3",
            prompt="xxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoicePreviewResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
