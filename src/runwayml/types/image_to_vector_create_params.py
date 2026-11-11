# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageToVectorCreateParams"]


class ImageToVectorCreateParams(TypedDict, total=False):
    image_uri: Required[Annotated[str, PropertyInfo(alias="imageUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:image/png;base64,...`, up to 5MB) containing an encoded image. See
    [our docs](/assets/inputs#images) on image inputs for more information.
    """

    model: Required[Literal["ideogram_vector"]]

    vectorization_mode: Annotated[Literal["simple", "default"], PropertyInfo(alias="vectorizationMode")]
    """Use simple for fewer shapes, or default to retain more detail."""
