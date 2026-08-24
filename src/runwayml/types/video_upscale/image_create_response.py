# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ImageCreateResponse",
    "Routing",
    "RoutingEstimatedCost",
    "RoutingResolvedInput",
    "RoutingResolvedSettings",
    "RoutingCapacityFallback",
]


class RoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutingResolvedInput(BaseModel):
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    aspect_ratio: str = FieldInfo(alias="aspectRatio")
    """Aspect ratio used for routing display."""

    ratio: str
    """
    Concrete output ratio derived from aspectRatio and resolution for the selected
    model.
    """

    resolution: str
    """Megapixel tier used for routing display."""


class RoutingResolvedSettings(BaseModel):
    """The resolved config settings the router used for this request."""

    optimize_for: Literal["cost", "latency", "quality"] = FieldInfo(alias="optimizeFor")
    """
    The single optimization preference the config selected, used as the soft
    weighting when scoring eligible models.
    """

    price_ceiling: Optional[float] = FieldInfo(alias="priceCeiling", default=None)
    """
    The applied maximum credits per generation for this request's modality, or null
    if the config sets no ceiling.
    """


class RoutingCapacityFallback(BaseModel):
    """
    Present only when the config enables fallback.onCapacity and capacity affected this request.
    """

    all_exhausted: bool = FieldInfo(alias="allExhausted")
    """
    True when every eligible model was at its concurrency limit, so the best-ranked
    model was used and the task will queue.
    """

    skipped: List[str]
    """
    Eligible models that were considered for this request but not selected because
    this account is at its concurrency limit for them.
    """


class Routing(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""

    capacity_fallback: Optional[RoutingCapacityFallback] = FieldInfo(alias="capacityFallback", default=None)
    """
    Present only when the config enables fallback.onCapacity and capacity affected
    this request.
    """


class ImageCreateResponse(BaseModel):
    id: str
    """The ID of the created task. Poll GET /v1/tasks/:id for the result."""

    routing: Routing
    """Metadata describing which model the router selected and why."""
