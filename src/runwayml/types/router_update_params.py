# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RouterUpdateParams", "Settings", "SettingsFallback", "SettingsMaxCreditsPerGeneration", "SettingsModels"]


class RouterUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: str
    """Display name. The slug is immutable and cannot be changed after creation."""

    settings: Settings
    """Nested merge: omitted settings fields keep their current values.

    When models is present, omitted models.mode or models.ids are preserved (sending
    only optimizeFor does not clear the model allowlist or credit ceiling). Set
    maxCreditsPerGeneration, or one of its modalities, to null to remove those
    credit caps.
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
    """Per-modality credit caps to change, applied per generated output.

    Omitted modalities keep their current cap; null removes that cap.
    """

    audio: Optional[int]

    image: Optional[int]

    video: Optional[int]


class SettingsModels(TypedDict, total=False):
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video or image model name (unknown ids are rejected on create/update).
    """

    ids: Required[SequenceNotStr[str]]

    mode: Required[Literal["allow_new_except", "allowlist_only"]]


class Settings(TypedDict, total=False):
    """Nested merge: omitted settings fields keep their current values.

    When models is present, omitted models.mode or models.ids are preserved (sending only optimizeFor does not clear the model allowlist or credit ceiling). Set maxCreditsPerGeneration, or one of its modalities, to null to remove those credit caps.
    """

    fallback: SettingsFallback
    """
    Opt-in behavior for what routing should do when the preferred model cannot start
    immediately.
    """

    max_credits_per_generation: Annotated[
        Optional[SettingsMaxCreditsPerGeneration], PropertyInfo(alias="maxCreditsPerGeneration")
    ]
    """Per-modality credit caps to change, applied per generated output.

    Omitted modalities keep their current cap; null removes that cap.
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
