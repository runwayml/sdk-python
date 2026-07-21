# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RouterCreateResponse", "Settings", "SettingsMaxCreditsPerGeneration", "SettingsModels"]


class SettingsMaxCreditsPerGeneration(BaseModel):
    """Optional per-modality hard caps on credits for one generation.

    Models whose estimated cost for that modality exceeds the cap are excluded.
    """

    audio: Optional[int] = None

    image: Optional[int] = None

    video: Optional[int] = None


class SettingsModels(BaseModel):
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video model name (unknown ids are rejected on create/update).
    """

    ids: List[str]

    mode: Literal["allow_new_except", "allowlist_only"]


class Settings(BaseModel):
    schema_version: Literal[1] = FieldInfo(alias="schemaVersion")
    """Settings JSON schema version used when this snapshot was written."""

    max_credits_per_generation: Optional[SettingsMaxCreditsPerGeneration] = FieldInfo(
        alias="maxCreditsPerGeneration", default=None
    )
    """Optional per-modality hard caps on credits for one generation.

    Models whose estimated cost for that modality exceeds the cap are excluded.
    """

    models: Optional[SettingsModels] = None
    """
    When mode is allow_new_except, ids are excluded; when allowlist_only, ids are
    the only allowed values. Each id must be a known public video model name
    (unknown ids are rejected on create/update).
    """

    optimize_for: Optional[Literal["cost", "latency", "quality"]] = FieldInfo(alias="optimizeFor", default=None)
    """Soft preference among eligible models: cost, latency, or quality."""


class RouterCreateResponse(BaseModel):
    id: str
    """The Model Router's primary key ID (UUID).

    Use it to manage this router via the API; use the slug to reference the router
    in generation requests.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the Model Router was created."""

    description: Optional[str] = None
    """An optional Model Router description."""

    name: str
    """Human-friendly Model Router display name shown in the dev portal.

    Mutable, and not used to reference the router in requests.
    """

    settings: Settings

    slug: str
    """
    Immutable slug used to reference this Model Router in generation requests (for
    example, production-video). Unique within the API project. The UUID id remains
    the canonical management identifier.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the Model Router was last updated."""

    version: int
    """Current settings version.

    Increments when settings change; name and description updates do not create a
    new version.
    """
