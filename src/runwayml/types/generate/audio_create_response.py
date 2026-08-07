# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AudioCreateResponse",
    "RoutedAudioTaskCreated",
    "RoutedAudioTaskCreatedRouting",
    "RoutedAudioTaskCreatedRoutingEstimatedCost",
    "RoutedAudioTaskCreatedRoutingResolvedInput",
    "RoutedAudioTaskCreatedRoutingResolvedSettings",
    "RoutedAudioTaskCreatedRoutingCapacityFallback",
    "RoutedAudioDryRun",
    "RoutedAudioDryRunRouting",
    "RoutedAudioDryRunRoutingEstimatedCost",
    "RoutedAudioDryRunRoutingResolvedInput",
    "RoutedAudioDryRunRoutingResolvedSettings",
    "RoutedAudioDryRunRoutingCapacityFallback",
]


class RoutedAudioTaskCreatedRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedAudioTaskCreatedRoutingResolvedInput(BaseModel):
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    type: Literal["speech", "audio"]
    """The prompt mode the router routed for."""

    voice: Literal["preset", "reference-audio", "default", "none"]
    """
    How the selected model resolves the voice: the requested preset or
    reference-audio clone, the model default for voiceless speech, or none for
    general audio.
    """


class RoutedAudioTaskCreatedRoutingResolvedSettings(BaseModel):
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


class RoutedAudioTaskCreatedRoutingCapacityFallback(BaseModel):
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


class RoutedAudioTaskCreatedRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedAudioTaskCreatedRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedAudioTaskCreatedRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedAudioTaskCreatedRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""

    capacity_fallback: Optional[RoutedAudioTaskCreatedRoutingCapacityFallback] = FieldInfo(
        alias="capacityFallback", default=None
    )
    """
    Present only when the config enables fallback.onCapacity and capacity affected
    this request.
    """


class RoutedAudioTaskCreated(BaseModel):
    id: str
    """The ID of the created task. Poll GET /v1/tasks/:id for the result."""

    dry_run: Literal[False] = FieldInfo(alias="dryRun")

    routing: RoutedAudioTaskCreatedRouting
    """Metadata describing which model the router selected and why."""


class RoutedAudioDryRunRoutingEstimatedCost(BaseModel):
    """Estimated cost, computed against current pricing."""

    credits: float
    """Estimated cost of the generation in credits."""


class RoutedAudioDryRunRoutingResolvedInput(BaseModel):
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    type: Literal["speech", "audio"]
    """The prompt mode the router routed for."""

    voice: Literal["preset", "reference-audio", "default", "none"]
    """
    How the selected model resolves the voice: the requested preset or
    reference-audio clone, the model default for voiceless speech, or none for
    general audio.
    """


class RoutedAudioDryRunRoutingResolvedSettings(BaseModel):
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


class RoutedAudioDryRunRoutingCapacityFallback(BaseModel):
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


class RoutedAudioDryRunRouting(BaseModel):
    """Metadata describing which model the router selected and why."""

    config_id: str = FieldInfo(alias="configId")
    """The slug of the router config that was applied to this request."""

    estimated_cost: RoutedAudioDryRunRoutingEstimatedCost = FieldInfo(alias="estimatedCost")
    """Estimated cost, computed against current pricing."""

    model: str
    """The public name of the model the router selected."""

    provider: str
    """The provider of the selected model."""

    resolved_input: RoutedAudioDryRunRoutingResolvedInput = FieldInfo(alias="resolvedInput")
    """Request-side defaults resolved for the routing response.

    Not necessarily identical to prepared model options.
    """

    resolved_settings: RoutedAudioDryRunRoutingResolvedSettings = FieldInfo(alias="resolvedSettings")
    """The resolved config settings the router used for this request."""

    capacity_fallback: Optional[RoutedAudioDryRunRoutingCapacityFallback] = FieldInfo(
        alias="capacityFallback", default=None
    )
    """
    Present only when the config enables fallback.onCapacity and capacity affected
    this request.
    """


class RoutedAudioDryRun(BaseModel):
    dry_run: Literal[True] = FieldInfo(alias="dryRun")

    routing: RoutedAudioDryRunRouting
    """Metadata describing which model the router selected and why."""


AudioCreateResponse: TypeAlias = Annotated[
    Union[RoutedAudioTaskCreated, RoutedAudioDryRun], PropertyInfo(discriminator="dry_run")
]
