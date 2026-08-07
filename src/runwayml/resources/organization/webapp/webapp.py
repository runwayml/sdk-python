# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform
from ...._compat import cached_property
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.organization import webapp_list_usage_params
from ....types.organization.webapp_list_usage_response import WebappListUsageResponse

__all__ = ["WebappResource", "AsyncWebappResource"]


class WebappResource(SyncAPIResource):
    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return WebappResourceWithStreamingResponse(self)

    def list_usage(
        self,
        *,
        from_: Union[str, datetime],
        limit: int,
        to: Union[str, datetime],
        cursor: str | Omit = omit,
        organization_id: str | Omit = omit,
        workspace_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WebappListUsageResponse]:
        """
        List per-generation credit-usage rows for the linked Runway workspaces you
        administer, newest first. Unlike `/v1/organization/usage` (this API project's
        own usage), this reports usage from the workspace linked to this API project.
        Authorized via that account link.

        Args:
          from_: Start of the time window (inclusive), ISO-8601 datetime.

          limit: The maximum number of items to return per page.

          to: End of the time window (exclusive), ISO-8601 datetime. A `cursor` can only
              narrow this window, never extend it past `to`.

          cursor: Cursor from a previous response for fetching the next page of results.

          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          workspace_ids: Restrict results to these workspace IDs, as a comma-separated list. Defaults to
              every workspace you administer in the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/organization/webapp/usage",
            page=SyncCursorPage[WebappListUsageResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "limit": limit,
                        "to": to,
                        "cursor": cursor,
                        "organization_id": organization_id,
                        "workspace_ids": workspace_ids,
                    },
                    webapp_list_usage_params.WebappListUsageParams,
                ),
            ),
            model=WebappListUsageResponse,
        )


class AsyncWebappResource(AsyncAPIResource):
    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncWebappResourceWithStreamingResponse(self)

    def list_usage(
        self,
        *,
        from_: Union[str, datetime],
        limit: int,
        to: Union[str, datetime],
        cursor: str | Omit = omit,
        organization_id: str | Omit = omit,
        workspace_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebappListUsageResponse, AsyncCursorPage[WebappListUsageResponse]]:
        """
        List per-generation credit-usage rows for the linked Runway workspaces you
        administer, newest first. Unlike `/v1/organization/usage` (this API project's
        own usage), this reports usage from the workspace linked to this API project.
        Authorized via that account link.

        Args:
          from_: Start of the time window (inclusive), ISO-8601 datetime.

          limit: The maximum number of items to return per page.

          to: End of the time window (exclusive), ISO-8601 datetime. A `cursor` can only
              narrow this window, never extend it past `to`.

          cursor: Cursor from a previous response for fetching the next page of results.

          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          workspace_ids: Restrict results to these workspace IDs, as a comma-separated list. Defaults to
              every workspace you administer in the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/organization/webapp/usage",
            page=AsyncCursorPage[WebappListUsageResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "limit": limit,
                        "to": to,
                        "cursor": cursor,
                        "organization_id": organization_id,
                        "workspace_ids": workspace_ids,
                    },
                    webapp_list_usage_params.WebappListUsageParams,
                ),
            ),
            model=WebappListUsageResponse,
        )


class WebappResourceWithRawResponse:
    def __init__(self, webapp: WebappResource) -> None:
        self._webapp = webapp

        self.list_usage = to_raw_response_wrapper(
            webapp.list_usage,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._webapp.audit_logs)


class AsyncWebappResourceWithRawResponse:
    def __init__(self, webapp: AsyncWebappResource) -> None:
        self._webapp = webapp

        self.list_usage = async_to_raw_response_wrapper(
            webapp.list_usage,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._webapp.audit_logs)


class WebappResourceWithStreamingResponse:
    def __init__(self, webapp: WebappResource) -> None:
        self._webapp = webapp

        self.list_usage = to_streamed_response_wrapper(
            webapp.list_usage,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._webapp.audit_logs)


class AsyncWebappResourceWithStreamingResponse:
    def __init__(self, webapp: AsyncWebappResource) -> None:
        self._webapp = webapp

        self.list_usage = async_to_streamed_response_wrapper(
            webapp.list_usage,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._webapp.audit_logs)
