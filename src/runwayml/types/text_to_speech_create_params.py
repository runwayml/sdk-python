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
    "ElevenV3",
    "ElevenV3Voice",
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
    """The voice to use for text-to-speech generation.

    If omitted, a default voice is used.
    """


class SeedAudioVoice(TypedDict, total=False):
    """The voice to use for text-to-speech generation.

    If omitted, a default voice is used.
    """

    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """

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


class ElevenV3(TypedDict, total=False):
    model: Required[Literal["eleven_v3"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """The text to convert to speech.

    You can include expressive audio tags like [laughs] or [whispers] in the script.
    """

    voice: Required[ElevenV3Voice]
    """A voice preset from the RunwayML API."""

    apply_text_normalization: Annotated[Literal["auto", "on", "off"], PropertyInfo(alias="applyTextNormalization")]
    """Text normalization mode: 'auto', 'on', or 'off' (e.g. spelling out numbers)."""

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]
    """ISO 639-1 language code to enforce pronunciation and normalization."""

    seed: int
    """Optional seed for more deterministic output (0–4294967295). Not guaranteed."""

    similarity_boost: Annotated[float, PropertyInfo(alias="similarityBoost")]
    """How closely the output tracks the original speaker (0–1).

    Maps to ElevenLabs similarity_boost.
    """

    speed: float
    """Speech speed multiplier (0.7–1.2).

    1.0 is default; values below slow down and above speed up.
    """

    stability: float
    """Voice stability (0–1).

    Lower values allow broader emotional range; higher values are steadier.
    """

    style: float
    """Style exaggeration (0–1). Higher values amplify the speaker style."""

    use_speaker_boost: Annotated[bool, PropertyInfo(alias="useSpeakerBoost")]
    """Boost similarity to the original speaker at a small latency cost."""


class ElevenV3Voice(TypedDict, total=False):
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


TextToSpeechCreateParams: TypeAlias = Union[SeedAudio, ElevenMultilingualV2, ElevenV3]
