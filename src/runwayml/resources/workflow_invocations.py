# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow_invocation_retrieve_response import WorkflowInvocationRetrieveResponse

__all__ = ["WorkflowInvocationsResource", "AsyncWorkflowInvocationsResource"]


class WorkflowInvocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return WorkflowInvocationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowInvocationRetrieveResponse:
        """Return details about a workflow invocation.

        Consumers of this API should not
        expect updates more frequent than once every five seconds for a given workflow
        invocation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            WorkflowInvocationRetrieveResponse,
            self._get(
                path_template("/v1/workflow_invocations/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, WorkflowInvocationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncWorkflowInvocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncWorkflowInvocationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowInvocationRetrieveResponse:
        """Return details about a workflow invocation.

        Consumers of this API should not
        expect updates more frequent than once every five seconds for a given workflow
        invocation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            WorkflowInvocationRetrieveResponse,
            await self._get(
                path_template("/v1/workflow_invocations/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, WorkflowInvocationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WorkflowInvocationsResourceWithRawResponse:
    def __init__(self, workflow_invocations: WorkflowInvocationsResource) -> None:
        self._workflow_invocations = workflow_invocations

        self.retrieve = to_raw_response_wrapper(
            workflow_invocations.retrieve,
        )


class AsyncWorkflowInvocationsResourceWithRawResponse:
    def __init__(self, workflow_invocations: AsyncWorkflowInvocationsResource) -> None:
        self._workflow_invocations = workflow_invocations

        self.retrieve = async_to_raw_response_wrapper(
            workflow_invocations.retrieve,
        )


class WorkflowInvocationsResourceWithStreamingResponse:
    def __init__(self, workflow_invocations: WorkflowInvocationsResource) -> None:
        self._workflow_invocations = workflow_invocations

        self.retrieve = to_streamed_response_wrapper(
            workflow_invocations.retrieve,
        )


class AsyncWorkflowInvocationsResourceWithStreamingResponse:
    def __init__(self, workflow_invocations: AsyncWorkflowInvocationsResource) -> None:
        self._workflow_invocations = workflow_invocations

        self.retrieve = async_to_streamed_response_wrapper(
            workflow_invocations.retrieve,
        )
