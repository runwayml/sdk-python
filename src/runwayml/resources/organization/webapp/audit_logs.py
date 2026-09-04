# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.organization.webapp import audit_log_list_params, audit_log_retrieve_params
from ....types.organization.webapp.audit_log_list_response import AuditLogListResponse
from ....types.organization.webapp.audit_log_retrieve_response import AuditLogRetrieveResponse

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogRetrieveResponse:
        """
        Get a single audit log entry, including its metadata and forensic details, for a
        linked Runway workspace you administer. Authorized via the account link between
        this API project and the workspace.

        Args:
          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v1/organization/webapp/audit_logs/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, audit_log_retrieve_params.AuditLogRetrieveParams
                ),
            ),
            cast_to=AuditLogRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int,
        actions: str | Omit = omit,
        actor_emails: str | Omit = omit,
        cursor: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        organization_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        workspace_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AuditLogListResponse]:
        """
        List audit log entries for the linked Runway workspaces you administer, newest
        first. Authorized via the account link between this API project and the
        workspace.

        Args:
          limit: The maximum number of items to return per page.

          actions: Restrict results to these audit log actions, as a comma-separated list of up to
              50 actions. Allowed values: `UserLogin`, `PasswordChanged`,
              `EmailChangeRequested`, `EmailChanged`, `UserRegistered`, `UserAccountDeleted`,
              `WorkspaceCreated`, `WorkspaceDeleted`, `MemberInvited`, `MemberRemoved`,
              `MemberRoleChanged`, `InviteAccepted`, `TeamSettingsUpdated`,
              `InviteLinkToggled`, `UserGroupCreated`, `UserGroupDeleted`,
              `UserGroupMemberAdded`, `UserGroupMemberRemoved`, `SSOLogin`,
              `SSOUserProvisioned`, `SSOConfigCreated`, `SSOUserAutoAddedToTeam`,
              `SSODomainRegistrationCloned`, `AssetCreated`, `AssetUpdated`, `AssetDeleted`,
              `AssetDownloaded`, `AssetShared`, `AssetUnshared`, `PermissionGranted`,
              `PermissionUpdated`, `PermissionRevoked`, `PermissionAccepted`,
              `SubscriptionCancelled`, `SubscriptionPlanSwitched`, `CreditsTransferred`,
              `SeatsTransferred`, `SessionShared`, `SessionUnshared`, `VideoProjectShared`,
              `VideoProjectUnshared`, `BrandKitShared`, `BrandKitUnshared`,
              `AgentCustomSkillCreated`, `AgentCustomSkillDeleted`, `AgentCustomSkillShared`,
              `AgentCustomSkillUnshared`, `AgentSessionShared`, `AgentSessionUnshared`,
              `AgentConnectorLinkTokenCreated`, `AgentConnectorConnected`,
              `AgentConnectorDisconnected`, `AgentConnectorAssetExported`,
              `AgentConnectorSessionEnabled`, `AgentConnectorSessionDisabled`,
              `GenerationCreated`, `AccountLinkCreated`, `AccountLinkDeleted`,
              `OrganizationSettingsUpdated`, `OrganizationDisabledModelsUpdated`,
              `WorkspaceCountryLockUpdated`, `WorkspaceTagCreated`, `WorkspaceTagUpdated`,
              `WorkspaceTagDeleted`, `WorkspaceTagAssigned`, `WorkspaceTagUnassigned`,
              `MeteredBillingConfigUpdated`, `MeteredBillingRefillTriggered`,
              `MeteredBillingRetryTriggered`, `EnterpriseSpendCapEnforcementUpdated`.

          actor_emails: Restrict results to entries performed by the users with these emails, as a
              comma-separated list of up to 50 emails.

          cursor: Cursor from a previous response for fetching the next page of results.

          from_: Start of the time window (inclusive), ISO-8601 datetime.

          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          to: End of the time window (exclusive), ISO-8601 datetime.

          workspace_ids: Restrict results to these workspace IDs, as a comma-separated list of up to 50
              IDs. Defaults to every workspace you administer in the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/organization/webapp/audit_logs",
            page=SyncCursorPage[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "actions": actions,
                        "actor_emails": actor_emails,
                        "cursor": cursor,
                        "from_": from_,
                        "organization_id": organization_id,
                        "to": to,
                        "workspace_ids": workspace_ids,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogRetrieveResponse:
        """
        Get a single audit log entry, including its metadata and forensic details, for a
        linked Runway workspace you administer. Authorized via the account link between
        this API project and the workspace.

        Args:
          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v1/organization/webapp/audit_logs/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, audit_log_retrieve_params.AuditLogRetrieveParams
                ),
            ),
            cast_to=AuditLogRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int,
        actions: str | Omit = omit,
        actor_emails: str | Omit = omit,
        cursor: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        organization_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        workspace_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogListResponse, AsyncCursorPage[AuditLogListResponse]]:
        """
        List audit log entries for the linked Runway workspaces you administer, newest
        first. Authorized via the account link between this API project and the
        workspace.

        Args:
          limit: The maximum number of items to return per page.

          actions: Restrict results to these audit log actions, as a comma-separated list of up to
              50 actions. Allowed values: `UserLogin`, `PasswordChanged`,
              `EmailChangeRequested`, `EmailChanged`, `UserRegistered`, `UserAccountDeleted`,
              `WorkspaceCreated`, `WorkspaceDeleted`, `MemberInvited`, `MemberRemoved`,
              `MemberRoleChanged`, `InviteAccepted`, `TeamSettingsUpdated`,
              `InviteLinkToggled`, `UserGroupCreated`, `UserGroupDeleted`,
              `UserGroupMemberAdded`, `UserGroupMemberRemoved`, `SSOLogin`,
              `SSOUserProvisioned`, `SSOConfigCreated`, `SSOUserAutoAddedToTeam`,
              `SSODomainRegistrationCloned`, `AssetCreated`, `AssetUpdated`, `AssetDeleted`,
              `AssetDownloaded`, `AssetShared`, `AssetUnshared`, `PermissionGranted`,
              `PermissionUpdated`, `PermissionRevoked`, `PermissionAccepted`,
              `SubscriptionCancelled`, `SubscriptionPlanSwitched`, `CreditsTransferred`,
              `SeatsTransferred`, `SessionShared`, `SessionUnshared`, `VideoProjectShared`,
              `VideoProjectUnshared`, `BrandKitShared`, `BrandKitUnshared`,
              `AgentCustomSkillCreated`, `AgentCustomSkillDeleted`, `AgentCustomSkillShared`,
              `AgentCustomSkillUnshared`, `AgentSessionShared`, `AgentSessionUnshared`,
              `AgentConnectorLinkTokenCreated`, `AgentConnectorConnected`,
              `AgentConnectorDisconnected`, `AgentConnectorAssetExported`,
              `AgentConnectorSessionEnabled`, `AgentConnectorSessionDisabled`,
              `GenerationCreated`, `AccountLinkCreated`, `AccountLinkDeleted`,
              `OrganizationSettingsUpdated`, `OrganizationDisabledModelsUpdated`,
              `WorkspaceCountryLockUpdated`, `WorkspaceTagCreated`, `WorkspaceTagUpdated`,
              `WorkspaceTagDeleted`, `WorkspaceTagAssigned`, `WorkspaceTagUnassigned`,
              `MeteredBillingConfigUpdated`, `MeteredBillingRefillTriggered`,
              `MeteredBillingRetryTriggered`, `EnterpriseSpendCapEnforcementUpdated`.

          actor_emails: Restrict results to entries performed by the users with these emails, as a
              comma-separated list of up to 50 emails.

          cursor: Cursor from a previous response for fetching the next page of results.

          from_: Start of the time window (inclusive), ISO-8601 datetime.

          organization_id: Organization to report on. Optional when this API project is linked to a single
              organization; required when it is linked to more than one.

          to: End of the time window (exclusive), ISO-8601 datetime.

          workspace_ids: Restrict results to these workspace IDs, as a comma-separated list of up to 50
              IDs. Defaults to every workspace you administer in the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/organization/webapp/audit_logs",
            page=AsyncCursorPage[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "actions": actions,
                        "actor_emails": actor_emails,
                        "cursor": cursor,
                        "from_": from_,
                        "organization_id": organization_id,
                        "to": to,
                        "workspace_ids": workspace_ids,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.retrieve = to_raw_response_wrapper(
            audit_logs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.retrieve = async_to_raw_response_wrapper(
            audit_logs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.retrieve = to_streamed_response_wrapper(
            audit_logs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.retrieve = async_to_streamed_response_wrapper(
            audit_logs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
