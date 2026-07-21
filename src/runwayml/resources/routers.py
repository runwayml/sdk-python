# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import router_list_params, router_create_params, router_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.router_list_response import RouterListResponse
from ..types.router_create_response import RouterCreateResponse
from ..types.router_update_response import RouterUpdateResponse
from ..types.router_retrieve_response import RouterRetrieveResponse

__all__ = ["RoutersResource", "AsyncRoutersResource"]


class RoutersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return RoutersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        slug: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        settings: router_create_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouterCreateResponse:
        """
        Create a Model Router configuration.

        Args:
          slug: Immutable slug used to reference this Model Router in generation requests (for
              example, production-video). Unique within the API project. The UUID id remains
              the canonical management identifier.

          description: An optional Model Router description.

          name: Optional human-readable display name for this router. Defaults to the slug when
              omitted.

          settings: Model Router routing preferences. Defaults to cost-optimized allow-all when
              omitted. Modality is implied by the generate endpoint used with this Model
              Router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/routers",
            body=maybe_transform(
                {
                    "slug": slug,
                    "description": description,
                    "name": name,
                    "settings": settings,
                },
                router_create_params.RouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterCreateResponse,
        )

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
    ) -> RouterRetrieveResponse:
        """
        Retrieve a Model Router configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        settings: router_update_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouterUpdateResponse:
        """Update a Model Router configuration.

        Settings changes append a new version; name
        and description updates do not. Settings are merged with the current snapshot —
        omitted fields keep their existing values.

        Args:
          name: Display name. The slug is immutable and cannot be changed after creation.

          settings: Nested merge: omitted settings fields keep their current values. When models is
              present, omitted models.mode or models.ids are preserved (sending only
              optimizeFor does not clear the model allowlist or credit ceiling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/routers/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "settings": settings,
                },
                router_update_params.RouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[RouterListResponse]:
        """
        List Model Router configurations for the authenticated organization with
        cursor-based pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/routers",
            page=SyncCursorPage[RouterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                    },
                    router_list_params.RouterListParams,
                ),
            ),
            model=RouterListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a Model Router configuration.

        Deleted Model Routers cannot be used for
        generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRoutersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncRoutersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        slug: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        settings: router_create_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouterCreateResponse:
        """
        Create a Model Router configuration.

        Args:
          slug: Immutable slug used to reference this Model Router in generation requests (for
              example, production-video). Unique within the API project. The UUID id remains
              the canonical management identifier.

          description: An optional Model Router description.

          name: Optional human-readable display name for this router. Defaults to the slug when
              omitted.

          settings: Model Router routing preferences. Defaults to cost-optimized allow-all when
              omitted. Modality is implied by the generate endpoint used with this Model
              Router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/routers",
            body=await async_maybe_transform(
                {
                    "slug": slug,
                    "description": description,
                    "name": name,
                    "settings": settings,
                },
                router_create_params.RouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterCreateResponse,
        )

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
    ) -> RouterRetrieveResponse:
        """
        Retrieve a Model Router configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        settings: router_update_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouterUpdateResponse:
        """Update a Model Router configuration.

        Settings changes append a new version; name
        and description updates do not. Settings are merged with the current snapshot —
        omitted fields keep their existing values.

        Args:
          name: Display name. The slug is immutable and cannot be changed after creation.

          settings: Nested merge: omitted settings fields keep their current values. When models is
              present, omitted models.mode or models.ids are preserved (sending only
              optimizeFor does not clear the model allowlist or credit ceiling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/routers/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "settings": settings,
                },
                router_update_params.RouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouterUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RouterListResponse, AsyncCursorPage[RouterListResponse]]:
        """
        List Model Router configurations for the authenticated organization with
        cursor-based pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/routers",
            page=AsyncCursorPage[RouterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                    },
                    router_list_params.RouterListParams,
                ),
            ),
            model=RouterListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a Model Router configuration.

        Deleted Model Routers cannot be used for
        generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RoutersResourceWithRawResponse:
    def __init__(self, routers: RoutersResource) -> None:
        self._routers = routers

        self.create = to_raw_response_wrapper(
            routers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            routers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            routers.update,
        )
        self.list = to_raw_response_wrapper(
            routers.list,
        )
        self.delete = to_raw_response_wrapper(
            routers.delete,
        )


class AsyncRoutersResourceWithRawResponse:
    def __init__(self, routers: AsyncRoutersResource) -> None:
        self._routers = routers

        self.create = async_to_raw_response_wrapper(
            routers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            routers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            routers.update,
        )
        self.list = async_to_raw_response_wrapper(
            routers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routers.delete,
        )


class RoutersResourceWithStreamingResponse:
    def __init__(self, routers: RoutersResource) -> None:
        self._routers = routers

        self.create = to_streamed_response_wrapper(
            routers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            routers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            routers.update,
        )
        self.list = to_streamed_response_wrapper(
            routers.list,
        )
        self.delete = to_streamed_response_wrapper(
            routers.delete,
        )


class AsyncRoutersResourceWithStreamingResponse:
    def __init__(self, routers: AsyncRoutersResource) -> None:
        self._routers = routers

        self.create = async_to_streamed_response_wrapper(
            routers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            routers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            routers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routers.delete,
        )
