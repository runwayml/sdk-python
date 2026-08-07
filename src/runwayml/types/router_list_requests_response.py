# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["RouterListRequestsResponse", "Pipeline", "PipelineFilter", "PipelineCapacity", "PipelineRank"]


class PipelineFilter(BaseModel):
    filter: Literal["capability", "prompt_length", "input_support", "allow_deny", "price"]
    """
    Hard-filter stage that ran: capability (modality/feature fit), prompt_length
    (prompt within model limits), input_support (requested inputs/assets),
    allow_deny (router model allowlist/denylist), or price (credit ceiling).
    """

    models: List[str]
    """Model IDs of the models that remained eligible after this filter stage."""

    type: Literal["filter"]


class PipelineCapacity(BaseModel):
    all_exhausted: bool = FieldInfo(alias="allExhausted")
    """
    True when every eligible model was at its limit, in which case none was skipped
    and the selected task queues.
    """

    skipped: List[str]
    """
    Model IDs that were eligible but passed over because the account was at its
    concurrency limit for them.
    """

    type: Literal["capacity"]


class PipelineRank(BaseModel):
    outcome: Literal["cost", "selected", "fallback", "single_candidate"]
    """
    How the router chose among eligible models: cost (sorted by estimated credits),
    selected (preference ranking chose a model), fallback (preference ranking failed
    so the eligible models were left in filter order), or single_candidate (only one
    model remained).
    """

    type: Literal["rank"]


Pipeline: TypeAlias = Annotated[
    Union[PipelineFilter, PipelineCapacity, PipelineRank], PropertyInfo(discriminator="type")
]


class RouterListRequestsResponse(BaseModel):
    """A recorded Model Router routing decision."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    emptied_by: List[Literal["capability", "prompt_length", "input_support", "allow_deny", "price"]] = FieldInfo(
        alias="emptiedBy"
    )
    """The filter(s) that reduced the eligible pool to zero."""

    estimated_credits: Optional[float] = FieldInfo(alias="estimatedCredits", default=None)

    model: Optional[str] = None

    pipeline: List[Pipeline]
    """
    Ordered routing story: hard-filter stages with surviving model ids, a capacity
    step when concurrency limits affected the pool, then rank step when selection
    reached ranking.
    """

    provider: Optional[str] = None

    reason: Optional[str] = None
    """Free-text explanation of the pick.

    Written by the ranker, so treat it as prose for humans and group on reasonCode
    instead.
    """

    reason_code: Optional[
        Literal["lowest_cost", "best_latency", "best_quality", "only_eligible_model", "filter_order_fallback"]
    ] = FieldInfo(alias="reasonCode", default=None)
    """
    Why the model won: lowest_cost, best_latency, best_quality, only_eligible_model,
    or filter_order_fallback (ranking was unavailable, so hard-filter order stood).
    Null when the request never reached ranking.
    """

    request_id: str = FieldInfo(alias="requestId")

    status: Literal["routed", "no_eligible_model", "router_config_not_found", "invalid_request", "error"]
    """
    How the routing attempt ended: routed (model selected), no_eligible_model (hard
    filters emptied the pool), router_config_not_found (same condition as the
    generate error of that name), invalid_request, or error.
    """

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
