# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import voice_list_params, voice_create_params, voice_preview_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.voice_list_response import VoiceListResponse
from ..types.voice_create_response import VoiceCreateResponse
from ..types.voice_preview_response import VoicePreviewResponse
from ..types.voice_retrieve_response import VoiceRetrieveResponse

__all__ = ["VoicesResource", "AsyncVoicesResource"]


class VoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: voice_create_params.From,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Create a custom voice from a text description.

        Args:
          from_: The source configuration for creating the voice.

          name: A name for the voice.

          description: An optional description of the voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/voices",
            body=maybe_transform(
                {
                    "from_": from_,
                    "name": name,
                    "description": description,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCreateResponse,
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
    ) -> VoiceRetrieveResponse:
        """
        Get details about a specific custom voice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            VoiceRetrieveResponse,
            self._get(
                f"/v1/voices/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VoiceRetrieveResponse
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
    ) -> SyncCursorPage[VoiceListResponse]:
        """
        List custom voices for the authenticated organization with cursor-based
        pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/voices",
            page=SyncCursorPage[VoiceListResponse],
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
                    voice_list_params.VoiceListParams,
                ),
            ),
            model=cast(Any, VoiceListResponse),  # Union types cannot be passed in as arguments in the type system
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
        Delete a custom voice.

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
            f"/v1/voices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def preview(
        self,
        *,
        model: Literal["eleven_multilingual_ttv_v2", "eleven_ttv_v3"],
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoicePreviewResponse:
        """Generate a short audio preview of a voice from a text description.

        Use this to
        audition a voice before creating it.

        Args:
          model: The voice design model to use.

          prompt: A text description of the desired voice characteristics. Must be at least 20
              characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/voices/preview",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                },
                voice_preview_params.VoicePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicePreviewResponse,
        )


class AsyncVoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: voice_create_params.From,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Create a custom voice from a text description.

        Args:
          from_: The source configuration for creating the voice.

          name: A name for the voice.

          description: An optional description of the voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/voices",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "name": name,
                    "description": description,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCreateResponse,
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
    ) -> VoiceRetrieveResponse:
        """
        Get details about a specific custom voice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            VoiceRetrieveResponse,
            await self._get(
                f"/v1/voices/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VoiceRetrieveResponse
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
    ) -> AsyncPaginator[VoiceListResponse, AsyncCursorPage[VoiceListResponse]]:
        """
        List custom voices for the authenticated organization with cursor-based
        pagination.

        Args:
          limit: The maximum number of items to return per page.

          cursor: Cursor from a previous response for fetching the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/voices",
            page=AsyncCursorPage[VoiceListResponse],
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
                    voice_list_params.VoiceListParams,
                ),
            ),
            model=cast(Any, VoiceListResponse),  # Union types cannot be passed in as arguments in the type system
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
        Delete a custom voice.

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
            f"/v1/voices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def preview(
        self,
        *,
        model: Literal["eleven_multilingual_ttv_v2", "eleven_ttv_v3"],
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoicePreviewResponse:
        """Generate a short audio preview of a voice from a text description.

        Use this to
        audition a voice before creating it.

        Args:
          model: The voice design model to use.

          prompt: A text description of the desired voice characteristics. Must be at least 20
              characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/voices/preview",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                },
                voice_preview_params.VoicePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicePreviewResponse,
        )


class VoicesResourceWithRawResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.create = to_raw_response_wrapper(
            voices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voices.retrieve,
        )
        self.list = to_raw_response_wrapper(
            voices.list,
        )
        self.delete = to_raw_response_wrapper(
            voices.delete,
        )
        self.preview = to_raw_response_wrapper(
            voices.preview,
        )


class AsyncVoicesResourceWithRawResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.create = async_to_raw_response_wrapper(
            voices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voices.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            voices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voices.delete,
        )
        self.preview = async_to_raw_response_wrapper(
            voices.preview,
        )


class VoicesResourceWithStreamingResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.create = to_streamed_response_wrapper(
            voices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voices.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            voices.list,
        )
        self.delete = to_streamed_response_wrapper(
            voices.delete,
        )
        self.preview = to_streamed_response_wrapper(
            voices.preview,
        )


class AsyncVoicesResourceWithStreamingResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.create = async_to_streamed_response_wrapper(
            voices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voices.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            voices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voices.delete,
        )
        self.preview = async_to_streamed_response_wrapper(
            voices.preview,
        )
