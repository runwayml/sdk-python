# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrganizationRetrieveResponse",
    "Tier",
    "TierModels",
    "TierModelsActTwo",
    "TierModelsElevenMultilingualV2",
    "TierModelsGemini2_5Flash",
    "TierModelsGen3aTurbo",
    "TierModelsGen4Aleph",
    "TierModelsGen4Image",
    "TierModelsGen4ImageTurbo",
    "TierModelsGen4Turbo",
    "TierModelsUpscaleV1",
    "TierModelsVeo3",
    "Usage",
    "UsageModels",
    "UsageModelsActTwo",
    "UsageModelsElevenMultilingualV2",
    "UsageModelsGemini2_5Flash",
    "UsageModelsGen3aTurbo",
    "UsageModelsGen4Aleph",
    "UsageModelsGen4Image",
    "UsageModelsGen4ImageTurbo",
    "UsageModelsGen4Turbo",
    "UsageModelsUpscaleV1",
    "UsageModelsVeo3",
]


class TierModelsActTwo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsElevenMultilingualV2(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGemini2_5Flash(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen3aTurbo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen4Aleph(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen4Image(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen4ImageTurbo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsGen4Turbo(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsUpscaleV1(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModelsVeo3(BaseModel):
    max_concurrent_generations: int = FieldInfo(alias="maxConcurrentGenerations")
    """The maximum number of generations that can be run concurrently for this model."""

    max_daily_generations: int = FieldInfo(alias="maxDailyGenerations")
    """The maximum number of generations that can be created each day for this model."""


class TierModels(BaseModel):
    act_two: Optional[TierModelsActTwo] = None
    """Limits associated with the act_two model."""

    eleven_multilingual_v2: Optional[TierModelsElevenMultilingualV2] = None
    """Limits associated with the eleven_multilingual_v2 model."""

    gemini_2_5_flash: Optional[TierModelsGemini2_5Flash] = FieldInfo(alias="gemini_2.5_flash", default=None)
    """Limits associated with the gemini_2.5_flash model."""

    gen3a_turbo: Optional[TierModelsGen3aTurbo] = None
    """Limits associated with the gen3a_turbo model."""

    gen4_aleph: Optional[TierModelsGen4Aleph] = None
    """Limits associated with the gen4_aleph model."""

    gen4_image: Optional[TierModelsGen4Image] = None
    """Limits associated with the gen4_image model."""

    gen4_image_turbo: Optional[TierModelsGen4ImageTurbo] = None
    """Limits associated with the gen4_image_turbo model."""

    gen4_turbo: Optional[TierModelsGen4Turbo] = None
    """Limits associated with the gen4_turbo model."""

    upscale_v1: Optional[TierModelsUpscaleV1] = None
    """Limits associated with the upscale_v1 model."""

    veo3: Optional[TierModelsVeo3] = None
    """Limits associated with the veo3 model."""


class Tier(BaseModel):
    max_monthly_credit_spend: int = FieldInfo(alias="maxMonthlyCreditSpend")
    """The maximum number of credits that can be purchased in a month."""

    models: TierModels
    """An object containing model-specific limits. Each key represents a model."""


class UsageModelsActTwo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsElevenMultilingualV2(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGemini2_5Flash(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen3aTurbo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen4Aleph(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen4Image(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen4ImageTurbo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsGen4Turbo(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsUpscaleV1(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModelsVeo3(BaseModel):
    daily_generations: int = FieldInfo(alias="dailyGenerations")
    """The number of generations that have been run for this model in the past day."""


class UsageModels(BaseModel):
    act_two: Optional[UsageModelsActTwo] = None
    """Usage data for the act_two model."""

    eleven_multilingual_v2: Optional[UsageModelsElevenMultilingualV2] = None
    """Usage data for the eleven_multilingual_v2 model."""

    gemini_2_5_flash: Optional[UsageModelsGemini2_5Flash] = FieldInfo(alias="gemini_2.5_flash", default=None)
    """Usage data for the gemini_2.5_flash model."""

    gen3a_turbo: Optional[UsageModelsGen3aTurbo] = None
    """Usage data for the gen3a_turbo model."""

    gen4_aleph: Optional[UsageModelsGen4Aleph] = None
    """Usage data for the gen4_aleph model."""

    gen4_image: Optional[UsageModelsGen4Image] = None
    """Usage data for the gen4_image model."""

    gen4_image_turbo: Optional[UsageModelsGen4ImageTurbo] = None
    """Usage data for the gen4_image_turbo model."""

    gen4_turbo: Optional[UsageModelsGen4Turbo] = None
    """Usage data for the gen4_turbo model."""

    upscale_v1: Optional[UsageModelsUpscaleV1] = None
    """Usage data for the upscale_v1 model."""

    veo3: Optional[UsageModelsVeo3] = None
    """Usage data for the veo3 model."""


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
