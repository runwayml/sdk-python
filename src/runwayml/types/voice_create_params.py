# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceCreateParams", "From"]


class VoiceCreateParams(TypedDict, total=False):
    from_: Required[Annotated[From, PropertyInfo(alias="from")]]
    """The source configuration for creating the voice."""

    name: Required[str]
    """A name for the voice."""

    description: Optional[str]
    """An optional description of the voice."""


class From(TypedDict, total=False):
    """The source configuration for creating the voice."""

    model: Required[Literal["eleven_multilingual_ttv_v2", "eleven_ttv_v3"]]
    """The voice design model to use."""

    prompt: Required[str]
    """A text description of the desired voice characteristics.

    Must be at least 20 characters.
    """

    type: Required[Literal["text"]]
