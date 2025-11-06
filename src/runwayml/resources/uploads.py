# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Literal, Mapping

import httpx
from httpx import Timeout

from runwayml._models import BaseModel

from .._files import _transform_file, _async_transform_file
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, HttpxFileTypes, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._exceptions import APIStatusError, APITimeoutError, APIConnectionError
from .._base_client import make_request_options
from ..types.upload_create_ephemeral_response import UploadCreateEphemeralResponse


class _RunwayUploadStartedResponse(BaseModel):
    runwayUri: str
    uploadUrl: str
    fields: Mapping[str, str]


class _RunwayCreateUploadArguments(BaseModel):
    filename: str
    type: Literal["ephemeral"] = "ephemeral"


def _infer_filename(file: FileTypes) -> str:
    """Infer filename from FileTypes. Raises ValueError if filename cannot be inferred."""
    # If it's a tuple, use the first element as filename
    if isinstance(file, tuple):
        filename = file[0]
        if filename is not None:
            return filename
        # If filename is None in tuple, try to infer from the file content
        file_content = file[1]
    else:
        file_content = file

    # If it's a PathLike, extract the basename
    if isinstance(file_content, os.PathLike):
        return os.path.basename(str(file_content))

    # If it's bytes, we cannot infer
    if isinstance(file_content, bytes):
        raise ValueError(
            "Cannot infer filename from file. Please use the tuple format: "
            "(filename, file_content) where filename is a string. "
            "For example: ('myfile.jpg', file_content)"
        )

    # If it's an IO object, try to get the name attribute
    name = getattr(file_content, "name", None)
    if name is not None and isinstance(name, str):
        return str(os.path.basename(name))

    # If it's an IO object without a name, we cannot infer
    raise ValueError(
        "Cannot infer filename from file. Please use the tuple format: "
        "(filename, file_content) where filename is a string. "
        "For example: ('myfile.jpg', file_content)"
    )


def _build_file_tuple_with_filename(filename: str, transformed_file: HttpxFileTypes) -> HttpxFileTypes:
    """Build a file tuple with the given filename, preserving any additional metadata."""
    if isinstance(transformed_file, tuple):
        # Extract content and any additional elements (content_type, headers)
        file_content = transformed_file[1]
        if len(transformed_file) == 2:
            # (filename, content)
            return (filename, file_content)
        elif len(transformed_file) == 3:
            # (filename, content, content_type)
            return (filename, file_content, transformed_file[2])
        else:  # len == 4
            # (filename, content, content_type, headers)
            return (filename, file_content, transformed_file[2], transformed_file[3])
    else:
        # Just content, wrap with filename
        return (filename, transformed_file)


def _prepare_upload_data(
    fields: Mapping[str, str],
    file_metadata: str | Omit,
) -> dict[str, str]:
    """Prepare form data for upload, including metadata if provided."""
    form_data = dict(fields)
    if not isinstance(file_metadata, Omit):
        form_data["metadata"] = file_metadata
    return form_data


def _get_upload_timeout(
    timeout: float | httpx.Timeout | None | NotGiven,
    client_timeout: float | Timeout | None,
) -> float | Timeout | None:
    """Extract timeout for upload request."""
    if isinstance(timeout, NotGiven):
        return client_timeout
    return timeout


def _handle_upload_errors(response: httpx.Response, upload_url: str) -> None:
    """Handle upload errors consistently."""
    upload_request = httpx.Request("POST", httpx.URL(upload_url))
    try:
        response.raise_for_status()
    except httpx.TimeoutException as err:
        request = getattr(err, "request", upload_request)
        raise APITimeoutError(request=request) from err
    except httpx.RequestError as err:
        request = getattr(err, "request", upload_request)
        raise APIConnectionError(message=str(err), request=request) from err
    except httpx.HTTPStatusError as err:
        raise APIStatusError(
            message=f"Upload failed with status {err.response.status_code}",
            response=err.response,
            body=err.response.text,
        ) from err


__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create_ephemeral(
        self,
        *,
        file: FileTypes,
        file_metadata: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateEphemeralResponse:
        """Uploads a temporary media file that can be used in other API generation
        requests.

        The uploaded files will be automatically expired and deleted after a
        period of time.

        Args:
          file: The file to upload. Must be a supported media type (image, video, or audio).

          file_metadata: Optional metadata for the file, serialized as a field in multipart/form-data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        filename = _infer_filename(file)
        upload_placeholder = self._post(
            "/v1/uploads",
            body=maybe_transform(
                _RunwayCreateUploadArguments(filename=filename, type="ephemeral"),
                _RunwayCreateUploadArguments,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=_RunwayUploadStartedResponse,
        )
        
        file_tuple = _build_file_tuple_with_filename(
            filename, _transform_file(file)
        )
        form_data = _prepare_upload_data(upload_placeholder.fields, file_metadata)
        upload_timeout = _get_upload_timeout(timeout, self._client.timeout)
        
        with httpx.Client(timeout=upload_timeout) as client:
            response = client.post(
                upload_placeholder.uploadUrl,
                data=form_data,
                files={"file": file_tuple},
            )
            _handle_upload_errors(response, upload_placeholder.uploadUrl)
        
        return UploadCreateEphemeralResponse(uri=upload_placeholder.runwayUri)


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create_ephemeral(
        self,
        *,
        file: FileTypes,
        file_metadata: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateEphemeralResponse:
        """Uploads a temporary media file that can be used in other API generation
        requests.

        The uploaded files will be automatically expired and deleted after a
        period of time.

        Args:
          file: The file to upload. Must be a supported media type (image, video, or audio).

          file_metadata: Optional metadata for the file, serialized as a field in multipart/form-data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        filename = _infer_filename(file)
        upload_placeholder = await self._post(
            "/v1/uploads",
            body=maybe_transform(
                _RunwayCreateUploadArguments(filename=filename, type="ephemeral"),
                _RunwayCreateUploadArguments,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=_RunwayUploadStartedResponse,
        )
        
        file_tuple = _build_file_tuple_with_filename(
            filename, await _async_transform_file(file)
        )
        form_data = _prepare_upload_data(upload_placeholder.fields, file_metadata)
        upload_timeout = _get_upload_timeout(timeout, self._client.timeout)
        
        async with httpx.AsyncClient(timeout=upload_timeout) as client:
            response = await client.post(
                upload_placeholder.uploadUrl,
                data=form_data,
                files={"file": file_tuple},
            )
            _handle_upload_errors(response, upload_placeholder.uploadUrl)
        
        return UploadCreateEphemeralResponse(uri=upload_placeholder.runwayUri)


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create_ephemeral = to_raw_response_wrapper(
            uploads.create_ephemeral,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create_ephemeral = async_to_raw_response_wrapper(
            uploads.create_ephemeral,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create_ephemeral = to_streamed_response_wrapper(
            uploads.create_ephemeral,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create_ephemeral = async_to_streamed_response_wrapper(
            uploads.create_ephemeral,
        )
