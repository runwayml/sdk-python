# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AvatarGetUsageParams"]


class AvatarGetUsageParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]]
    """End of the date range in UTC (exclusive). Required."""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]]
    """Start of the date range in UTC (inclusive). Required."""
