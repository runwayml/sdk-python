# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VoiceUpdateParams"]


class VoiceUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """An optional description of the voice."""

    name: str
    """A name for the voice."""
