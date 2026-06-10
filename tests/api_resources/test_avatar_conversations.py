# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import (
    AvatarConversationListResponse,
    AvatarConversationRetrieveResponse,
)
from runwayml._utils import parse_datetime
from runwayml.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatarConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        avatar_conversation = client.avatar_conversations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.avatar_conversations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = response.parse()
        assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.avatar_conversations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = response.parse()
            assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.avatar_conversations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        avatar_conversation = client.avatar_conversations.list(
            limit=1,
        )
        assert_matches_type(SyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: RunwayML) -> None:
        avatar_conversation = client.avatar_conversations.list(
            limit=1,
            avatar="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.avatar_conversations.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = response.parse()
        assert_matches_type(SyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.avatar_conversations.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = response.parse()
            assert_matches_type(SyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RunwayML) -> None:
        avatar_conversation = client.avatar_conversations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert avatar_conversation is None

    @parametrize
    def test_raw_response_delete(self, client: RunwayML) -> None:
        response = client.avatar_conversations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = response.parse()
        assert avatar_conversation is None

    @parametrize
    def test_streaming_response_delete(self, client: RunwayML) -> None:
        with client.avatar_conversations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = response.parse()
            assert avatar_conversation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.avatar_conversations.with_raw_response.delete(
                "",
            )


class TestAsyncAvatarConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        avatar_conversation = await async_client.avatar_conversations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatar_conversations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = await response.parse()
        assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatar_conversations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = await response.parse()
            assert_matches_type(AvatarConversationRetrieveResponse, avatar_conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.avatar_conversations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        avatar_conversation = await async_client.avatar_conversations.list(
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRunwayML) -> None:
        avatar_conversation = await async_client.avatar_conversations.list(
            limit=1,
            avatar="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatar_conversations.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = await response.parse()
        assert_matches_type(AsyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatar_conversations.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = await response.parse()
            assert_matches_type(AsyncCursorPage[AvatarConversationListResponse], avatar_conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayML) -> None:
        avatar_conversation = await async_client.avatar_conversations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert avatar_conversation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.avatar_conversations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar_conversation = await response.parse()
        assert avatar_conversation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayML) -> None:
        async with async_client.avatar_conversations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar_conversation = await response.parse()
            assert avatar_conversation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.avatar_conversations.with_raw_response.delete(
                "",
            )
