# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrganizationRetrieveResponse",
    "Tier",
    "TierModels",
    "TierModelsGen3aTurbo",
    "TierModelsGen4Turbo",
    "Usage",
    "UsageModels",
    "UsageModelsGen3aTurbo",
    "UsageModelsGen4Turbo",
]


class TierModelsGen3aTurbo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen4Turbo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModels(BaseModel):
    gen3a_turbo: Optional[TierModelsGen3aTurbo] = None
    """Limits associated with the gen3a_turbo model."""

    gen4_turbo: Optional[TierModelsGen4Turbo] = None
    """Limits associated with the gen4_turbo model."""


class Tier(BaseModel):
    max_monthly_credit_spend: int = FieldInfo(alias="maxMonthlyCreditSpend")
    """The maximum number of credits that can be purchased in a month."""

    models: TierModels
    """An object containing model-specific limits. Each key represents a model."""


class UsageModelsGen3aTurbo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen4Turbo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModels(BaseModel):
    gen3a_turbo: Optional[UsageModelsGen3aTurbo] = None
    """Usage data for the gen3a_turbo model."""

    gen4_turbo: Optional[UsageModelsGen4Turbo] = None
    """Usage data for the gen4_turbo model."""


class Usage(BaseModel):
    models: UsageModels
    """Usage data for each model."""


class OrganizationRetrieveResponse(BaseModel):
    credit_balance: int = FieldInfo(alias="creditBalance")
    """The number of credits remaining in the organization account."""

    tier: Tier
    """Limits associated with the organization's tier."""

    usage: Usage
    """Usage data for the organization."""
