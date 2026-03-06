# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VoiceListParams"]


class VoiceListParams(TypedDict, total=False):
    limit: Required[int]
    """The maximum number of items to return per page."""

    cursor: str
    """Cursor from a previous response for fetching the next page of results."""
