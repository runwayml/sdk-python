# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SpeechToSpeechCreateParams", "Media", "MediaAudio", "MediaVideo", "Voice"]


class SpeechToSpeechCreateParams(TypedDict, total=False):
    media: Required[Media]
    """The media to use as a source for the dialogue for the generated speech."""

    model: Required[Literal["eleven_multilingual_sts_v2"]]

    voice: Required[Voice]
    """A voice preset from the RunwayML API."""

    remove_background_noise: Annotated[bool, PropertyInfo(alias="removeBackgroundNoise")]
    """Whether to remove background noise from the generated speech."""


class MediaAudio(TypedDict, total=False):
    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL."""


class MediaVideo(TypedDict, total=False):
    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL."""


Media: TypeAlias = Union[MediaAudio, MediaVideo]


class Voice(TypedDict, total=False):
    preset_id: Required[
        Annotated[
            Literal[
                "Maya",
                "Arjun",
                "Serene",
                "Bernard",
                "Billy",
                "Mark",
                "Clint",
                "Mabel",
                "Chad",
                "Leslie",
                "Eleanor",
                "Elias",
                "Elliot",
                "Grungle",
                "Brodie",
                "Sandra",
                "Kirk",
                "Kylie",
                "Lara",
                "Lisa",
                "Malachi",
                "Marlene",
                "Martin",
                "Miriam",
                "Monster",
                "Paula",
                "Pip",
                "Rusty",
                "Ragnar",
                "Xylar",
                "Maggie",
                "Jack",
                "Katie",
                "Noah",
                "James",
                "Rina",
                "Ella",
                "Mariah",
                "Frank",
                "Claudia",
                "Niki",
                "Vincent",
                "Kendrick",
                "Myrna",
                "Tom",
                "Wanda",
                "Benjamin",
                "Kiana",
                "Rachel",
            ],
            PropertyInfo(alias="presetId"),
        ]
    ]
    """The preset voice ID to use for the generated speech."""

    type: Required[Literal["runway-preset"]]
