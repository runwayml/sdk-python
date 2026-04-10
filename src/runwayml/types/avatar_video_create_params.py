# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AvatarVideoCreateParams",
    "Avatar",
    "AvatarRunwayPreset",
    "AvatarCustom",
    "Speech",
    "SpeechAudio",
    "SpeechText",
    "SpeechTextVoice",
    "SpeechTextVoicePreset",
    "SpeechTextVoiceCustom",
]


class AvatarVideoCreateParams(TypedDict, total=False):
    avatar: Required[Avatar]
    """The avatar configuration for the session."""

    model: Required[Literal["gwm1_avatars"]]
    """The model to use for avatar video generation."""

    speech: Required[Speech]
    """The speech source for avatar video generation.

    Either an audio file or text script.
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


class SpeechAudio(TypedDict, total=False):
    """Provide an audio file for the avatar to speak."""

    audio: Required[str]
    """A HTTPS URL."""

    type: Required[Literal["audio"]]


class SpeechTextVoicePreset(TypedDict, total=False):
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

    type: Required[Literal["preset"]]


class SpeechTextVoiceCustom(TypedDict, total=False):
    """A custom voice created via the Voices API."""

    id: Required[str]

    type: Required[Literal["custom"]]


SpeechTextVoice: TypeAlias = Union[SpeechTextVoicePreset, SpeechTextVoiceCustom]


class SpeechText(TypedDict, total=False):
    """Provide text for the avatar to speak via TTS."""

    text: Required[str]
    """Text script for speech-driven video generation."""

    type: Required[Literal["text"]]

    voice: SpeechTextVoice
    """Optional voice override for TTS.

    If not provided, the avatar's configured voice is used.
    """


Speech: TypeAlias = Union[SpeechAudio, SpeechText]
