# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecipeAdLocalizationParams", "ReferenceImage"]


class RecipeAdLocalizationParams(TypedDict, total=False):
    reference_image: Required[Annotated[ReferenceImage, PropertyInfo(alias="referenceImage")]]
    """Reference ad image to localize.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    target_language: Required[
        Annotated[
            Literal[
                "ar",
                "zh",
                "zh-Hant",
                "nl",
                "en",
                "fr",
                "de",
                "hi",
                "id",
                "it",
                "ja",
                "ko",
                "pl",
                "pt",
                "ru",
                "es",
                "sv",
                "th",
                "tr",
                "uk",
                "vi",
                "el",
            ],
            PropertyInfo(alias="targetLanguage"),
        ]
    ]
    """Target language for the localized ad.

    Use ISO-style codes (e.g. "ja" for Japanese, "es" for Spanish).
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """


class ReferenceImage(TypedDict, total=False):
    """Reference ad image to localize.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""
