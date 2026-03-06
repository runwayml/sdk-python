# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AvatarUpdateParams", "Voice", "VoiceRunwayLivePreset", "VoiceCustom"]


class AvatarUpdateParams(TypedDict, total=False):
    document_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="documentIds")]
    """List of knowledge document IDs to attach to this avatar.

    Replaces all current attachments. Documents provide additional context during
    conversations.
    """

    image_processing: Annotated[Literal["optimize", "none"], PropertyInfo(alias="imageProcessing")]
    """Controls image preprocessing.

    `optimize` improves the image for better avatar results. `none` uses the image
    as-is; quality not guaranteed.
    """

    name: str
    """The character name for the avatar."""

    personality: str
    """System prompt defining how the avatar should behave in conversations."""

    reference_image: Annotated[str, PropertyInfo(alias="referenceImage")]
    """A HTTPS URL."""

    start_script: Annotated[Optional[str], PropertyInfo(alias="startScript")]
    """Optional opening message that the avatar will say when a session starts.

    Set to null to clear.
    """

    voice: Voice
    """The voice configuration for the avatar."""


class VoiceRunwayLivePreset(TypedDict, total=False):
    """A preset voice from the Runway API."""

    preset_id: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="presetId"),
        ]
    ]
    """The ID of a preset voice.

    Available voices: `victoria` (Victoria), `vincent` (Vincent), `clara` (Clara),
    `drew` (Drew), `skye` (Skye), `max` (Max), `morgan` (Morgan), `felix` (Felix),
    `mia` (Mia), `marcus` (Marcus), `summer` (Summer), `ruby` (Ruby), `aurora`
    (Aurora), `jasper` (Jasper), `leo` (Leo), `adrian` (Adrian), `nina` (Nina),
    `emma` (Emma), `blake` (Blake), `david` (David), `maya` (Maya), `nathan`
    (Nathan), `sam` (Sam), `georgia` (Georgia), `petra` (Petra), `adam` (Adam),
    `zach` (Zach), `violet` (Violet), `roman` (Roman), `luna` (Luna).
    """

    type: Required[Literal["runway-live-preset"]]


class VoiceCustom(TypedDict, total=False):
    """A custom voice created via the Voices API."""

    id: Required[str]
    """The ID of a custom voice created via the Voices API."""

    type: Required[Literal["custom"]]


Voice: TypeAlias = Union[VoiceRunwayLivePreset, VoiceCustom]
