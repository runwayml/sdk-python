# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditLogRetrieveResponse", "Metadata"]


class Metadata(BaseModel):
    """Action-specific details."""

    amount: Optional[object] = FieldInfo(alias="Amount", default=None)

    application: Optional[object] = FieldInfo(alias="Application", default=None)

    asset_name: Optional[object] = FieldInfo(alias="Asset name", default=None)

    default_task_name_template: Optional[object] = FieldInfo(alias="Default task name template", default=None)

    group_name: Optional[object] = FieldInfo(alias="Group name", default=None)

    hard_spend_cap: Optional[object] = FieldInfo(alias="Hard spend cap", default=None)

    invited_member: Optional[object] = FieldInfo(alias="Invited member", default=None)

    login_method: Optional[object] = FieldInfo(alias="Login method", default=None)

    member_email: Optional[object] = FieldInfo(alias="Member email", default=None)

    model: Optional[object] = FieldInfo(alias="Model", default=None)

    new_role: Optional[object] = FieldInfo(alias="New role", default=None)

    new_user: Optional[object] = FieldInfo(alias="New User", default=None)

    operation: Optional[object] = FieldInfo(alias="Operation", default=None)

    plan: Optional[object] = FieldInfo(alias="Plan", default=None)

    platform: Optional[object] = FieldInfo(alias="Platform", default=None)

    previous_role: Optional[object] = FieldInfo(alias="Previous role", default=None)

    removed_member: Optional[object] = FieldInfo(alias="Removed member", default=None)

    role: Optional[object] = FieldInfo(alias="Role", default=None)

    shared_with_projects: Optional[object] = FieldInfo(alias="Shared with projects", default=None)

    shared_with_workspace: Optional[object] = FieldInfo(alias="Shared with workspace", default=None)

    spend_cap: Optional[object] = FieldInfo(alias="Spend cap", default=None)

    tag_color: Optional[object] = FieldInfo(alias="Tag color", default=None)

    tag_name: Optional[object] = FieldInfo(alias="Tag name", default=None)

    target_member: Optional[object] = FieldInfo(alias="Target member", default=None)

    workspace: Optional[object] = FieldInfo(alias="Workspace", default=None)

    workspace_description: Optional[object] = FieldInfo(alias="Workspace description", default=None)

    workspace_id: Optional[object] = FieldInfo(alias="Workspace ID", default=None)

    workspace_name: Optional[object] = FieldInfo(alias="Workspace name", default=None)

    workspace_picture: Optional[object] = FieldInfo(alias="Workspace picture", default=None)


class AuditLogRetrieveResponse(BaseModel):
    action: Literal[
        "UserLogin",
        "PasswordChanged",
        "EmailChangeRequested",
        "EmailChanged",
        "UserRegistered",
        "UserAccountDeleted",
        "WorkspaceCreated",
        "WorkspaceDeleted",
        "MemberInvited",
        "MemberRemoved",
        "MemberRoleChanged",
        "InviteAccepted",
        "TeamSettingsUpdated",
        "InviteLinkToggled",
        "UserGroupCreated",
        "UserGroupDeleted",
        "UserGroupMemberAdded",
        "UserGroupMemberRemoved",
        "SSOLogin",
        "SSOUserProvisioned",
        "SSOConfigCreated",
        "SSOUserAutoAddedToTeam",
        "SSODomainRegistrationCloned",
        "AssetCreated",
        "AssetUpdated",
        "AssetDeleted",
        "AssetDownloaded",
        "AssetShared",
        "AssetUnshared",
        "PermissionGranted",
        "PermissionUpdated",
        "PermissionRevoked",
        "PermissionAccepted",
        "SubscriptionCancelled",
        "SubscriptionPlanSwitched",
        "CreditsTransferred",
        "SeatsTransferred",
        "SessionShared",
        "SessionUnshared",
        "VideoProjectShared",
        "VideoProjectUnshared",
        "BrandKitShared",
        "BrandKitUnshared",
        "AgentCustomSkillCreated",
        "AgentCustomSkillDeleted",
        "AgentCustomSkillShared",
        "AgentCustomSkillUnshared",
        "AgentSessionShared",
        "AgentSessionUnshared",
        "AgentConnectorLinkTokenCreated",
        "AgentConnectorConnected",
        "AgentConnectorDisconnected",
        "AgentConnectorAssetExported",
        "AgentConnectorSessionEnabled",
        "AgentConnectorSessionDisabled",
        "GenerationCreated",
        "AccountLinkCreated",
        "AccountLinkDeleted",
        "OrganizationSettingsUpdated",
        "OrganizationDisabledModelsUpdated",
        "WorkspaceCountryLockUpdated",
        "WorkspaceTagCreated",
        "WorkspaceTagUpdated",
        "WorkspaceTagDeleted",
        "WorkspaceTagAssigned",
        "WorkspaceTagUnassigned",
        "MeteredBillingConfigUpdated",
        "MeteredBillingRefillTriggered",
        "MeteredBillingRetryTriggered",
        "EnterpriseSpendCapEnforcementUpdated",
    ]
    """The action performed."""

    actor_deleted: bool = FieldInfo(alias="actorDeleted")
    """Whether the acting user has since been deleted."""

    actor_email: Optional[str] = FieldInfo(alias="actorEmail", default=None)
    """Email of the user who performed the action."""

    actor_username: Optional[str] = FieldInfo(alias="actorUsername", default=None)
    """Username of the user who performed the action."""

    client_ip_address: str = FieldInfo(alias="clientIpAddress")
    """IP address of the client that performed the action."""

    event_id: str = FieldInfo(alias="eventId")
    """Unique identifier of the entry."""

    metadata: Metadata
    """Action-specific details."""

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)
    """Request ID for correlation with other logs."""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """ID of the affected resource, if any."""

    resource_type: Optional[str] = FieldInfo(alias="resourceType", default=None)
    """Type of the affected resource, if any.

    Currently one of `account_link`, `agent_custom_skill`, `asset`, `brand_kit`,
    `generation`, `invite_link`, `membership`, `organization`, `permission`,
    `promotion`, `session`, `shared_asset`, `sso_config`, `sso_domain_registration`,
    `subscription`, `team_settings`, `user`, `user_group`, `video_project`,
    `workspace`, or `workspace_tag`. New types may be added over time, so treat this
    as an open set.
    """

    timestamp: datetime
    """When the action occurred."""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User-Agent header of the client request."""

    workspace_id: int = FieldInfo(alias="workspaceId")
    """ID of the owning workspace."""

    workspace_name: str = FieldInfo(alias="workspaceName")
    """Name of the owning workspace."""
