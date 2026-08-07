# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebappListUsageParams"]


class WebappListUsageParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Start of the time window (inclusive), ISO-8601 datetime."""

    limit: Required[int]
    """The maximum number of items to return per page."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the time window (exclusive), ISO-8601 datetime.

    A `cursor` can only narrow this window, never extend it past `to`.
    """

    cursor: str
    """Cursor from a previous response for fetching the next page of results."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Organization to report on.

    Optional when this API project is linked to a single organization; required when
    it is linked to more than one.
    """

    workspace_ids: Annotated[str, PropertyInfo(alias="workspaceIds")]
    """Restrict results to these workspace IDs, as a comma-separated list.

    Defaults to every workspace you administer in the organization.
    """
