# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    actions: str
    """
    Restrict results to these audit log actions, as a comma-separated list of up to
    50 actions. Allowed values: `AgentArtifactCommentCreated`,
    `AgentArtifactCreated`, `AgentArtifactVersionSaved`,
    `AgentArtifactSessionAttached`, `AgentArtifactSessionDetached`, `UserLogin`,
    `PasswordChanged`, `EmailChangeRequested`, `EmailChanged`, `UserRegistered`,
    `UserAccountDeleted`, `WorkspaceCreated`, `WorkspaceDeleted`, `MemberInvited`,
    `MemberInviteReminderSent`, `MemberRemoved`, `MemberRoleChanged`,
    `InviteAccepted`, `MemberJoinedViaDomain`, `TeamSettingsUpdated`,
    `InviteLinkToggled`, `UserGroupCreated`, `UserGroupUpdated`, `UserGroupDeleted`,
    `UserGroupArchived`, `UserGroupRestored`, `UserGroupMemberAdded`,
    `UserGroupMemberRemoved`, `UserGroupCreditCapUpdated`,
    `UserGroupVisibilityUpdated`, `SSOLogin`, `SSOUserProvisioned`,
    `SSOConfigCreated`, `SSOUserAutoAddedToTeam`, `SSODomainRegistrationCloned`,
    `AssetCreated`, `AssetUpdated`, `AssetDeleted`, `AssetDownloaded`,
    `AssetShared`, `AssetUnshared`, `CommentCreated`, `CommentEdited`,
    `CommentDeleted`, `CommentAgentCallRun`, `CommentRemovedByModerator`,
    `CommentRestoredByModerator`, `CommentRemovalReasonChanged`,
    `PermissionGranted`, `PermissionUpdated`, `PermissionRevoked`,
    `PermissionAccepted`, `SubscriptionCancelled`,
    `SubscriptionReactivatedWithOffer`, `SubscriptionPlanSwitched`,
    `CreditsTransferred`, `SeatsTransferred`, `SessionShared`, `SessionUnshared`,
    `SessionMadePrivateByAdmin`, `VideoProjectShared`, `VideoProjectUnshared`,
    `BrandKitShared`, `BrandKitUnshared`, `AgentCustomSkillCreated`,
    `AgentCustomSkillDeleted`, `AgentCustomSkillShared`, `AgentCustomSkillUnshared`,
    `AgentSessionShared`, `AgentSessionUnshared`, `AgentConnectorLinkTokenCreated`,
    `AgentConnectorConnected`, `AgentConnectorDisconnected`,
    `AgentConnectorAssetExported`, `AgentConnectorSessionEnabled`,
    `AgentConnectorSessionDisabled`, `GenerationCreated`, `StudioSessionOpened`,
    `AppStudioAiRunOpened`, `AppStudioAppCreated`, `AppStudioAppPublished`,
    `AppStudioAppVisibilityChanged`, `AppStudioAppRenamed`, `AppStudioAppDeleted`,
    `AppStudioAppCoOwnerChanged`, `AppStudioAppSecretChanged`,
    `AppStudioAppRunwayAccessGranted`, `AppStudioAppRunwayAccessRevoked`,
    `AppStudioConnectorConnected`, `AppStudioConnectorDisconnected`,
    `AppStudioConnectorAppGranted`, `AppStudioConnectorAppRevoked`,
    `AppStudioConnectorPolicyChanged`, `AppStudioConnectorToolCalled`,
    `AccountLinkCreated`, `AccountLinkDeleted`, `AdConnectionAuthorizationStarted`,
    `AdConnectionConnected`, `AdAccountSelectionUpdated`, `AdAccountSyncRequested`,
    `AdConnectionDisconnected`, `AdWorkspaceOnboardingUpdated`,
    `AdCreativeReviewSubmitted`, `AdCreativeReviewCancelled`,
    `AdCreativeReviewDecided`, `AdCreativeApprovalRevoked`, `AdCreativeArchived`,
    `AdCreativeUnarchived`, `AdPublishBatchQueued`, `AdPublishBatchCancelled`,
    `AdPublishBatchRetried`, `AdStatusChanged`, `AdCampaignSetupDrafted`,
    `AdCampaignSetupDiscarded`, `AdCampaignSetupConfirmed`,
    `AdCampaignSetupCancelled`, `AdCampaignSetupRetried`,
    `OrganizationSettingsUpdated`, `OrganizationDisabledModelsUpdated`,
    `OrganizationAgentSandboxUpdated`, `OrganizationApiAccountReleased`,
    `OrganizationApiAccountMemberInvited`,
    `OrganizationApiAccountMemberRoleChanged`,
    `OrganizationApiAccountMemberRemoved`, `WorkspaceCountryLockUpdated`,
    `WorkspaceTagCreated`, `WorkspaceTagUpdated`, `WorkspaceTagDeleted`,
    `WorkspaceTagAssigned`, `WorkspaceTagUnassigned`, `MeteredBillingConfigUpdated`,
    `MeteredBillingRefillTriggered`, `MeteredBillingRetryTriggered`,
    `EnterpriseSpendCapEnforcementUpdated`, `OnboardingBonusGranted`,
    `PromotionCreditsGranted`, `AwsMarketplaceEnterpriseSubscriptionLinked`.
    """

    actor_emails: Annotated[str, PropertyInfo(alias="actorEmails")]
    """
    Restrict results to entries performed by the users with these emails, as a
    comma-separated list of up to 50 emails.
    """

    cursor: str
    """Cursor from a previous response for fetching the next page of results."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start of the time window (inclusive), ISO-8601 datetime."""

    limit: int
    """The maximum number of items to return per page."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Organization to report on.

    Optional when this API project is linked to a single organization; required when
    it is linked to more than one. If it is missing then, the 400 response lists the
    IDs and names of the linked organizations in `details.organizations`.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time window (exclusive), ISO-8601 datetime."""

    workspace_ids: Annotated[str, PropertyInfo(alias="workspaceIds")]
    """
    Restrict results to these workspace IDs, as a comma-separated list of up to 50
    IDs. Defaults to every workspace you administer in the organization.
    """
