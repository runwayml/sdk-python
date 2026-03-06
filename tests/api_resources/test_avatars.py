# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import (
    AvatarListResponse,
    AvatarCreateResponse,
    AvatarUpdateResponse,
    AvatarRetrieveResponse,
)
from runwayml.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        avatar = client.avatars.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        avatar = client.avatars.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
            document_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_processing="optimize",
            start_script="Hello! How can I help you today?",
        )
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.avatars.with_raw_response.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.avatars.with_streaming_response.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        avatar = client.avatars.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.avatars.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.avatars.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.avatars.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: RunwayML) -> None:
        avatar = client.avatars.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: RunwayML) -> None:
        avatar = client.avatars.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_processing="optimize",
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            start_script="Hello! How can I help you today?",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: RunwayML) -> None:
        response = client.avatars.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: RunwayML) -> None:
        with client.avatars.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.avatars.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        avatar = client.avatars.list(
            limit=1,
        )
        assert_matches_type(SyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: RunwayML) -> None:
        avatar = client.avatars.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(SyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.avatars.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(SyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.avatars.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(SyncCursorPage[AvatarListResponse], avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RunwayML) -> None:
        avatar = client.avatars.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert avatar is None

    @parametrize
    def test_raw_response_delete(self, client: RunwayML) -> None:
        response = client.avatars.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert avatar is None

    @parametrize
    def test_streaming_response_delete(self, client: RunwayML) -> None:
        with client.avatars.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.avatars.with_raw_response.delete(
                "",
            )


class TestAsyncAvatars:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
            document_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_processing="optimize",
            start_script="Hello! How can I help you today?",
        )
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatars.with_raw_response.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatars.with_streaming_response.create(
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarCreateResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatars.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatars.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarRetrieveResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.avatars.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_processing="optimize",
            name="x",
            personality="You are a helpful support agent assisting users with their account questions. Be friendly, patient, and provide clear step-by-step guidance.",
            reference_image="https://example.com/reference.jpg",
            start_script="Hello! How can I help you today?",
            voice={
                "preset_id": "adrian",
                "type": "runway-live-preset",
            },
        )
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatars.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatars.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarUpdateResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.avatars.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.list(
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(AsyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatars.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AsyncCursorPage[AvatarListResponse], avatar, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatars.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AsyncCursorPage[AvatarListResponse], avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayML) -> None:
        avatar = await async_client.avatars.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert avatar is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatars.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert avatar is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatars.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.avatars.with_raw_response.delete(
                "",
            )
