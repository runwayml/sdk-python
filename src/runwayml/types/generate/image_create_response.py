# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ImageCreateResponse",
    "RoutedImageTaskCreated",
    "RoutedImageTaskCreatedRouting",
    "RoutedImageTaskCreatedRoutingEstimatedCost",
    "RoutedImageTaskCreatedRoutingResolvedInput",
    "RoutedImageTaskCreatedRoutingResolvedSettings",
    "RoutedImageTaskCreatedRoutingCapacityFallback",
    "RoutedImageDryRun",
    "RoutedImageDryRunRouting",
    "RoutedImageDryRunRoutingEstimatedCost",
    "RoutedImageDryRunRoutingResolvedInput",
    "RoutedImageDryRunRoutingResolvedSettings",
    "RoutedImageDryRunRoutingCapacityFallback",
]


class RoutedImageTaskCreatedRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedImageTaskCreatedRoutingResolvedInput(BaseModel):
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


class RoutedImageTaskCreatedRoutingResolvedSettings(BaseModel):
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


class RoutedImageTaskCreatedRoutingCapacityFallback(BaseModel):
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


class RoutedImageTaskCreatedRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedImageTaskCreatedRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedImageTaskCreatedRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedImageTaskCreatedRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""

    capacity_fallback: Optional[RoutedImageTaskCreatedRoutingCapacityFallback] = FieldInfo(
        alias="capacityFallback", default=None
    )
    """
    Present only when the config enables fallback.onCapacity and capacity affected
    this request.
    """


class RoutedImageTaskCreated(BaseModel):
    id: str
    """The ID of the created task. Poll GET /v1/tasks/:id for the result."""

    dry_run: Literal[False] = FieldInfo(alias="dryRun")

    routing: RoutedImageTaskCreatedRouting
    """Metadata describing which model the router selected and why."""


class RoutedImageDryRunRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedImageDryRunRoutingResolvedInput(BaseModel):
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


class RoutedImageDryRunRoutingResolvedSettings(BaseModel):
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


class RoutedImageDryRunRoutingCapacityFallback(BaseModel):
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


class RoutedImageDryRunRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedImageDryRunRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedImageDryRunRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedImageDryRunRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""

    capacity_fallback: Optional[RoutedImageDryRunRoutingCapacityFallback] = FieldInfo(
        alias="capacityFallback", default=None
    )
    """
    Present only when the config enables fallback.onCapacity and capacity affected
    this request.
    """


class RoutedImageDryRun(BaseModel):
    dry_run: Literal[True] = FieldInfo(alias="dryRun")

    routing: RoutedImageDryRunRouting
    """Metadata describing which model the router selected and why."""


ImageCreateResponse: TypeAlias = Annotated[
    Union[RoutedImageTaskCreated, RoutedImageDryRun], PropertyInfo(discriminator="dry_run")
]
