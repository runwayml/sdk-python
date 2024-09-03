# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import Runwayml, AsyncRunwayml
from tests.utils import assert_matches_type
from runwayml.types import TaskRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Runwayml) -> None:
        task = client.tasks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Runwayml) -> None:
        response = client.tasks.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Runwayml) -> None:
        with client.tasks.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Runwayml) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                id="",
                x_runway_version="2023-09-06",
            )

    @parametrize
    def test_method_delete(self, client: Runwayml) -> None:
        task = client.tasks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )
        assert task is None

    @parametrize
    def test_raw_response_delete(self, client: Runwayml) -> None:
        response = client.tasks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_delete(self, client: Runwayml) -> None:
        with client.tasks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Runwayml) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.delete(
                id="",
                x_runway_version="2023-09-06",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayml) -> None:
        task = await async_client.tasks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayml) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayml) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayml) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                id="",
                x_runway_version="2023-09-06",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncRunwayml) -> None:
        task = await async_client.tasks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )
        assert task is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRunwayml) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRunwayml) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_runway_version="2023-09-06",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRunwayml) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.delete(
                id="",
                x_runway_version="2023-09-06",
            )
