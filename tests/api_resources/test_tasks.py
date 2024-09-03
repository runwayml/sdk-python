# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import TaskRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        task = client.tasks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.tasks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.tasks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_delete(self, client: RunwayML) -> None:
        task = client.tasks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert task is None

    @parametrize
    def test_raw_response_delete(self, client: RunwayML) -> None:
        response = client.tasks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_delete(self, client: RunwayML) -> None:
        with client.tasks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.delete(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        task = await async_client.tasks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayML) -> None:
        task = await async_client.tasks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert task is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayML) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.delete(
                "",
            )
