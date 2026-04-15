# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationRetrieveUsageResponse", "Result", "ResultUsedCredit"]


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
        "act_two",
        "gen4_aleph",
        "veo3",
        "veo3.1",
        "veo3.1_fast",
        "gemini_2.5_flash",
        "gemini_image3_pro",
        "gemini_image3.1_flash",
        "eleven_multilingual_v2",
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
    ]
    """The model that credits were spent on."""


class Result(BaseModel):
    date: datetime.date
    """The date of the usage data in ISO-8601 format (YYYY-MM-DD).

    All dates are in UTC.
    """

    used_credits: List[ResultUsedCredit] = FieldInfo(alias="usedCredits")
    """The credits used per model for the given date."""


class OrganizationRetrieveUsageResponse(BaseModel):
    models: List[
        Literal[
            "gen4.5",
            "gen3a_turbo",
            "gen4_turbo",
            "gen4_image",
            "gen4_image_turbo",
            "act_two",
            "gen4_aleph",
            "veo3",
            "veo3.1",
            "veo3.1_fast",
            "gemini_2.5_flash",
            "gemini_image3_pro",
            "gemini_image3.1_flash",
            "eleven_multilingual_v2",
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
        ]
    ]
    """The list of models with usage during the queried time range."""

    results: List[Result]
