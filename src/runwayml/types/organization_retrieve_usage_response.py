# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationRetrieveUsageResponse", "Result", "ResultUsedCredit"]


class ResultUsedCredit(BaseModel):
    amount: int
    """The number of credits used for the model."""

    model: Literal["upscale_v1", "act_two", "gen4_image", "gen3a_turbo", "gen4_turbo"]
    """The model whose usage resulted in the credit usage."""


class Result(BaseModel):
    date: datetime.date
    """The date of the usage data in ISO-8601 format (YYYY-MM-DD).

    All dates are in UTC.
    """

    used_credits: List[ResultUsedCredit] = FieldInfo(alias="usedCredits")
    """The credits used per model for the given date."""


class OrganizationRetrieveUsageResponse(BaseModel):
    models: List[Literal["upscale_v1", "act_two", "gen4_image", "gen3a_turbo", "gen4_turbo"]]
    """The list of models with usage during the queried time range."""

    results: List[Result]
