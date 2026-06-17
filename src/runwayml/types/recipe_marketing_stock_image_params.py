# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecipeMarketingStockImageParams", "ReferenceImage"]


class RecipeMarketingStockImageParams(TypedDict, total=False):
    prompt: Required[str]
    """Marketing image brief.

    Describe the subject, audience, channel, desired mood, setting, and any
    constraints.
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """

    reference_image: Annotated[ReferenceImage, PropertyInfo(alias="referenceImage")]
    """Optional brand logo image to guide the generated marketing stock image.

    See [our docs](/assets/inputs#images) on image inputs.
    """


class ReferenceImage(TypedDict, total=False):
    """Optional brand logo image to guide the generated marketing stock image.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""
