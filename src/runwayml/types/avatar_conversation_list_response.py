# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["AvatarConversationListResponse", "Avatar", "AvatarRunwayPreset", "AvatarCustom"]


class AvatarRunwayPreset(BaseModel):
    """A preset avatar."""

    name: str
    """The preset avatar's display name (e.g. "Mina")."""

    preset_id: str = FieldInfo(alias="presetId")
    """The preset avatar ID."""

    type: Literal["runway-preset"]


class AvatarCustom(BaseModel):
    """A custom avatar created by the user."""

    id: Optional[str] = None
    """The custom avatar ID, or null if deleted."""

    name: Optional[str] = None
    """The avatar's configured name, or null if unavailable."""

    type: Literal["custom"]


Avatar: TypeAlias = Annotated[Union[AvatarRunwayPreset, AvatarCustom, None], PropertyInfo(discriminator="type")]


class AvatarConversationListResponse(BaseModel):
    """Summary of a conversation for list responses."""

    id: str
    """Unique conversation identifier.

    This is the same value as the realtime session ID for the call.
    """

    avatar: Optional[Avatar] = None
    """The avatar used in this conversation."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the conversation was created."""

    duration: Optional[int] = None
    """Duration of the conversation in seconds, or null if not started."""

    has_tools: bool = FieldInfo(alias="hasTools")
    """Whether tools were configured for this conversation session."""

    name: str
    """Conversation name (auto-generated or user-provided)."""

    status: Literal["in_progress", "ended", "failed"]
    """The status of the conversation.

    `in_progress` means the session is active, `ended` means it completed
    successfully, `failed` means it ended due to an error.
    """
