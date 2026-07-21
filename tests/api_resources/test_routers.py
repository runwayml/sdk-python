# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import (
    RouterListResponse,
    RouterCreateResponse,
    RouterUpdateResponse,
    RouterRetrieveResponse,
)
from runwayml.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        router = client.routers.create(
            slug="slug",
        )
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        router = client.routers.create(
            slug="slug",
            description="description",
            name="x",
            settings={
                "max_credits_per_generation": {
                    "audio": 1,
                    "image": 1,
                    "video": 1,
                },
                "models": {
                    "ids": ["string"],
                    "mode": "allow_new_except",
                },
                "optimize_for": "cost",
                "schema_version": 1,
            },
        )
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.routers.with_raw_response.create(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.routers.with_streaming_response.create(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(RouterCreateResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        router = client.routers.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RouterRetrieveResponse, router, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.routers.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(RouterRetrieveResponse, router, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.routers.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(RouterRetrieveResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: RunwayML) -> None:
        router = client.routers.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: RunwayML) -> None:
        router = client.routers.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="x",
            settings={
                "max_credits_per_generation": {
                    "audio": 1,
                    "image": 1,
                    "video": 1,
                },
                "models": {
                    "ids": ["string"],
                    "mode": "allow_new_except",
                },
                "optimize_for": "cost",
                "schema_version": 1,
            },
        )
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: RunwayML) -> None:
        response = client.routers.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: RunwayML) -> None:
        with client.routers.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(RouterUpdateResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routers.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        router = client.routers.list(
            limit=1,
        )
        assert_matches_type(SyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: RunwayML) -> None:
        router = client.routers.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(SyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.routers.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(SyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.routers.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(SyncCursorPage[RouterListResponse], router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RunwayML) -> None:
        router = client.routers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert router is None

    @parametrize
    def test_raw_response_delete(self, client: RunwayML) -> None:
        response = client.routers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert router is None

    @parametrize
    def test_streaming_response_delete(self, client: RunwayML) -> None:
        with client.routers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert router is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routers.with_raw_response.delete(
                "",
            )


class TestAsyncRouters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.create(
            slug="slug",
        )
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.create(
            slug="slug",
            description="description",
            name="x",
            settings={
                "max_credits_per_generation": {
                    "audio": 1,
                    "image": 1,
                    "video": 1,
                },
                "models": {
                    "ids": ["string"],
                    "mode": "allow_new_except",
                },
                "optimize_for": "cost",
                "schema_version": 1,
            },
        )
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.routers.with_raw_response.create(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(RouterCreateResponse, router, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.routers.with_streaming_response.create(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(RouterCreateResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RouterRetrieveResponse, router, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.routers.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(RouterRetrieveResponse, router, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.routers.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(RouterRetrieveResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="x",
            settings={
                "max_credits_per_generation": {
                    "audio": 1,
                    "image": 1,
                    "video": 1,
                },
                "models": {
                    "ids": ["string"],
                    "mode": "allow_new_except",
                },
                "optimize_for": "cost",
                "schema_version": 1,
            },
        )
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.routers.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(RouterUpdateResponse, router, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRunwayML) -> None:
        async with async_client.routers.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(RouterUpdateResponse, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routers.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.list(
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.list(
            limit=1,
            cursor="x",
        )
        assert_matches_type(AsyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.routers.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(AsyncCursorPage[RouterListResponse], router, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.routers.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(AsyncCursorPage[RouterListResponse], router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayML) -> None:
        router = await async_client.routers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert router is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.routers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert router is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayML) -> None:
        async with async_client.routers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert router is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routers.with_raw_response.delete(
                "",
            )
