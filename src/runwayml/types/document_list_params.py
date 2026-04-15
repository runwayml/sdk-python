# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    limit: Required[int]
    """The maximum number of items to return per page."""

    order: Required[Literal["asc", "desc"]]
    """Sort direction."""

    sort: Required[Literal["createdAt", "updatedAt"]]
    """Field to sort results by."""

    cursor: str
    """Cursor from a previous response for fetching the next page of results."""
