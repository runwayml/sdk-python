# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RouterUpdateParams", "Settings", "SettingsMaxCreditsPerGeneration", "SettingsModels"]


class RouterUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: str
    """Display name. The slug is immutable and cannot be changed after creation."""

    settings: Settings
    """Nested merge: omitted settings fields keep their current values.

    When models is present, omitted models.mode or models.ids are preserved (sending
    only optimizeFor does not clear the model allowlist or credit ceiling).
    """


class SettingsMaxCreditsPerGeneration(TypedDict, total=False):
    """Optional per-modality hard caps on credits for one generation.

    Models whose estimated cost for that modality exceeds the cap are excluded.
    """

    audio: int

    image: int

    video: int


class SettingsModels(TypedDict, total=False):
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video model name (unknown ids are rejected on create/update).
    """

    ids: Required[SequenceNotStr[str]]

    mode: Required[Literal["allow_new_except", "allowlist_only"]]


class Settings(TypedDict, total=False):
    """Nested merge: omitted settings fields keep their current values.

    When models is present, omitted models.mode or models.ids are preserved (sending only optimizeFor does not clear the model allowlist or credit ceiling).
    """

    max_credits_per_generation: Annotated[
        SettingsMaxCreditsPerGeneration, PropertyInfo(alias="maxCreditsPerGeneration")
    ]
    """Optional per-modality hard caps on credits for one generation.

    Models whose estimated cost for that modality exceeds the cap are excluded.
    """

    models: SettingsModels
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are
    the only allowed values. Each id must be a known public video model name
    (unknown ids are rejected on create/update).
    """

    optimize_for: Annotated[Literal["cost", "latency", "quality"], PropertyInfo(alias="optimizeFor")]
    """Soft preference among eligible models: cost, latency, or quality."""

    schema_version: Annotated[Literal[1], PropertyInfo(alias="schemaVersion")]
    """Settings JSON schema version.

    Omit on write to use the current version; responses and stored snapshots always
    include it.
    """
