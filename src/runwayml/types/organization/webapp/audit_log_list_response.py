# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditLogListResponse"]


class AuditLogListResponse(BaseModel):
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

    event_id: str = FieldInfo(alias="eventId")
    """Unique identifier of the entry."""

    timestamp: datetime
    """When the action occurred."""

    workspace_id: int = FieldInfo(alias="workspaceId")
    """ID of the owning workspace."""

    workspace_name: str = FieldInfo(alias="workspaceName")
    """Name of the owning workspace."""
