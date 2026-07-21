# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VideoCreateParams",
    "Input",
    "InputContentModeration",
    "InputKeyframe",
    "InputKeyframeUnionMember0",
    "InputKeyframeUnionMember0Range",
    "InputKeyframeUnionMember1",
    "InputKeyframeUnionMember1Range",
    "InputReferenceAudio",
    "InputReferenceImage",
    "InputReferenceVideo",
]


class VideoCreateParams(TypedDict, total=False):
    config_id: Required[Annotated[str, PropertyInfo(alias="configId")]]
    """The slug of a saved Model Router config to route this request with."""

    input: Required[Input]
    """Model-agnostic video generation input.

    Fields are optional; the router selects a model and maps these options to it.
    """

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]
    """
    When true, run the full routing pipeline and return the decision and estimated
    cost without generating. No task is created, nothing is billed, and no asset is
    produced.
    """


class InputContentModeration(TypedDict, total=False):
    """Settings that affect the behavior of the content moderation system."""

    public_figure_threshold: Annotated[Literal["auto", "low"], PropertyInfo(alias="publicFigureThreshold")]
    """
    When set to `low`, the content moderation system will be less strict about
    preventing generations that include recognizable public figures.
    """


class InputKeyframeUnionMember0Range(TypedDict, total=False):
    end_seconds: Required[int]

    start_seconds: Required[int]


class InputKeyframeUnionMember0(TypedDict, total=False):
    seconds: Required[float]

    uri: Required[str]
    """A HTTPS URL."""

    range: InputKeyframeUnionMember0Range


class InputKeyframeUnionMember1Range(TypedDict, total=False):
    end_seconds: Required[int]

    start_seconds: Required[int]


class InputKeyframeUnionMember1(TypedDict, total=False):
    at: Required[float]

    uri: Required[str]
    """A HTTPS URL."""

    range: InputKeyframeUnionMember1Range


InputKeyframe: TypeAlias = Union[InputKeyframeUnionMember0, InputKeyframeUnionMember1]


class InputReferenceAudio(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL."""


class InputReferenceImage(TypedDict, total=False):
    role: Required[Literal["first", "last", "reference"]]
    """How the image is used.

    `first` is the starting frame; `last` is an end frame; `reference` is additional
    image context.
    """

    uri: Required[str]
    """A HTTPS URL."""


class InputReferenceVideo(TypedDict, total=False):
    role: Required[Literal["source", "reference"]]
    """How the video is used.

    `source` is the primary video-to-video input; `reference` is additional video
    context.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Input(TypedDict, total=False):
    """Model-agnostic video generation input.

    Fields are optional; the router selects a model and maps these options to it.
    """

    aspect_ratio: Annotated[Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"], PropertyInfo(alias="aspectRatio")]
    """Desired aspect ratio.

    Models that do not support the requested aspect are excluded.
    """

    audio: bool
    """Whether to generate native audio with the video.

    When true, only models that output audio remain eligible; when false, silent
    models and models with an audio toggle remain eligible (always-on native-audio
    models are excluded). When omitted, the selected model’s default applies.
    """

    content_moderation: Annotated[InputContentModeration, PropertyInfo(alias="contentModeration")]
    """Settings that affect the behavior of the content moderation system."""

    duration: int
    """Desired duration of the output video, in seconds.

    Unsupported values exclude models; with a source video, V2V duration support
    applies.
    """

    keyframes: Iterable[InputKeyframe]
    """Timed guidance images for video restyle.

    Requires a source video; unsupported models are excluded.
    """

    negative_prompt: Annotated[str, PropertyInfo(alias="negativePrompt")]
    """A text description of what to avoid in the output."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """A text prompt describing the desired video."""

    reference_audio: Annotated[Iterable[InputReferenceAudio], PropertyInfo(alias="referenceAudio")]
    """Optional audio inputs for the generation."""

    reference_images: Annotated[Iterable[InputReferenceImage], PropertyInfo(alias="referenceImages")]
    """Optional image inputs.

    Each entry requires a `role`. At most one `first` and one `last` are allowed;
    multiple `reference` images are allowed.
    """

    reference_videos: Annotated[Iterable[InputReferenceVideo], PropertyInfo(alias="referenceVideos")]
    """Optional video inputs.

    Each entry requires a `role`. Use `source` for video-to-video; use `reference`
    for additional context videos (only models that support them remain eligible).
    At most one `source` is allowed.
    """

    resolution: Literal["480p", "720p", "1080p", "4k"]
    """Desired output resolution tier.

    Models that do not support the requested tier are excluded.
    """

    seed: int
    """A seed for reproducible generation. Random if omitted."""
