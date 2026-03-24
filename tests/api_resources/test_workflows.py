# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import WorkflowRunResponse, WorkflowListResponse, WorkflowRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        workflow = client.workflows.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.workflows.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.workflows.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        workflow = client.workflows.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run(self, client: RunwayML) -> None:
        workflow = client.workflows.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    def test_method_run_with_all_params(self, client: RunwayML) -> None:
        workflow = client.workflows.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            node_outputs={
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e": {
                    "foo": {
                        "type": "primitive",
                        "value": "string",
                    }
                }
            },
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: RunwayML) -> None:
        response = client.workflows.with_raw_response.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: RunwayML) -> None:
        with client.workflows.with_streaming_response.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflows.with_raw_response.run(
                id="",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        workflow = await async_client.workflows.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.workflows.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        workflow = await async_client.workflows.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run(self, async_client: AsyncRunwayML) -> None:
        workflow = await async_client.workflows.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncRunwayML) -> None:
        workflow = await async_client.workflows.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            node_outputs={
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e": {
                    "foo": {
                        "type": "primitive",
                        "value": "string",
                    }
                }
            },
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.workflows.with_raw_response.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncRunwayML) -> None:
        async with async_client.workflows.with_streaming_response.run(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflows.with_raw_response.run(
                id="",
            )
