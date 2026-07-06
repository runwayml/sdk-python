# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TextToSpeechCreateParams",
    "SeedAudio",
    "SeedAudioVoice",
    "ElevenMultilingualV2",
    "ElevenMultilingualV2Voice",
]


class SeedAudio(TypedDict, total=False):
    model: Required[Literal["seed_audio"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty text prompt.

    For text-to-speech, the words to speak. For text-to-audio, a scene description
    that can include voice direction, dialogue, music, and sound effects.
    """

    loudness_rate: Annotated[int, PropertyInfo(alias="loudnessRate")]
    """Relative output loudness. Negative is quieter, positive is louder; 0 is normal."""

    output_format: Annotated[Literal["wav", "mp3", "ogg_opus"], PropertyInfo(alias="outputFormat")]
    """Output audio container/format."""

    pitch_rate: Annotated[int, PropertyInfo(alias="pitchRate")]
    """Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged."""

    sample_rate: Annotated[Literal[8000, 16000, 24000, 32000, 44100, 48000], PropertyInfo(alias="sampleRate")]
    """Output sample rate in Hz."""

    speech_rate: Annotated[int, PropertyInfo(alias="speechRate")]
    """Relative speech speed. Negative is slower, positive is faster; 0 is normal."""

    voice: SeedAudioVoice
    """Clone from a single reference audio clip, then speak promptText in that voice."""


class SeedAudioVoice(TypedDict, total=False):
    """Clone from a single reference audio clip, then speak promptText in that voice."""

    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL."""

    type: Required[Literal["reference-audio"]]


class ElevenMultilingualV2(TypedDict, total=False):
    model: Required[Literal["eleven_multilingual_v2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A non-empty string up to 1000 characters (measured in UTF-16 code units).

    This should describe in detail what should appear in the output.
    """

    voice: Required[ElevenMultilingualV2Voice]
    """A voice preset from the RunwayML API."""


class ElevenMultilingualV2Voice(TypedDict, total=False):
    """A voice preset from the RunwayML API."""

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


TextToSpeechCreateParams: TypeAlias = Union[SeedAudio, ElevenMultilingualV2]
