# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVideoCreateParams"]


class ImageToVideoCreateParams(TypedDict, total=False):
    model: Required[Literal["gen3a_turbo"]]
    """The model variant to use."""

    prompt_image: Required[Annotated[str, PropertyInfo(alias="promptImage")]]
    """A HTTPS URL pointing to an image.

    Images must be JPEG, PNG, or WebP and are limited to 16MB. Responses must
    include a valid `Content-Length` header.
    """

    duration: Literal[5, 10]
    """The number of seconds of duration for the output video."""

    prompt_text: Annotated[str, PropertyInfo(alias="promptText")]

    ratio: Literal["16:9", "9:16"]
    """The aspect ratio of the output video."""

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
