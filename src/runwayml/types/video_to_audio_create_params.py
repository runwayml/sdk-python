# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoToAudioCreateParams"]


class VideoToAudioCreateParams(TypedDict, total=False):
    duration: Required[float]

    model: Required[Literal["mirelo_sfx_2_0"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    format: Literal["mp3", "wav", "flac"]
    """The format of the generated audio."""

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """Sounds to avoid in the generated audio."""

    num_variants: Annotated[int, PropertyInfo(alias="numVariants")]
    """The number of audio variations to generate."""

    preserve_speech: Annotated[bool, PropertyInfo(alias="preserveSpeech")]
    """Whether to preserve dialogue from the input video.

    Disabling this does not guarantee speech-free output.
    """

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A description of the sound effects to generate."""

    seed: int
    """A seed for reproducible generation."""
