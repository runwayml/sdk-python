# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditLogRetrieveParams"]


class AuditLogRetrieveParams(TypedDict, total=False):
    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Organization to report on.

    Optional when this API project is linked to a single organization; required when
    it is linked to more than one.
    """
