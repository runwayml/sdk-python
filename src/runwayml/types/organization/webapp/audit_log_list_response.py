# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditLogListResponse", "Metadata"]


class Metadata(BaseModel):
    """Action-specific details."""

    accepted_by: Optional[str] = FieldInfo(alias="Accepted by", default=None)

    ad_account_id: Optional[str] = FieldInfo(alias="Ad account ID", default=None)

    ad_creative_id: Optional[str] = FieldInfo(alias="Ad creative ID", default=None)

    ad_level: Optional[str] = FieldInfo(alias="Ad level", default=None)

    ad_publish_batch_id: Optional[str] = FieldInfo(alias="Ad publish batch ID", default=None)

    ad_review_batch_id: Optional[str] = FieldInfo(alias="Ad review batch ID", default=None)

    ad_review_request_id: Optional[str] = FieldInfo(alias="Ad review request ID", default=None)

    ad_sync_end_date: Optional[str] = FieldInfo(alias="Ad sync end date", default=None)

    ad_sync_run_id: Optional[str] = FieldInfo(alias="Ad sync run ID", default=None)

    ad_sync_start_date: Optional[str] = FieldInfo(alias="Ad sync start date", default=None)

    added_member: Optional[str] = FieldInfo(alias="Added member", default=None)

    ads_created_as: Optional[str] = FieldInfo(alias="Ads created as", default=None)

    ads_onboarding_answers: Optional[List[str]] = FieldInfo(alias="Ads onboarding answers", default=None)

    ads_onboarding_completed: Optional[bool] = FieldInfo(alias="Ads onboarding completed", default=None)

    agent_session_id: Optional[str] = FieldInfo(alias="Agent session ID", default=None)

    agent_tagged: Optional[bool] = FieldInfo(alias="Agent tagged", default=None)

    amount: Optional[float] = FieldInfo(alias="Amount", default=None)

    amount_received: Optional[float] = FieldInfo(alias="Amount received", default=None)

    anonymous: Optional[bool] = FieldInfo(alias="Anonymous", default=None)

    api_account: Optional[str] = FieldInfo(alias="API account", default=None)

    api_project_id: Optional[str] = FieldInfo(alias="API project ID", default=None)

    app_studio_app: Optional[str] = FieldInfo(alias="App Studio app", default=None)

    app_studio_app_id: Optional[str] = FieldInfo(alias="App Studio app ID", default=None)

    app_studio_deploy: Optional[str] = FieldInfo(alias="App Studio deploy", default=None)

    app_studio_session: Optional[str] = FieldInfo(alias="App Studio session", default=None)

    application: Optional[str] = FieldInfo(alias="Application", default=None)

    asset_name: Optional[str] = FieldInfo(alias="Asset name", default=None)

    asset_type: Optional[str] = FieldInfo(alias="Asset type", default=None)

    automatic: Optional[bool] = FieldInfo(alias="Automatic", default=None)

    aws_license: Optional[str] = FieldInfo(alias="AWS license", default=None)

    brand_kit_id: Optional[str] = FieldInfo(alias="Brand kit ID", default=None)

    cancels_at_period_end: Optional[bool] = FieldInfo(alias="Cancels at period end", default=None)

    comment_id: Optional[str] = FieldInfo(alias="Comment ID", default=None)

    comment_target_id: Optional[str] = FieldInfo(alias="Comment target ID", default=None)

    comment_target_type: Optional[str] = FieldInfo(alias="Comment target type", default=None)

    comment_text: Optional[str] = FieldInfo(alias="Comment text", default=None)

    connector: Optional[str] = FieldInfo(alias="Connector", default=None)

    creatives_cancelled: Optional[float] = FieldInfo(alias="Creatives cancelled", default=None)

    creatives_queued: Optional[float] = FieldInfo(alias="Creatives queued", default=None)

    creatives_retried: Optional[float] = FieldInfo(alias="Creatives retried", default=None)

    credits_used: Optional[float] = FieldInfo(alias="Credits used", default=None)

    default_project_discoverability: Optional[str] = FieldInfo(alias="Default project discoverability", default=None)

    default_task_name_template: Optional[str] = FieldInfo(alias="Default task name template", default=None)

    destination_category_id: Optional[str] = FieldInfo(alias="Destination category ID", default=None)

    direction: Optional[str] = FieldInfo(alias="Direction", default=None)

    downloaded_by_owner: Optional[bool] = FieldInfo(alias="Downloaded by owner", default=None)

    email_domain: Optional[str] = FieldInfo(alias="Email domain", default=None)

    enabled: Optional[bool] = FieldInfo(alias="Enabled", default=None)

    error_code: Optional[str] = FieldInfo(alias="Error code", default=None)

    filename: Optional[str] = FieldInfo(alias="Filename", default=None)

    from_workspace_id: Optional[float] = FieldInfo(alias="From workspace ID", default=None)

    group_name: Optional[str] = FieldInfo(alias="Group name", default=None)

    hard_spend_cap: Optional[bool] = FieldInfo(alias="Hard spend cap", default=None)

    into_a_new_test_ad_set: Optional[bool] = FieldInfo(alias="Into a new test ad set", default=None)

    invited_member: Optional[str] = FieldInfo(alias="Invited member", default=None)

    join_policy: Optional[str] = FieldInfo(alias="Join policy", default=None)

    language_model_or_provider: Optional[str] = FieldInfo(alias="Language model or provider", default=None)

    link_type: Optional[str] = FieldInfo(alias="Link type", default=None)

    login_method: Optional[str] = FieldInfo(alias="Login method", default=None)

    media_included: Optional[bool] = FieldInfo(alias="Media included", default=None)

    member_email: Optional[str] = FieldInfo(alias="Member email", default=None)

    mentions: Optional[float] = FieldInfo(alias="Mentions", default=None)

    method: Optional[str] = FieldInfo(alias="Method", default=None)

    model: Optional[str] = FieldInfo(alias="Model", default=None)

    new_email: Optional[str] = FieldInfo(alias="New email", default=None)

    new_role: Optional[str] = FieldInfo(alias="New role", default=None)

    new_text: Optional[str] = FieldInfo(alias="New text", default=None)

    new_user: Optional[bool] = FieldInfo(alias="New User", default=None)

    new_value: Union[str, float, bool, Dict[str, bool], None] = FieldInfo(alias="New value", default=None)

    operation: Optional[str] = FieldInfo(alias="Operation", default=None)

    organization: Optional[str] = FieldInfo(alias="Organization", default=None)

    outcome: Optional[str] = FieldInfo(alias="Outcome", default=None)

    plan: Optional[str] = FieldInfo(alias="Plan", default=None)

    platform: Optional[str] = FieldInfo(alias="Platform", default=None)

    platform_ad_account_id: Optional[str] = FieldInfo(alias="Platform ad account ID", default=None)

    platform_object_id: Optional[str] = FieldInfo(alias="Platform object ID", default=None)

    previous_email: Optional[str] = FieldInfo(alias="Previous email", default=None)

    previous_project_credit_cap: Optional[float] = FieldInfo(alias="Previous project credit cap", default=None)

    previous_role: Optional[str] = FieldInfo(alias="Previous role", default=None)

    previous_text: Optional[str] = FieldInfo(alias="Previous text", default=None)

    previous_value: Union[str, float, bool, Dict[str, bool], None] = FieldInfo(alias="Previous value", default=None)

    project_credit_cap: Optional[float] = FieldInfo(alias="Project credit cap", default=None)

    project_id: Optional[str] = FieldInfo(alias="Project ID", default=None)

    provider: Optional[str] = FieldInfo(alias="Provider", default=None)

    reason: Optional[str] = FieldInfo(alias="Reason", default=None)

    recharge_amount_usd_cents: Optional[float] = FieldInfo(alias="Recharge amount (USD cents)", default=None)

    recharge_below_credits: Optional[float] = FieldInfo(alias="Recharge below (credits)", default=None)

    removed_member: Optional[str] = FieldInfo(alias="Removed member", default=None)

    requested_via: Optional[List[str]] = FieldInfo(alias="Requested via", default=None)

    result_metric_id: Optional[str] = FieldInfo(alias="Result metric ID", default=None)

    review_decision: Optional[str] = FieldInfo(alias="Review decision", default=None)

    role: Optional[str] = FieldInfo(alias="Role", default=None)

    root_asset_id: Optional[str] = FieldInfo(alias="Root asset ID", default=None)

    secret_name: Optional[str] = FieldInfo(alias="Secret name", default=None)

    selected: Optional[bool] = FieldInfo(alias="Selected", default=None)

    setting: Optional[str] = FieldInfo(alias="Setting", default=None)

    shared_in_project: Optional[str] = FieldInfo(alias="Shared in project", default=None)

    shared_with_projects: Optional[List[str]] = FieldInfo(alias="Shared with projects", default=None)

    shared_with_workspace: Optional[bool] = FieldInfo(alias="Shared with workspace", default=None)

    source: Optional[str] = FieldInfo(alias="Source", default=None)

    source_application: Optional[str] = FieldInfo(alias="Source application", default=None)

    source_category_id: Optional[str] = FieldInfo(alias="Source category ID", default=None)

    spend_cap: Optional[float] = FieldInfo(alias="Spend cap", default=None)

    spend_cap_usd_cents: Optional[float] = FieldInfo(alias="Spend cap (USD cents)", default=None)

    spend_cap_change: Optional[float] = FieldInfo(alias="Spend cap change", default=None)

    status_after: Optional[str] = FieldInfo(alias="Status after", default=None)

    status_before: Optional[str] = FieldInfo(alias="Status before", default=None)

    submitted_via: Optional[str] = FieldInfo(alias="Submitted via", default=None)

    tag_color: Optional[str] = FieldInfo(alias="Tag color", default=None)

    tag_name: Optional[str] = FieldInfo(alias="Tag name", default=None)

    target_member: Optional[str] = FieldInfo(alias="Target member", default=None)

    task_id: Optional[str] = FieldInfo(alias="Task ID", default=None)

    to_workspace_id: Optional[float] = FieldInfo(alias="To workspace ID", default=None)

    tool: Optional[str] = FieldInfo(alias="Tool", default=None)

    updated_fields: Optional[List[str]] = FieldInfo(alias="Updated fields", default=None)

    via_public_api: Optional[bool] = FieldInfo(alias="Via public API", default=None)

    watermarked: Optional[bool] = FieldInfo(alias="Watermarked", default=None)

    workspace: Optional[str] = FieldInfo(alias="Workspace", default=None)

    workspace_description: Optional[str] = FieldInfo(alias="Workspace description", default=None)

    workspace_id: Optional[float] = FieldInfo(alias="Workspace ID", default=None)

    workspace_name: Optional[str] = FieldInfo(alias="Workspace name", default=None)

    workspace_picture: Optional[str] = FieldInfo(alias="Workspace picture", default=None)


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
        "MemberInviteReminderSent",
        "MemberRemoved",
        "MemberRoleChanged",
        "InviteAccepted",
        "MemberJoinedViaDomain",
        "TeamSettingsUpdated",
        "InviteLinkToggled",
        "UserGroupCreated",
        "UserGroupUpdated",
        "UserGroupDeleted",
        "UserGroupArchived",
        "UserGroupRestored",
        "UserGroupMemberAdded",
        "UserGroupMemberRemoved",
        "UserGroupCreditCapUpdated",
        "UserGroupVisibilityUpdated",
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
        "CommentCreated",
        "CommentEdited",
        "CommentDeleted",
        "CommentAgentCallRun",
        "CommentRemovedByModerator",
        "CommentRestoredByModerator",
        "CommentRemovalReasonChanged",
        "PermissionGranted",
        "PermissionUpdated",
        "PermissionRevoked",
        "PermissionAccepted",
        "SubscriptionCancelled",
        "SubscriptionReactivatedWithOffer",
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
        "StudioSessionOpened",
        "AppStudioAiRunOpened",
        "AppStudioAppCreated",
        "AppStudioAppPublished",
        "AppStudioAppVisibilityChanged",
        "AppStudioAppRenamed",
        "AppStudioAppDeleted",
        "AppStudioAppCoOwnerChanged",
        "AppStudioAppSecretChanged",
        "AppStudioAppRunwayAccessGranted",
        "AppStudioAppRunwayAccessRevoked",
        "AccountLinkCreated",
        "AccountLinkDeleted",
        "AdConnectionAuthorizationStarted",
        "AdConnectionConnected",
        "AdAccountSelectionUpdated",
        "AdAccountSyncRequested",
        "AdConnectionDisconnected",
        "AdWorkspaceOnboardingUpdated",
        "AdCreativeReviewSubmitted",
        "AdCreativeReviewCancelled",
        "AdCreativeReviewDecided",
        "AdCreativeApprovalRevoked",
        "AdCreativeArchived",
        "AdCreativeUnarchived",
        "AdPublishBatchQueued",
        "AdPublishBatchCancelled",
        "AdPublishBatchRetried",
        "AdStatusChanged",
        "OrganizationSettingsUpdated",
        "OrganizationDisabledModelsUpdated",
        "OrganizationAgentSandboxUpdated",
        "OrganizationApiAccountReleased",
        "OrganizationApiAccountMemberInvited",
        "OrganizationApiAccountMemberRoleChanged",
        "OrganizationApiAccountMemberRemoved",
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
        "OnboardingBonusGranted",
        "AwsMarketplaceEnterpriseSubscriptionLinked",
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

    metadata: Metadata
    """Action-specific details."""

    timestamp: datetime
    """When the action occurred."""

    workspace_id: int = FieldInfo(alias="workspaceId")
    """ID of the owning workspace."""

    workspace_name: str = FieldInfo(alias="workspaceName")
    """Name of the owning workspace."""
