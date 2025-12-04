# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationRetrieveResponse", "Tier", "TierModels", "Usage", "UsageModels"]


class TierModels(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class Tier(BaseModel):
    max_monthly_credit_spend: int = FieldInfo(alias="maxMonthlyCreditSpend")
    """The maximum number of credits that can be purchased in a month."""

    models: Dict[str, TierModels]
    """An object containing model-specific limits. Each key represents a model."""


class UsageModels(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class Usage(BaseModel):
    models: Dict[str, UsageModels]


class OrganizationRetrieveResponse(BaseModel):
    credit_balance: int = FieldInfo(alias="creditBalance")
    """The number of credits remaining in the organization account."""

    tier: Tier
    """Limits associated with the organization's tier."""

    usage: Usage
    """Usage data for the organization."""
