# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime

import httpx

from ..types import avatar_conversation_list_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.avatar_conversation_list_response import AvatarConversationListResponse
from ..types.avatar_conversation_retrieve_response import AvatarConversationRetrieveResponse

__all__ = ["AvatarConversationsResource", "AsyncAvatarConversationsResource"]


class AvatarConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AvatarConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AvatarConversationsResourceWithStreamingResponse(self)

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
    ) -> AvatarConversationRetrieveResponse:
        """
        Get detailed information about a specific conversation, including the transcript
        and recording download URL when available. The conversation ID is the same value
        returned when the realtime session was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarConversationRetrieveResponse,
            self._get(
                path_template("/v1/avatar_conversations/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarConversationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int,
        avatar: str | Omit = omit,
        cursor: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AvatarConversationListResponse]:
        """
        List realtime avatar conversations for the authenticated user with cursor-based
        pagination. Each conversation corresponds to a realtime session, and the
        conversation ID matches the realtime session ID. Pass `avatar` to restrict
        results to a single avatar.

        Args:
          limit: The maximum number of items to return per page.

          avatar: Filter to conversations that used the given custom avatar.

          cursor: Cursor from a previous response for fetching the next page of results.

          end_date: Filter conversations created before this timestamp (exclusive).

          start_date: Filter conversations created on or after this timestamp (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/avatar_conversations",
            page=SyncCursorPage[AvatarConversationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "avatar": avatar,
                        "cursor": cursor,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    avatar_conversation_list_params.AvatarConversationListParams,
                ),
            ),
            model=AvatarConversationListResponse,
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
        Delete a conversation and its associated data.

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
            path_template("/v1/avatar_conversations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAvatarConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncAvatarConversationsResourceWithStreamingResponse(self)

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
    ) -> AvatarConversationRetrieveResponse:
        """
        Get detailed information about a specific conversation, including the transcript
        and recording download URL when available. The conversation ID is the same value
        returned when the realtime session was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarConversationRetrieveResponse,
            await self._get(
                path_template("/v1/avatar_conversations/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarConversationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int,
        avatar: str | Omit = omit,
        cursor: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AvatarConversationListResponse, AsyncCursorPage[AvatarConversationListResponse]]:
        """
        List realtime avatar conversations for the authenticated user with cursor-based
        pagination. Each conversation corresponds to a realtime session, and the
        conversation ID matches the realtime session ID. Pass `avatar` to restrict
        results to a single avatar.

        Args:
          limit: The maximum number of items to return per page.

          avatar: Filter to conversations that used the given custom avatar.

          cursor: Cursor from a previous response for fetching the next page of results.

          end_date: Filter conversations created before this timestamp (exclusive).

          start_date: Filter conversations created on or after this timestamp (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/avatar_conversations",
            page=AsyncCursorPage[AvatarConversationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "avatar": avatar,
                        "cursor": cursor,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    avatar_conversation_list_params.AvatarConversationListParams,
                ),
            ),
            model=AvatarConversationListResponse,
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
        Delete a conversation and its associated data.

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
            path_template("/v1/avatar_conversations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AvatarConversationsResourceWithRawResponse:
    def __init__(self, avatar_conversations: AvatarConversationsResource) -> None:
        self._avatar_conversations = avatar_conversations

        self.retrieve = to_raw_response_wrapper(
            avatar_conversations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            avatar_conversations.list,
        )
        self.delete = to_raw_response_wrapper(
            avatar_conversations.delete,
        )


class AsyncAvatarConversationsResourceWithRawResponse:
    def __init__(self, avatar_conversations: AsyncAvatarConversationsResource) -> None:
        self._avatar_conversations = avatar_conversations

        self.retrieve = async_to_raw_response_wrapper(
            avatar_conversations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            avatar_conversations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            avatar_conversations.delete,
        )


class AvatarConversationsResourceWithStreamingResponse:
    def __init__(self, avatar_conversations: AvatarConversationsResource) -> None:
        self._avatar_conversations = avatar_conversations

        self.retrieve = to_streamed_response_wrapper(
            avatar_conversations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            avatar_conversations.list,
        )
        self.delete = to_streamed_response_wrapper(
            avatar_conversations.delete,
        )


class AsyncAvatarConversationsResourceWithStreamingResponse:
    def __init__(self, avatar_conversations: AsyncAvatarConversationsResource) -> None:
        self._avatar_conversations = avatar_conversations

        self.retrieve = async_to_streamed_response_wrapper(
            avatar_conversations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            avatar_conversations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            avatar_conversations.delete,
        )
