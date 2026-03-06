# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AvatarListResponse",
    "Processing",
    "ProcessingVoice",
    "ProcessingVoiceRunwayLivePreset",
    "ProcessingVoiceCustom",
    "Ready",
    "ReadyVoice",
    "ReadyVoiceRunwayLivePreset",
    "ReadyVoiceCustom",
    "Failed",
    "FailedVoice",
    "FailedVoiceRunwayLivePreset",
    "FailedVoiceCustom",
]


class ProcessingVoiceRunwayLivePreset(BaseModel):
    """A preset voice from the Runway API."""

    description: str
    """A brief description of the voice characteristics."""

    name: str
    """The display name of the voice."""

    preset_id: Literal[
        "victoria",
        "vincent",
        "clara",
        "drew",
        "skye",
        "max",
        "morgan",
        "felix",
        "mia",
        "marcus",
        "summer",
        "ruby",
        "aurora",
        "jasper",
        "leo",
        "adrian",
        "nina",
        "emma",
        "blake",
        "david",
        "maya",
        "nathan",
        "sam",
        "georgia",
        "petra",
        "adam",
        "zach",
        "violet",
        "roman",
        "luna",
    ] = FieldInfo(alias="presetId")
    """The preset voice identifier."""

    type: Literal["runway-live-preset"]


class ProcessingVoiceCustom(BaseModel):
    """A custom voice created via the Voices API."""

    id: str
    """The unique identifier of the custom voice."""

    deleted: bool
    """Whether the voice has been deleted.

    When true, name and description are omitted.
    """

    type: Literal["custom"]

    description: Optional[str] = None
    """A brief description of the voice characteristics."""

    name: Optional[str] = None
    """The display name of the voice."""


ProcessingVoice: TypeAlias = Annotated[
    Union[ProcessingVoiceRunwayLivePreset, ProcessingVoiceCustom], PropertyInfo(discriminator="type")
]


class Processing(BaseModel):
    """An avatar that is still being processed."""

    id: str
    """The unique identifier of the avatar."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the avatar was created."""

    document_ids: List[str] = FieldInfo(alias="documentIds")
    """IDs of knowledge documents attached to this avatar."""

    name: str
    """The character name for the avatar."""

    personality: str
    """System prompt defining how the avatar should behave in conversations."""

    processed_image_uri: Optional[str] = FieldInfo(alias="processedImageUri", default=None)
    """A URI pointing to a low-resolution preview of the processed reference image."""

    reference_image_uri: Optional[str] = FieldInfo(alias="referenceImageUri", default=None)
    """A URI pointing to a low-resolution preview of the avatar's reference image."""

    start_script: Optional[str] = FieldInfo(alias="startScript", default=None)
    """
    Opening message that the avatar will say when a session starts, or null if not
    set.
    """

    status: Literal["PROCESSING"]

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the avatar was last updated."""

    voice: ProcessingVoice
    """The voice configured for this avatar."""


class ReadyVoiceRunwayLivePreset(BaseModel):
    """A preset voice from the Runway API."""

    description: str
    """A brief description of the voice characteristics."""

    name: str
    """The display name of the voice."""

    preset_id: Literal[
        "victoria",
        "vincent",
        "clara",
        "drew",
        "skye",
        "max",
        "morgan",
        "felix",
        "mia",
        "marcus",
        "summer",
        "ruby",
        "aurora",
        "jasper",
        "leo",
        "adrian",
        "nina",
        "emma",
        "blake",
        "david",
        "maya",
        "nathan",
        "sam",
        "georgia",
        "petra",
        "adam",
        "zach",
        "violet",
        "roman",
        "luna",
    ] = FieldInfo(alias="presetId")
    """The preset voice identifier."""

    type: Literal["runway-live-preset"]


class ReadyVoiceCustom(BaseModel):
    """A custom voice created via the Voices API."""

    id: str
    """The unique identifier of the custom voice."""

    deleted: bool
    """Whether the voice has been deleted.

    When true, name and description are omitted.
    """

    type: Literal["custom"]

    description: Optional[str] = None
    """A brief description of the voice characteristics."""

    name: Optional[str] = None
    """The display name of the voice."""


ReadyVoice: TypeAlias = Annotated[
    Union[ReadyVoiceRunwayLivePreset, ReadyVoiceCustom], PropertyInfo(discriminator="type")
]


class Ready(BaseModel):
    """An avatar that is ready for use in sessions."""

    id: str
    """The unique identifier of the avatar."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the avatar was created."""

    document_ids: List[str] = FieldInfo(alias="documentIds")
    """IDs of knowledge documents attached to this avatar."""

    name: str
    """The character name for the avatar."""

    personality: str
    """System prompt defining how the avatar should behave in conversations."""

    processed_image_uri: Optional[str] = FieldInfo(alias="processedImageUri", default=None)
    """A URI pointing to a low-resolution preview of the processed reference image."""

    reference_image_uri: Optional[str] = FieldInfo(alias="referenceImageUri", default=None)
    """A URI pointing to a low-resolution preview of the avatar's reference image."""

    start_script: Optional[str] = FieldInfo(alias="startScript", default=None)
    """
    Opening message that the avatar will say when a session starts, or null if not
    set.
    """

    status: Literal["READY"]

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the avatar was last updated."""

    voice: ReadyVoice
    """The voice configured for this avatar."""


class FailedVoiceRunwayLivePreset(BaseModel):
    """A preset voice from the Runway API."""

    description: str
    """A brief description of the voice characteristics."""

    name: str
    """The display name of the voice."""

    preset_id: Literal[
        "victoria",
        "vincent",
        "clara",
        "drew",
        "skye",
        "max",
        "morgan",
        "felix",
        "mia",
        "marcus",
        "summer",
        "ruby",
        "aurora",
        "jasper",
        "leo",
        "adrian",
        "nina",
        "emma",
        "blake",
        "david",
        "maya",
        "nathan",
        "sam",
        "georgia",
        "petra",
        "adam",
        "zach",
        "violet",
        "roman",
        "luna",
    ] = FieldInfo(alias="presetId")
    """The preset voice identifier."""

    type: Literal["runway-live-preset"]


class FailedVoiceCustom(BaseModel):
    """A custom voice created via the Voices API."""

    id: str
    """The unique identifier of the custom voice."""

    deleted: bool
    """Whether the voice has been deleted.

    When true, name and description are omitted.
    """

    type: Literal["custom"]

    description: Optional[str] = None
    """A brief description of the voice characteristics."""

    name: Optional[str] = None
    """The display name of the voice."""


FailedVoice: TypeAlias = Annotated[
    Union[FailedVoiceRunwayLivePreset, FailedVoiceCustom], PropertyInfo(discriminator="type")
]


class Failed(BaseModel):
    """An avatar that failed to finish processing."""

    id: str
    """The unique identifier of the avatar."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the avatar was created."""

    document_ids: List[str] = FieldInfo(alias="documentIds")
    """IDs of knowledge documents attached to this avatar."""

    failure_reason: str = FieldInfo(alias="failureReason")
    """A human-readable error message.

    This value is not stable and should not be matched against programmatically.
    """

    name: str
    """The character name for the avatar."""

    personality: str
    """System prompt defining how the avatar should behave in conversations."""

    processed_image_uri: Optional[str] = FieldInfo(alias="processedImageUri", default=None)
    """A URI pointing to a low-resolution preview of the processed reference image."""

    reference_image_uri: Optional[str] = FieldInfo(alias="referenceImageUri", default=None)
    """A URI pointing to a low-resolution preview of the avatar's reference image."""

    start_script: Optional[str] = FieldInfo(alias="startScript", default=None)
    """
    Opening message that the avatar will say when a session starts, or null if not
    set.
    """

    status: Literal["FAILED"]

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the avatar was last updated."""

    voice: FailedVoice
    """The voice configured for this avatar."""


AvatarListResponse: TypeAlias = Annotated[Union[Processing, Ready, Failed], PropertyInfo(discriminator="status")]
