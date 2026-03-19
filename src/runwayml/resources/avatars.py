# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import avatar_list_params, avatar_create_params, avatar_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.avatar_list_response import AvatarListResponse
from ..types.avatar_create_response import AvatarCreateResponse
from ..types.avatar_update_response import AvatarUpdateResponse
from ..types.avatar_retrieve_response import AvatarRetrieveResponse

__all__ = ["AvatarsResource", "AsyncAvatarsResource"]


class AvatarsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AvatarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AvatarsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        personality: str,
        reference_image: str,
        voice: avatar_create_params.Voice,
        document_ids: SequenceNotStr[str] | Omit = omit,
        image_processing: Literal["optimize", "none"] | Omit = omit,
        start_script: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarCreateResponse:
        """
        Create a new avatar with a reference image and voice.

        Args:
          name: The character name for the avatar.

          personality: System prompt defining how the avatar should behave in conversations.

          reference_image: A HTTPS URL.

          voice: The voice configuration for the avatar.

          document_ids: Optional list of knowledge document IDs to attach to this avatar. Documents
              provide additional context during conversations.

          image_processing: Controls image preprocessing. `optimize` improves the image for better avatar
              results. `none` uses the image as-is; quality not guaranteed.

          start_script: Optional opening message that the avatar will say when a session starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AvatarCreateResponse,
            self._post(
                "/v1/avatars",
                body=maybe_transform(
                    {
                        "name": name,
                        "personality": personality,
                        "reference_image": reference_image,
                        "voice": voice,
                        "document_ids": document_ids,
                        "image_processing": image_processing,
                        "start_script": start_script,
                    },
                    avatar_create_params.AvatarCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AvatarRetrieveResponse:
        """
        Get details of a specific avatar.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarRetrieveResponse,
            self._get(
                path_template("/v1/avatars/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        id: str,
        *,
        document_ids: SequenceNotStr[str] | Omit = omit,
        image_processing: Literal["optimize", "none"] | Omit = omit,
        name: str | Omit = omit,
        personality: str | Omit = omit,
        reference_image: str | Omit = omit,
        start_script: Optional[str] | Omit = omit,
        voice: avatar_update_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarUpdateResponse:
        """Update an existing avatar.

        At least one field must be provided.

        Args:
          document_ids: List of knowledge document IDs to attach to this avatar. Replaces all current
              attachments. Documents provide additional context during conversations.

          image_processing: Controls image preprocessing. `optimize` improves the image for better avatar
              results. `none` uses the image as-is; quality not guaranteed.

          name: The character name for the avatar.

          personality: System prompt defining how the avatar should behave in conversations.

          reference_image: A HTTPS URL.

          start_script: Optional opening message that the avatar will say when a session starts. Set to
              null to clear.

          voice: The voice configuration for the avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarUpdateResponse,
            self._patch(
                path_template("/v1/avatars/{id}", id=id),
                body=maybe_transform(
                    {
                        "document_ids": document_ids,
                        "image_processing": image_processing,
                        "name": name,
                        "personality": personality,
                        "reference_image": reference_image,
                        "start_script": start_script,
                        "voice": voice,
                    },
                    avatar_update_params.AvatarUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SyncCursorPage[AvatarListResponse]:
        """
        List avatars for the authenticated user with cursor-based pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/avatars",
            page=SyncCursorPage[AvatarListResponse],
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
                    avatar_list_params.AvatarListParams,
                ),
            ),
            model=cast(Any, AvatarListResponse),  # Union types cannot be passed in as arguments in the type system
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
        Delete an avatar.

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
            path_template("/v1/avatars/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAvatarsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncAvatarsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        personality: str,
        reference_image: str,
        voice: avatar_create_params.Voice,
        document_ids: SequenceNotStr[str] | Omit = omit,
        image_processing: Literal["optimize", "none"] | Omit = omit,
        start_script: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarCreateResponse:
        """
        Create a new avatar with a reference image and voice.

        Args:
          name: The character name for the avatar.

          personality: System prompt defining how the avatar should behave in conversations.

          reference_image: A HTTPS URL.

          voice: The voice configuration for the avatar.

          document_ids: Optional list of knowledge document IDs to attach to this avatar. Documents
              provide additional context during conversations.

          image_processing: Controls image preprocessing. `optimize` improves the image for better avatar
              results. `none` uses the image as-is; quality not guaranteed.

          start_script: Optional opening message that the avatar will say when a session starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AvatarCreateResponse,
            await self._post(
                "/v1/avatars",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "personality": personality,
                        "reference_image": reference_image,
                        "voice": voice,
                        "document_ids": document_ids,
                        "image_processing": image_processing,
                        "start_script": start_script,
                    },
                    avatar_create_params.AvatarCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AvatarRetrieveResponse:
        """
        Get details of a specific avatar.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarRetrieveResponse,
            await self._get(
                path_template("/v1/avatars/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        id: str,
        *,
        document_ids: SequenceNotStr[str] | Omit = omit,
        image_processing: Literal["optimize", "none"] | Omit = omit,
        name: str | Omit = omit,
        personality: str | Omit = omit,
        reference_image: str | Omit = omit,
        start_script: Optional[str] | Omit = omit,
        voice: avatar_update_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarUpdateResponse:
        """Update an existing avatar.

        At least one field must be provided.

        Args:
          document_ids: List of knowledge document IDs to attach to this avatar. Replaces all current
              attachments. Documents provide additional context during conversations.

          image_processing: Controls image preprocessing. `optimize` improves the image for better avatar
              results. `none` uses the image as-is; quality not guaranteed.

          name: The character name for the avatar.

          personality: System prompt defining how the avatar should behave in conversations.

          reference_image: A HTTPS URL.

          start_script: Optional opening message that the avatar will say when a session starts. Set to
              null to clear.

          voice: The voice configuration for the avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AvatarUpdateResponse,
            await self._patch(
                path_template("/v1/avatars/{id}", id=id),
                body=await async_maybe_transform(
                    {
                        "document_ids": document_ids,
                        "image_processing": image_processing,
                        "name": name,
                        "personality": personality,
                        "reference_image": reference_image,
                        "start_script": start_script,
                        "voice": voice,
                    },
                    avatar_update_params.AvatarUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AvatarUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AsyncPaginator[AvatarListResponse, AsyncCursorPage[AvatarListResponse]]:
        """
        List avatars for the authenticated user with cursor-based pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/avatars",
            page=AsyncCursorPage[AvatarListResponse],
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
                    avatar_list_params.AvatarListParams,
                ),
            ),
            model=cast(Any, AvatarListResponse),  # Union types cannot be passed in as arguments in the type system
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
        Delete an avatar.

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
            path_template("/v1/avatars/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AvatarsResourceWithRawResponse:
    def __init__(self, avatars: AvatarsResource) -> None:
        self._avatars = avatars

        self.create = to_raw_response_wrapper(
            avatars.create,
        )
        self.retrieve = to_raw_response_wrapper(
            avatars.retrieve,
        )
        self.update = to_raw_response_wrapper(
            avatars.update,
        )
        self.list = to_raw_response_wrapper(
            avatars.list,
        )
        self.delete = to_raw_response_wrapper(
            avatars.delete,
        )


class AsyncAvatarsResourceWithRawResponse:
    def __init__(self, avatars: AsyncAvatarsResource) -> None:
        self._avatars = avatars

        self.create = async_to_raw_response_wrapper(
            avatars.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            avatars.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            avatars.update,
        )
        self.list = async_to_raw_response_wrapper(
            avatars.list,
        )
        self.delete = async_to_raw_response_wrapper(
            avatars.delete,
        )


class AvatarsResourceWithStreamingResponse:
    def __init__(self, avatars: AvatarsResource) -> None:
        self._avatars = avatars

        self.create = to_streamed_response_wrapper(
            avatars.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            avatars.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            avatars.update,
        )
        self.list = to_streamed_response_wrapper(
            avatars.list,
        )
        self.delete = to_streamed_response_wrapper(
            avatars.delete,
        )


class AsyncAvatarsResourceWithStreamingResponse:
    def __init__(self, avatars: AsyncAvatarsResource) -> None:
        self._avatars = avatars

        self.create = async_to_streamed_response_wrapper(
            avatars.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            avatars.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            avatars.update,
        )
        self.list = async_to_streamed_response_wrapper(
            avatars.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            avatars.delete,
        )
