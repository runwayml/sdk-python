# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml._utils import parse_datetime
from runwayml.pagination import SyncCursorPage, AsyncCursorPage
from runwayml.types.organization import WebappListUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebapp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_usage(self, client: RunwayML) -> None:
        webapp = client.organization.webapp.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    def test_method_list_usage_with_all_params(self, client: RunwayML) -> None:
        webapp = client.organization.webapp.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workspace_ids="workspaceIds",
        )
        assert_matches_type(SyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    def test_raw_response_list_usage(self, client: RunwayML) -> None:
        response = client.organization.webapp.with_raw_response.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webapp = response.parse()
        assert_matches_type(SyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    def test_streaming_response_list_usage(self, client: RunwayML) -> None:
        with client.organization.webapp.with_streaming_response.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webapp = response.parse()
            assert_matches_type(SyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebapp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_usage(self, async_client: AsyncRunwayML) -> None:
        webapp = await async_client.organization.webapp.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    async def test_method_list_usage_with_all_params(self, async_client: AsyncRunwayML) -> None:
        webapp = await async_client.organization.webapp.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workspace_ids="workspaceIds",
        )
        assert_matches_type(AsyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    async def test_raw_response_list_usage(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.organization.webapp.with_raw_response.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webapp = await response.parse()
        assert_matches_type(AsyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

    @parametrize
    async def test_streaming_response_list_usage(self, async_client: AsyncRunwayML) -> None:
        async with async_client.organization.webapp.with_streaming_response.list_usage(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webapp = await response.parse()
            assert_matches_type(AsyncCursorPage[WebappListUsageResponse], webapp, path=["response"])

        assert cast(Any, response.is_closed) is True
