# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AudioCreateParams",
    "Input",
    "InputReferenceAudio",
    "InputVoice",
    "InputVoicePreset",
    "InputVoiceReferenceAudio",
]


class AudioCreateParams(TypedDict, total=False):
    config_id: Required[Annotated[str, PropertyInfo(alias="configId")]]
    """The slug of a saved Model Router config to route this request with."""

    input: Required[Input]
    """Model-agnostic audio generation input.

    The router selects a model and maps these options to it.
    """


class InputReferenceAudio(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""


class InputVoicePreset(TypedDict, total=False):
    """A preset voice."""

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
    """A Runway preset voice id.

    Choosing a preset routes only to models that support preset voices.
    """

    type: Required[Literal["preset"]]


class InputVoiceReferenceAudio(TypedDict, total=False):
    """Clone a voice from a reference audio clip, then speak promptText in that voice.

    Routes only to models that support voice cloning.
    """

    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL."""

    type: Required[Literal["reference-audio"]]


InputVoice: TypeAlias = Union[InputVoicePreset, InputVoiceReferenceAudio]


class Input(TypedDict, total=False):
    """Model-agnostic audio generation input.

    The router selects a model and maps these options to it.
    """

    prompt_text: Required[Annotated[str, PropertyInfo(alias="promptText")]]
    """For `speech`, the words to speak.

    For `audio`, a description of the desired output.
    """

    type: Required[Literal["speech", "audio"]]
    """
    How promptText is interpreted: `speech` speaks it verbatim as a script; `audio`
    treats it as a description of the desired audio, which may combine speech,
    music, ambience, and sound effects.
    """

    duration: float
    """Desired output duration in seconds for `audio` generation.

    Models that cannot honor an explicit duration are excluded.
    """

    loop: bool
    """When true, the `audio` output is designed to loop seamlessly.

    Models without loop support are excluded.
    """

    reference_audios: Annotated[Iterable[InputReferenceAudio], PropertyInfo(alias="referenceAudios")]
    """
    Optional reference audio clips guiding `audio` generation, for models that
    support them. Reference each clip in promptText as @Audio1, @Audio2, and @Audio3
    in order.
    """

    voice: InputVoice
    """The voice to speak with.

    When omitted, models that support a default voice remain eligible.
    """
