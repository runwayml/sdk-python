# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["OrganizationRetrieveUsageParams"]


class OrganizationRetrieveUsageParams(TypedDict, total=False):
    before_date: Annotated[Union[str, date], PropertyInfo(alias="beforeDate", format="iso8601")]
    """The end date of the usage data in ISO-8601 format (YYYY-MM-DD), not inclusive.

    If unspecified, it will default to thirty days after the start date. Must be
    less than or equal to 90 days after the start date. All dates are in UTC.
    """

    group_by: Annotated[str, PropertyInfo(alias="groupBy")]
    """Also break usage down by tag in `resultsByTag`.

    `"tag"` gives one bucket per tag; a generation with several tags counts toward
    each of them. `"tag:<key>"` (for example `"tag:team"`) gives one bucket per
    value of that key, so each generation counts once. Generations without a
    matching tag fall under a `null` tag.
    """

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """The start date of the usage data in ISO-8601 format (YYYY-MM-DD).

    If unspecified, it will default to 30 days before the current date. All dates
    are in UTC.
    """

    tags: SequenceNotStr[str]
    """
    Only count generations that were created with every one of these tags in the
    `X-Runway-Tags` header. Tags are case-insensitive. Up to 10 tags.
    """
