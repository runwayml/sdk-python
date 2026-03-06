# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DocumentListResponse", "UsedBy"]


class UsedBy(BaseModel):
    id: str
    """The avatar ID."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to the avatar image, or null if not yet processed."""

    name: str
    """The avatar name."""


class DocumentListResponse(BaseModel):
    id: str
    """The unique identifier of the document."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the document was created."""

    name: str
    """The name of the document."""

    type: Literal["text", "file"]
    """The type of document."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the document was last updated."""

    used_by: List[UsedBy] = FieldInfo(alias="usedBy")
    """Avatars that use this document."""
