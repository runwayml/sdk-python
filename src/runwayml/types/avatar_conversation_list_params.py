# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AvatarConversationListParams"]


class AvatarConversationListParams(TypedDict, total=False):
    limit: Required[int]
    """The maximum number of items to return per page."""

    avatar: str
    """Filter to conversations that used the given custom avatar."""

    cursor: str
    """Cursor from a previous response for fetching the next page of results."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """Filter conversations created before this timestamp (exclusive)."""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Filter conversations created on or after this timestamp (inclusive)."""
