# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RecipeProductCampaignImageParams", "Image"]


class RecipeProductCampaignImageParams(TypedDict, total=False):
    image: Required[Image]
    """Product image to preserve across the generated campaign.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    prompt: Required[str]
    """Style / creative brief for the fashion campaign, e.g.

    "High-key fashion editorial, gorpcore-meets-blokecore-meets-Y2K".
    """

    version: Required[Literal["2026-06", "unsafe-latest"]]
    """Workflow version.

    Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to
    track the newest stable version (may break without notice).
    """


class Image(TypedDict, total=False):
    """Product image to preserve across the generated campaign.

    See [our docs](/assets/inputs#images) on image inputs.
    """

    uri: Required[str]
    """A HTTPS URL."""
