# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceCreateParams", "From", "FromAudio", "FromText"]


class VoiceCreateParams(TypedDict, total=False):
    from_: Required[Annotated[From, PropertyInfo(alias="from")]]

    name: Required[str]
    """A name for the voice."""

    description: Optional[str]
    """An optional description of the voice."""


class FromAudio(TypedDict, total=False):
    audio: Required[str]
    """A HTTPS URL."""

    type: Required[Literal["audio"]]


class FromText(TypedDict, total=False):
    model: Required[Literal["eleven_ttv_v3", "eleven_multilingual_ttv_v2"]]
    """The voice design model to use.

    Prefer eleven_ttv_v3 (latest); eleven_multilingual_ttv_v2 is the previous
    generation.
    """

    prompt: Required[str]
    """A text description of the desired voice characteristics.

    Must be at least 20 characters.
    """

    type: Required[Literal["text"]]


From: TypeAlias = Union[FromAudio, FromText]
