# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import OrganizationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: RunwayML) -> None:
        organization = client.organization.retrieve()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RunwayML) -> None:
        response = client.organization.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RunwayML) -> None:
        with client.organization.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRunwayML) -> None:
        organization = await async_client.organization.retrieve()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.organization.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRunwayML) -> None:
        async with async_client.organization.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
