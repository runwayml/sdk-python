# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceDubbingCreateParams"]


class VoiceDubbingCreateParams(TypedDict, total=False):
    audio_uri: Required[Annotated[str, PropertyInfo(alias="audioUri")]]
    """A HTTPS URL."""

    model: Required[Literal["eleven_voice_dubbing"]]

    target_lang: Required[
        Annotated[
            Literal[
                "en",
                "hi",
                "pt",
                "zh",
                "es",
                "fr",
                "de",
                "ja",
                "ar",
                "ru",
                "ko",
                "id",
                "it",
                "nl",
                "tr",
                "pl",
                "sv",
                "fil",
                "ms",
                "ro",
                "uk",
                "el",
                "cs",
                "da",
                "fi",
                "bg",
                "hr",
                "sk",
                "ta",
            ],
            PropertyInfo(alias="targetLang"),
        ]
    ]
    """
    The target language code to dub the audio to (e.g., "es" for Spanish, "fr" for
    French).
    """

    disable_voice_cloning: Annotated[bool, PropertyInfo(alias="disableVoiceCloning")]
    """Whether to disable voice cloning and use a generic voice instead."""

    drop_background_audio: Annotated[bool, PropertyInfo(alias="dropBackgroundAudio")]
    """Whether to remove background audio from the dubbed output."""

    num_speakers: Annotated[int, PropertyInfo(alias="numSpeakers")]
    """The number of speakers in the audio.

    If not provided, it will be detected automatically.
    """
