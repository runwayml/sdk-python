# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import realtime_session_create_params
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
from .._base_client import make_request_options
from ..types.realtime_session_create_response import RealtimeSessionCreateResponse
from ..types.realtime_session_retrieve_response import RealtimeSessionRetrieveResponse

__all__ = ["RealtimeSessionsResource", "AsyncRealtimeSessionsResource"]


class RealtimeSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealtimeSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RealtimeSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return RealtimeSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        avatar: realtime_session_create_params.Avatar,
        model: Literal["gwm1_avatars"],
        max_duration: int | Omit = omit,
        personality: str | Omit = omit,
        start_script: str | Omit = omit,
        tools: Iterable[realtime_session_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeSessionCreateResponse:
        """
        Create a new realtime session with the specified model configuration.

        Args:
          avatar: The avatar configuration for the session.

          model: The realtime session model type.

          max_duration: Maximum session duration in seconds.

          personality: Override the avatar personality for this session. If not provided, uses the
              avatar default.

          start_script: Override the avatar start script for this session. If not provided, uses the
              avatar default.

          tools: Tools available to the avatar during the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/realtime_sessions",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "model": model,
                    "max_duration": max_duration,
                    "personality": personality,
                    "start_script": start_script,
                    "tools": tools,
                },
                realtime_session_create_params.RealtimeSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeSessionCreateResponse,
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
    ) -> RealtimeSessionRetrieveResponse:
        """
        Get the status of a realtime session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            RealtimeSessionRetrieveResponse,
            self._get(
                path_template("/v1/realtime_sessions/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, RealtimeSessionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        """
        Cancel an active realtime session.

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
            path_template("/v1/realtime_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRealtimeSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealtimeSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncRealtimeSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        avatar: realtime_session_create_params.Avatar,
        model: Literal["gwm1_avatars"],
        max_duration: int | Omit = omit,
        personality: str | Omit = omit,
        start_script: str | Omit = omit,
        tools: Iterable[realtime_session_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeSessionCreateResponse:
        """
        Create a new realtime session with the specified model configuration.

        Args:
          avatar: The avatar configuration for the session.

          model: The realtime session model type.

          max_duration: Maximum session duration in seconds.

          personality: Override the avatar personality for this session. If not provided, uses the
              avatar default.

          start_script: Override the avatar start script for this session. If not provided, uses the
              avatar default.

          tools: Tools available to the avatar during the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/realtime_sessions",
            body=await async_maybe_transform(
                {
                    "avatar": avatar,
                    "model": model,
                    "max_duration": max_duration,
                    "personality": personality,
                    "start_script": start_script,
                    "tools": tools,
                },
                realtime_session_create_params.RealtimeSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeSessionCreateResponse,
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
    ) -> RealtimeSessionRetrieveResponse:
        """
        Get the status of a realtime session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            RealtimeSessionRetrieveResponse,
            await self._get(
                path_template("/v1/realtime_sessions/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, RealtimeSessionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        """
        Cancel an active realtime session.

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
            path_template("/v1/realtime_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RealtimeSessionsResourceWithRawResponse:
    def __init__(self, realtime_sessions: RealtimeSessionsResource) -> None:
        self._realtime_sessions = realtime_sessions

        self.create = to_raw_response_wrapper(
            realtime_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            realtime_sessions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            realtime_sessions.delete,
        )


class AsyncRealtimeSessionsResourceWithRawResponse:
    def __init__(self, realtime_sessions: AsyncRealtimeSessionsResource) -> None:
        self._realtime_sessions = realtime_sessions

        self.create = async_to_raw_response_wrapper(
            realtime_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            realtime_sessions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            realtime_sessions.delete,
        )


class RealtimeSessionsResourceWithStreamingResponse:
    def __init__(self, realtime_sessions: RealtimeSessionsResource) -> None:
        self._realtime_sessions = realtime_sessions

        self.create = to_streamed_response_wrapper(
            realtime_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            realtime_sessions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            realtime_sessions.delete,
        )


class AsyncRealtimeSessionsResourceWithStreamingResponse:
    def __init__(self, realtime_sessions: AsyncRealtimeSessionsResource) -> None:
        self._realtime_sessions = realtime_sessions

        self.create = async_to_streamed_response_wrapper(
            realtime_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            realtime_sessions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            realtime_sessions.delete,
        )
