# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["RealtimeSessionRetrieveResponse", "NotReady", "Ready", "Running", "Completed", "Failed", "Cancelled"]


class NotReady(BaseModel):
    """A session that is being provisioned."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    status: Literal["NOT_READY"]

    queued: Optional[bool] = None
    """When true, the session is waiting in a queue for available capacity.

    When false or absent, the session is actively being provisioned.
    """


class Ready(BaseModel):
    """A session that is ready to connect."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the session credentials expire."""

    session_key: str = FieldInfo(alias="sessionKey")
    """Session key for authenticating the /consume endpoint. Use as Bearer token."""

    status: Literal["READY"]


class Running(BaseModel):
    """A session with an active WebRTC connection."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    status: Literal["RUNNING"]


class Completed(BaseModel):
    """A session that ended normally."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    duration: int
    """The session duration in seconds."""

    status: Literal["COMPLETED"]


class Failed(BaseModel):
    """A session that encountered an error."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    failure: str
    """A human-readable error message.

    This value is not stable and should not be matched against programmatically.
    """

    failure_code: str = FieldInfo(alias="failureCode")
    """A stable, machine-readable error code.

    See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
    """

    status: Literal["FAILED"]


class Cancelled(BaseModel):
    """A session that was explicitly cancelled."""

    id: str
    """The realtime session ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the session was created."""

    status: Literal["CANCELLED"]


RealtimeSessionRetrieveResponse: TypeAlias = Annotated[
    Union[NotReady, Ready, Running, Completed, Failed, Cancelled], PropertyInfo(discriminator="status")
]
