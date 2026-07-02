# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrganizationRetrieveUsageResponse",
    "Result",
    "ResultUsedCredit",
    "ResultsByAPIKey",
    "ResultsByAPIKeyUsedCredit",
]


class ResultUsedCredit(BaseModel):
    amount: int
    """The net number of credits spent on the model.

    May be negative if refunds exceeded charges on this day.
    """

    model: Literal[
        "gen4.5",
        "gen3a_turbo",
        "gen4_turbo",
        "gen4_image",
        "gen4_image_turbo",
        "gpt_image_2",
        "act_two",
        "gen4_aleph",
        "veo3",
        "veo3.1",
        "veo3.1_fast",
        "gemini_2.5_flash",
        "gemini_image3_pro",
        "gemini_image3.1_flash",
        "eleven_multilingual_v2",
        "seed_audio",
        "eleven_v3",
        "eleven_text_to_sound_v2",
        "eleven_voice_isolation",
        "eleven_voice_dubbing",
        "eleven_multilingual_sts_v2",
        "eleven_scribe_v2",
        "gwm1_avatars",
        "gwm1_avatar_async_audio_to_video",
        "gwm1_avatar_async_text_to_video",
        "voice_processing",
        "seedance2",
        "seedance2_fast",
        "seedance2_mini",
        "magnific_precision_upscaler_v2",
        "magnific_video_upscaler_creative",
        "kling2.5_turbo_pro",
        "kling3.0_pro",
        "kling3.0_4k",
        "kling3.0_standard",
        "klingO3_pro",
        "klingO3_standard",
        "klingO3_4k",
        "happyhorse_1_0",
        "aleph2",
        "product_swap",
        "product_ad",
        "multi_shot_video",
        "product_ugc",
        "marketing_stock_image",
        "product_campaign_image",
    ]
    """The model that credits were spent on."""


class Result(BaseModel):
    date: datetime.date
    """The date of the usage data in ISO-8601 format (YYYY-MM-DD).

    All dates are in UTC.
    """

    used_credits: List[ResultUsedCredit] = FieldInfo(alias="usedCredits")
    """The credits used per model for the given date."""


class ResultsByAPIKeyUsedCredit(BaseModel):
    amount: int

    api_key_id: str = FieldInfo(alias="apiKeyId")


class ResultsByAPIKey(BaseModel):
    date: datetime.date

    used_credits: List[ResultsByAPIKeyUsedCredit] = FieldInfo(alias="usedCredits")


class OrganizationRetrieveUsageResponse(BaseModel):
    models: List[
        Literal[
            "gen4.5",
            "gen3a_turbo",
            "gen4_turbo",
            "gen4_image",
            "gen4_image_turbo",
            "gpt_image_2",
            "act_two",
            "gen4_aleph",
            "veo3",
            "veo3.1",
            "veo3.1_fast",
            "gemini_2.5_flash",
            "gemini_image3_pro",
            "gemini_image3.1_flash",
            "eleven_multilingual_v2",
            "seed_audio",
            "eleven_v3",
            "eleven_text_to_sound_v2",
            "eleven_voice_isolation",
            "eleven_voice_dubbing",
            "eleven_multilingual_sts_v2",
            "eleven_scribe_v2",
            "gwm1_avatars",
            "gwm1_avatar_async_audio_to_video",
            "gwm1_avatar_async_text_to_video",
            "voice_processing",
            "seedance2",
            "seedance2_fast",
            "seedance2_mini",
            "magnific_precision_upscaler_v2",
            "magnific_video_upscaler_creative",
            "kling2.5_turbo_pro",
            "kling3.0_pro",
            "kling3.0_4k",
            "kling3.0_standard",
            "klingO3_pro",
            "klingO3_standard",
            "klingO3_4k",
            "happyhorse_1_0",
            "aleph2",
            "product_swap",
            "product_ad",
            "multi_shot_video",
            "product_ugc",
            "marketing_stock_image",
            "product_campaign_image",
        ]
    ]
    """The list of models with usage during the queried time range."""

    results: List[Result]

    api_keys: Optional[List[str]] = FieldInfo(alias="apiKeys", default=None)
    """Reserved for future use."""

    results_by_api_key: Optional[List[ResultsByAPIKey]] = FieldInfo(alias="resultsByApiKey", default=None)
    """Reserved for future use."""
