# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml._utils import parse_datetime
from runwayml.pagination import SyncCursorPage, AsyncCursorPage
from runwayml.types.organization.webapp import (
    AuditLogListResponse,
    AuditLogRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        audit_log = client.organization.webapp.audit_logs.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: RunwayML) -> None:
        audit_log = client.organization.webapp.audit_logs.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.organization.webapp.audit_logs.with_raw_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.organization.webapp.audit_logs.with_streaming_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.organization.webapp.audit_logs.with_raw_response.retrieve(
                event_id="",
            )

    @parametrize
    def test_method_list(self, client: RunwayML) -> None:
        audit_log = client.organization.webapp.audit_logs.list(
            limit=1,
        )
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: RunwayML) -> None:
        audit_log = client.organization.webapp.audit_logs.list(
            limit=1,
            actions="actions",
            actor_emails="actorEmails",
            cursor="x",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            workspace_ids="workspaceIds",
        )
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RunwayML) -> None:
        response = client.organization.webapp.audit_logs.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RunwayML) -> None:
        with client.organization.webapp.audit_logs.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        audit_log = await async_client.organization.webapp.audit_logs.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncRunwayML) -> None:
        audit_log = await async_client.organization.webapp.audit_logs.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.organization.webapp.audit_logs.with_raw_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.organization.webapp.audit_logs.with_streaming_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AuditLogRetrieveResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRunwayML) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.organization.webapp.audit_logs.with_raw_response.retrieve(
                event_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRunwayML) -> None:
        audit_log = await async_client.organization.webapp.audit_logs.list(
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRunwayML) -> None:
        audit_log = await async_client.organization.webapp.audit_logs.list(
            limit=1,
            actions="actions",
            actor_emails="actorEmails",
            cursor="x",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            workspace_ids="workspaceIds",
        )
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.organization.webapp.audit_logs.with_raw_response.list(
            limit=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRunwayML) -> None:
        async with async_client.organization.webapp.audit_logs.with_streaming_response.list(
            limit=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True
