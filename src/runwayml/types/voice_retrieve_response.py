# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["VoiceRetrieveResponse", "Processing", "Ready", "Failed"]


class Processing(BaseModel):
    """A voice that is still being processed."""

    id: str
    """The unique identifier of the voice."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the voice was created."""

    description: Optional[str] = None
    """A description of the voice, or null if not set."""

    name: str
    """The name of the voice."""

    status: Literal["PROCESSING"]


class Ready(BaseModel):
    """A voice that is ready for use."""

    id: str
    """The unique identifier of the voice."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the voice was created."""

    description: Optional[str] = None
    """A description of the voice, or null if not set."""

    name: str
    """The name of the voice."""

    preview_url: Optional[str] = FieldInfo(alias="previewUrl", default=None)
    """
    A signed URL to an MP3 audio sample of the voice, or null if no sample is
    available.
    """

    status: Literal["READY"]


class Failed(BaseModel):
    """A voice that failed to finish processing."""

    id: str
    """The unique identifier of the voice."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the voice was created."""

    description: Optional[str] = None
    """A description of the voice, or null if not set."""

    failure_reason: str = FieldInfo(alias="failureReason")
    """A human-readable error message.

    This value is not stable and should not be matched against programmatically.
    """

    name: str
    """The name of the voice."""

    status: Literal["FAILED"]


VoiceRetrieveResponse: TypeAlias = Annotated[Union[Processing, Ready, Failed], PropertyInfo(discriminator="status")]
