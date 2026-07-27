# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeprecatedLivekitParam"]


class DeprecatedLivekitParam(TypedDict, total=False):
    """Use integration with type "livekit" instead."""

    token: Required[str]
    """
    LiveKit access token granting the avatar worker publish rights in the external
    room.
    """

    room_name: Required[Annotated[str, PropertyInfo(alias="roomName")]]
    """Name of the external LiveKit room."""

    url: Required[str]
    """WebSocket URL of the external LiveKit server the avatar worker should join."""

    agent_identity: Annotated[str, PropertyInfo(alias="agentIdentity")]
    """The participant identity of the customer agent already in the room.

    When provided, the avatar worker trusts audio published by this identity.
    """
