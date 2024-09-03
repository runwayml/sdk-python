# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVideoCreateParams"]


class ImageToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen3a_turbo"]]
    """The model variant to use."""

    prompt_image: Required[Annotated[str, PropertyInfo(alias="promptImage")]]
    """A URL pointing to an image. See documentation on input URLs."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]
    """
    A non-empty string up to 512 UTF-16 code points in length (that is,
    `promptText.length === 512` in JavaScript). This should describe in detail what
    should appear in the output.
    """

    seed: int
    """If unspecified, a random number is chosen.

    Varying the seed integer is a way to get different results for the same other
    request parameters. Using the same seed integer for an identical request will
    produce similar results.
    """

    watermark: bool
    """
    A boolean indicating whether or not the output video will contain a Runway
    watermark.
    """
