# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import organization_retrieve_usage_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_retrieve_response import OrganizationRetrieveResponse
from ..types.organization_retrieve_usage_response import OrganizationRetrieveUsageResponse

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return OrganizationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        Get usage tier and credit balance information about the organization associated
        with the API key used to make the request.
        """
        return self._get(
            "/v1/organization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    def retrieve_usage(
        self,
        *,
        before_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveUsageResponse:
        """
        Fetch credit usage data broken down by model and day for the organization
        associated with the API key used to make the request. Up to 90 days of data can
        be queried at a time.

        Args:
          before_date: The end date of the usage data in ISO-8601 format (YYYY-MM-DD), not inclusive.
              If unspecified, it will default to thirty days after the start date. Must be
              less than or equal to 90 days after the start date. All dates are in UTC.

          start_date: The start date of the usage data in ISO-8601 format (YYYY-MM-DD). If
              unspecified, it will default to 30 days before the current date. All dates are
              in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/organization/usage",
            body=maybe_transform(
                {
                    "before_date": before_date,
                    "start_date": start_date,
                },
                organization_retrieve_usage_params.OrganizationRetrieveUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveUsageResponse,
        )


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncOrganizationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        Get usage tier and credit balance information about the organization associated
        with the API key used to make the request.
        """
        return await self._get(
            "/v1/organization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    async def retrieve_usage(
        self,
        *,
        before_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveUsageResponse:
        """
        Fetch credit usage data broken down by model and day for the organization
        associated with the API key used to make the request. Up to 90 days of data can
        be queried at a time.

        Args:
          before_date: The end date of the usage data in ISO-8601 format (YYYY-MM-DD), not inclusive.
              If unspecified, it will default to thirty days after the start date. Must be
              less than or equal to 90 days after the start date. All dates are in UTC.

          start_date: The start date of the usage data in ISO-8601 format (YYYY-MM-DD). If
              unspecified, it will default to 30 days before the current date. All dates are
              in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/organization/usage",
            body=await async_maybe_transform(
                {
                    "before_date": before_date,
                    "start_date": start_date,
                },
                organization_retrieve_usage_params.OrganizationRetrieveUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveUsageResponse,
        )


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.retrieve = to_raw_response_wrapper(
            organization.retrieve,
        )
        self.retrieve_usage = to_raw_response_wrapper(
            organization.retrieve_usage,
        )


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.retrieve = async_to_raw_response_wrapper(
            organization.retrieve,
        )
        self.retrieve_usage = async_to_raw_response_wrapper(
            organization.retrieve_usage,
        )


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.retrieve = to_streamed_response_wrapper(
            organization.retrieve,
        )
        self.retrieve_usage = to_streamed_response_wrapper(
            organization.retrieve_usage,
        )


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.retrieve = async_to_streamed_response_wrapper(
            organization.retrieve,
        )
        self.retrieve_usage = async_to_streamed_response_wrapper(
            organization.retrieve_usage,
        )
