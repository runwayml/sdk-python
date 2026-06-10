# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AvatarGetUsageResponse", "ByDay"]


class ByDay(BaseModel):
    date: datetime.date
    """The UTC calendar date (YYYY-MM-DD)."""

    seconds: int
    """Total seconds of measured conversation duration on this date."""

    sessions: int
    """Number of conversations started on this date."""


class AvatarGetUsageResponse(BaseModel):
    avg_duration_seconds: int = FieldInfo(alias="avgDurationSeconds")
    """
    Average duration in seconds across conversations with a measured duration, or 0
    if none completed. May not equal `totalSeconds / totalSessions` because
    unfinished conversations contribute to the session count but not the duration.
    """

    by_day: List[ByDay] = FieldInfo(alias="byDay")
    """Per-day usage across the date range.

    Days with no sessions are included with zeroes.
    """

    total_seconds: int = FieldInfo(alias="totalSeconds")
    """Total seconds across conversations with a measured duration in the date range."""

    total_sessions: int = FieldInfo(alias="totalSessions")
    """Number of conversations started in the date range.

    Includes unfinished and failed conversations.
    """
