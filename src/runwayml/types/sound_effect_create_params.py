# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SoundEffectCreateParams", "SeedAudio", "MireloSfx2_0", "ElevenTextToSoundV2"]


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

    reference_audios: Annotated[SequenceNotStr[str], PropertyInfo(alias="referenceAudios")]
    """Up to three reference audio clips.

    When provided, reference them in promptText as @Audio1, @Audio2, and @Audio3 in
    order.
    """

    sample_rate: Annotated[Literal[8000, 16000, 24000, 32000, 44100, 48000], PropertyInfo(alias="sampleRate")]
    """Output sample rate in Hz."""

    speech_rate: Annotated[int, PropertyInfo(alias="speechRate")]
    """Relative speech speed. Negative is slower, positive is faster; 0 is normal."""


class MireloSfx2_0(TypedDict, total=False):
    duration: Required[float]
    """The duration of the generated audio in seconds."""

    model: Required[Literal["mirelo_sfx_2_0"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A description of the sound effects to generate."""

    format: Literal["mp3", "wav", "flac"]
    """The format of the generated audio."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Sounds to avoid in the generated audio."""

    num_variants: Annotated[int, PropertyInfo(alias="numVariants")]
    """The number of audio variations to generate."""

    seed: int
    """A seed for reproducible generation."""


class ElevenTextToSoundV2(TypedDict, total=False):
    model: Required[Literal["eleven_text_to_sound_v2"]]

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """A text description of the sound effect to generate."""

    duration: float
    """The duration of the sound effect in seconds, between 0.5 and 30 seconds.

    If not provided, the duration will be determined automatically based on the text
    description.
    """

    loop: bool
    """Whether the output sound effect should be designed to loop seamlessly."""


SoundEffectCreateParams: TypeAlias = Union[SeedAudio, MireloSfx2_0, ElevenTextToSoundV2]
