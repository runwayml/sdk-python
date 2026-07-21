# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "VideoCreateResponse",
    "RoutedVideoTaskCreated",
    "RoutedVideoTaskCreatedRouting",
    "RoutedVideoTaskCreatedRoutingEstimatedCost",
    "RoutedVideoTaskCreatedRoutingResolvedInput",
    "RoutedVideoTaskCreatedRoutingResolvedSettings",
    "RoutedVideoDryRun",
    "RoutedVideoDryRunRouting",
    "RoutedVideoDryRunRoutingEstimatedCost",
    "RoutedVideoDryRunRoutingResolvedInput",
    "RoutedVideoDryRunRoutingResolvedSettings",
]


class RoutedVideoTaskCreatedRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedVideoTaskCreatedRoutingResolvedInput(BaseModel):
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    duration: float
    """Duration in seconds used for routing display (request value or router default)."""

    ratio: str
    """Concrete output ratio derived from aspectRatio (e.g.

    "1280:720"), or the router default.
    """

    resolution: str
    """Resolution tier from the request, or the router default when omitted."""


class RoutedVideoTaskCreatedRoutingResolvedSettings(BaseModel):
    """The resolved config settings the router used for this request."""

    optimize_for: Literal["cost", "latency", "quality"] = FieldInfo(alias="optimizeFor")
    """
    The single optimization preference the config selected, used as the soft
    weighting when scoring eligible models.
    """

    price_ceiling: Optional[float] = FieldInfo(alias="priceCeiling", default=None)
    """
    The applied maximum credits per generation for this request’s modality, or null
    if the config sets no ceiling.
    """


class RoutedVideoTaskCreatedRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedVideoTaskCreatedRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedVideoTaskCreatedRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedVideoTaskCreatedRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""


class RoutedVideoTaskCreated(BaseModel):
    id: str
    """The ID of the created task. Poll GET /v1/tasks/:id for the result."""

    dry_run: Literal[False] = FieldInfo(alias="dryRun")

    routing: RoutedVideoTaskCreatedRouting
    """Metadata describing which model the router selected and why."""


class RoutedVideoDryRunRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedVideoDryRunRoutingResolvedInput(BaseModel):
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    duration: float
    """Duration in seconds used for routing display (request value or router default)."""

    ratio: str
    """Concrete output ratio derived from aspectRatio (e.g.

    "1280:720"), or the router default.
    """

    resolution: str
    """Resolution tier from the request, or the router default when omitted."""


class RoutedVideoDryRunRoutingResolvedSettings(BaseModel):
    """The resolved config settings the router used for this request."""

    optimize_for: Literal["cost", "latency", "quality"] = FieldInfo(alias="optimizeFor")
    """
    The single optimization preference the config selected, used as the soft
    weighting when scoring eligible models.
    """

    price_ceiling: Optional[float] = FieldInfo(alias="priceCeiling", default=None)
    """
    The applied maximum credits per generation for this request’s modality, or null
    if the config sets no ceiling.
    """


class RoutedVideoDryRunRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedVideoDryRunRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedVideoDryRunRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedVideoDryRunRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""


class RoutedVideoDryRun(BaseModel):
    dry_run: Literal[True] = FieldInfo(alias="dryRun")

    routing: RoutedVideoDryRunRouting
    """Metadata describing which model the router selected and why."""


VideoCreateResponse: TypeAlias = Annotated[
    Union[RoutedVideoTaskCreated, RoutedVideoDryRun], PropertyInfo(discriminator="dry_run")
]
