# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationRetrieveUsageParams"]


class OrganizationRetrieveUsageParams(TypedDict, total=False):
    before_date: Annotated[Union[str, date], PropertyInfo(alias="beforeDate", format="iso8601")]
    """The end date of the usage data in ISO-8601 format (YYYY-MM-DD), not inclusive.

    If unspecified, it will default to thirty days after the start date. Must be
    less than or equal to 90 days after the start date. All dates are in UTC.
    """

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """The start date of the usage data in ISO-8601 format (YYYY-MM-DD).

    If unspecified, it will default to 30 days before the current date. All dates
    are in UTC.
    """
