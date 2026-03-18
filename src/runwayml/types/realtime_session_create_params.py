# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["RealtimeSessionCreateParams", "Avatar", "AvatarRunwayPreset", "AvatarCustom"]


class RealtimeSessionCreateParams(TypedDict, total=False):
    avatar: Required[Avatar]
    """The avatar configuration for the session."""

    model: Required[Literal["gwm1_avatars"]]
    """The realtime session model type."""

    max_duration: Annotated[int, PropertyInfo(alias="maxDuration")]
    """Maximum session duration in seconds."""

    personality: str
    """Override the avatar personality for this session.

    If not provided, uses the avatar default.
    """

    start_script: Annotated[str, PropertyInfo(alias="startScript")]
    """Override the avatar start script for this session.

    If not provided, uses the avatar default.
    """


class AvatarRunwayPreset(TypedDict, total=False):
    """A preset avatar from Runway."""

    preset_id: Required[
        Annotated[
            Literal[
                "game-character",
                "music-superstar",
                "game-character-man",
                "cat-character",
                "influencer",
                "tennis-coach",
                "human-resource",
                "fashion-designer",
                "cooking-teacher",
            ],
            PropertyInfo(alias="presetId"),
        ]
    ]
    """ID of a preset avatar."""

    type: Required[Literal["runway-preset"]]


class AvatarCustom(TypedDict, total=False):
    """A user-created avatar."""

    avatar_id: Required[Annotated[str, PropertyInfo(alias="avatarId")]]
    """ID of a user-created avatar."""

    type: Required[Literal["custom"]]


Avatar: TypeAlias = Union[AvatarRunwayPreset, AvatarCustom]
