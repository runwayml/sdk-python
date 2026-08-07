# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RouterCreateParams", "Settings", "SettingsFallback", "SettingsMaxCreditsPerGeneration", "SettingsModels"]


class RouterCreateParams(TypedDict, total=False):
    slug: Required[str]
    """
    Immutable slug used to reference this Model Router in generation requests (for
    example, production-video). Unique within the API project. The UUID id remains
    the canonical management identifier.
    """

    description: str
    """An optional Model Router description."""

    name: str
    """Optional human-readable display name for this router.

    Defaults to the slug when omitted.
    """

    settings: Settings
    """Model Router routing preferences.

    Defaults to cost-optimized allow-all when omitted. Modality is implied by the
    generate endpoint used with this Model Router.
    """


class SettingsFallback(TypedDict, total=False):
    """
    Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    """

    on_capacity: Annotated[bool, PropertyInfo(alias="onCapacity")]
    """
    When true, if the account is at its concurrency limit on the preferred model,
    routing skips it and picks the next-best eligible model instead of queueing. If
    every eligible model is at its limit, the original best-ranked model is used and
    the task queues as usual.
    """


class SettingsMaxCreditsPerGeneration(TypedDict, total=False):
    """Optional per-modality credit caps, applied per generated output.

    Models whose estimated per-output cost exceeds the cap are excluded.
    """

    audio: int

    image: int

    video: int


class SettingsModels(TypedDict, total=False):
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video or image model name (unknown ids are rejected on create/update).
    """

    ids: Required[SequenceNotStr[str]]

    mode: Required[Literal["allow_new_except", "allowlist_only"]]


class Settings(TypedDict, total=False):
    """Model Router routing preferences.

    Defaults to cost-optimized allow-all when omitted. Modality is implied by the generate endpoint used with this Model Router.
    """

    fallback: SettingsFallback
    """
    Opt-in behavior for what routing should do when the preferred model cannot start
    immediately.
    """

    max_credits_per_generation: Annotated[
        SettingsMaxCreditsPerGeneration, PropertyInfo(alias="maxCreditsPerGeneration")
    ]
    """Optional per-modality credit caps, applied per generated output.

    Models whose estimated per-output cost exceeds the cap are excluded.
    """

    models: SettingsModels
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are
    the only allowed values. Each id must be a known public video or image model
    name (unknown ids are rejected on create/update).
    """

    optimize_for: Annotated[Literal["cost", "latency", "quality"], PropertyInfo(alias="optimizeFor")]
    """Soft preference among eligible models: cost, latency, or quality."""

    schema_version: Annotated[Literal[1], PropertyInfo(alias="schemaVersion")]
    """Settings JSON schema version.

    Omit on write to use the current version; responses and stored snapshots always
    include it.
    """
