# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SpeechToSpeechCreateParams", "Media", "MediaAudio", "MediaVideo", "Voice"]


class SpeechToSpeechCreateParams(TypedDict, total=False):
    media: Required[Media]

    model: Required[Literal["eleven_multilingual_sts_v2"]]

    voice: Required[Voice]
    """The voice to use for the generated speech."""

    remove_background_noise: Annotated[bool, PropertyInfo(alias="removeBackgroundNoise")]


class MediaAudio(TypedDict, total=False):
    type: Required[Literal["audio"]]

    uri: Required[str]
    """A data URI containing encoded audio."""


class MediaVideo(TypedDict, total=False):
    type: Required[Literal["video"]]

    uri: Required[str]
    """A data URI containing an encoded video."""


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
