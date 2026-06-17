# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RecipeMultiShotVideoParams",
    "Variant0",
    "Variant0FirstFrame",
    "Variant1",
    "Variant1Shot",
    "Variant1FirstFrame",
]


class Variant0(TypedDict, total=False):
    mode: Required[Literal["auto"]]
    """Workflow mode. `auto` decomposes a story prompt into exactly 5 shots."""

    prompt: Required[str]
    """Story prompt for auto mode."""

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Literal[5, 10, 15]
    """Total duration of the output video in seconds. Defaults to 10 seconds."""

    first_frame: Annotated[Variant0FirstFrame, PropertyInfo(alias="firstFrame")]
    """Optional image used as the first frame of the output video.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"]
    """Output dimensions as width:height.

    720p ratios (`1280:720`, `720:1280`, `960:960`) use the standard tier; 1080p
    ratios (`1920:1080`, `1080:1920`, `1440:1440`) use the pro tier. Defaults to
    `1280:720`.
    """


class Variant0FirstFrame(TypedDict, total=False):
    """Optional image used as the first frame of the output video.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""


class Variant1(TypedDict, total=False):
    mode: Required[Literal["custom"]]
    """Workflow mode. `custom` polishes a user-provided shot list of 3–5 shots."""

    shots: Required[Iterable[Variant1Shot]]
    """Shot list for custom mode (3–5 shots).

    Per-shot durations must sum to `duration`.
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    audio: bool
    """Whether to generate audio for the video."""

    duration: Literal[5, 10, 15]
    """Total duration of the output video in seconds. Defaults to 10 seconds."""

    first_frame: Annotated[Variant1FirstFrame, PropertyInfo(alias="firstFrame")]
    """Optional image used as the first frame of the output video.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    ratio: Literal["1280:720", "720:1280", "960:960", "1920:1080", "1080:1920", "1440:1440"]
    """Output dimensions as width:height.

    720p ratios (`1280:720`, `720:1280`, `960:960`) use the standard tier; 1080p
    ratios (`1920:1080`, `1080:1920`, `1440:1440`) use the pro tier. Defaults to
    `1280:720`.
    """


class Variant1Shot(TypedDict, total=False):
    duration: Required[int]
    """Duration of this shot in seconds."""

    prompt: Required[str]
    """Shot description prompt."""


class Variant1FirstFrame(TypedDict, total=False):
    """Optional image used as the first frame of the output video.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""


RecipeMultiShotVideoParams: TypeAlias = Union[Variant0, Variant1]
