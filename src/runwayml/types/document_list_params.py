# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    cursor: str
    """Cursor from a previous response for fetching the next page of results."""

    limit: int
    """The maximum number of items to return per page."""

    order: Literal["asc", "desc"]
    """Sort direction."""

    sort: Literal["createdAt", "updatedAt"]
    """Field to sort results by."""
