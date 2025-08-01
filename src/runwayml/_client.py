# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    tasks,
    organization,
    text_to_image,
    video_upscale,
    image_to_video,
    video_to_video,
    character_performance,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import RunwayMLError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "RunwayML",
    "AsyncRunwayML",
    "Client",
    "AsyncClient",
]


class RunwayML(SyncAPIClient):
    tasks: tasks.TasksResource
    image_to_video: image_to_video.ImageToVideoResource
    video_to_video: video_to_video.VideoToVideoResource
    text_to_image: text_to_image.TextToImageResource
    video_upscale: video_upscale.VideoUpscaleResource
    character_performance: character_performance.CharacterPerformanceResource
    organization: organization.OrganizationResource
    with_raw_response: RunwayMLWithRawResponse
    with_streaming_response: RunwayMLWithStreamedResponse

    # client options
    api_key: str
    runway_version: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = "2024-11-06",
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous RunwayML client instance.

        This automatically infers the `api_key` argument from the `RUNWAYML_API_SECRET` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RUNWAYML_API_SECRET")
        if api_key is None:
            raise RunwayMLError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RUNWAYML_API_SECRET environment variable"
            )
        self.api_key = api_key

        if runway_version is None:
            runway_version = "2024-11-06"
        self.runway_version = runway_version

        if base_url is None:
            base_url = os.environ.get("RUNWAYML_BASE_URL")
        if base_url is None:
            base_url = f"https://api.dev.runwayml.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.tasks = tasks.TasksResource(self)
        self.image_to_video = image_to_video.ImageToVideoResource(self)
        self.video_to_video = video_to_video.VideoToVideoResource(self)
        self.text_to_image = text_to_image.TextToImageResource(self)
        self.video_upscale = video_upscale.VideoUpscaleResource(self)
        self.character_performance = character_performance.CharacterPerformanceResource(self)
        self.organization = organization.OrganizationResource(self)
        self.with_raw_response = RunwayMLWithRawResponse(self)
        self.with_streaming_response = RunwayMLWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Runway-Version": self.runway_version,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            runway_version=runway_version or self.runway_version,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRunwayML(AsyncAPIClient):
    tasks: tasks.AsyncTasksResource
    image_to_video: image_to_video.AsyncImageToVideoResource
    video_to_video: video_to_video.AsyncVideoToVideoResource
    text_to_image: text_to_image.AsyncTextToImageResource
    video_upscale: video_upscale.AsyncVideoUpscaleResource
    character_performance: character_performance.AsyncCharacterPerformanceResource
    organization: organization.AsyncOrganizationResource
    with_raw_response: AsyncRunwayMLWithRawResponse
    with_streaming_response: AsyncRunwayMLWithStreamedResponse

    # client options
    api_key: str
    runway_version: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = "2024-11-06",
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRunwayML client instance.

        This automatically infers the `api_key` argument from the `RUNWAYML_API_SECRET` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RUNWAYML_API_SECRET")
        if api_key is None:
            raise RunwayMLError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RUNWAYML_API_SECRET environment variable"
            )
        self.api_key = api_key

        if runway_version is None:
            runway_version = "2024-11-06"
        self.runway_version = runway_version

        if base_url is None:
            base_url = os.environ.get("RUNWAYML_BASE_URL")
        if base_url is None:
            base_url = f"https://api.dev.runwayml.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.tasks = tasks.AsyncTasksResource(self)
        self.image_to_video = image_to_video.AsyncImageToVideoResource(self)
        self.video_to_video = video_to_video.AsyncVideoToVideoResource(self)
        self.text_to_image = text_to_image.AsyncTextToImageResource(self)
        self.video_upscale = video_upscale.AsyncVideoUpscaleResource(self)
        self.character_performance = character_performance.AsyncCharacterPerformanceResource(self)
        self.organization = organization.AsyncOrganizationResource(self)
        self.with_raw_response = AsyncRunwayMLWithRawResponse(self)
        self.with_streaming_response = AsyncRunwayMLWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Runway-Version": self.runway_version,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            runway_version=runway_version or self.runway_version,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RunwayMLWithRawResponse:
    def __init__(self, client: RunwayML) -> None:
        self.tasks = tasks.TasksResourceWithRawResponse(client.tasks)
        self.image_to_video = image_to_video.ImageToVideoResourceWithRawResponse(client.image_to_video)
        self.video_to_video = video_to_video.VideoToVideoResourceWithRawResponse(client.video_to_video)
        self.text_to_image = text_to_image.TextToImageResourceWithRawResponse(client.text_to_image)
        self.video_upscale = video_upscale.VideoUpscaleResourceWithRawResponse(client.video_upscale)
        self.character_performance = character_performance.CharacterPerformanceResourceWithRawResponse(
            client.character_performance
        )
        self.organization = organization.OrganizationResourceWithRawResponse(client.organization)


class AsyncRunwayMLWithRawResponse:
    def __init__(self, client: AsyncRunwayML) -> None:
        self.tasks = tasks.AsyncTasksResourceWithRawResponse(client.tasks)
        self.image_to_video = image_to_video.AsyncImageToVideoResourceWithRawResponse(client.image_to_video)
        self.video_to_video = video_to_video.AsyncVideoToVideoResourceWithRawResponse(client.video_to_video)
        self.text_to_image = text_to_image.AsyncTextToImageResourceWithRawResponse(client.text_to_image)
        self.video_upscale = video_upscale.AsyncVideoUpscaleResourceWithRawResponse(client.video_upscale)
        self.character_performance = character_performance.AsyncCharacterPerformanceResourceWithRawResponse(
            client.character_performance
        )
        self.organization = organization.AsyncOrganizationResourceWithRawResponse(client.organization)


class RunwayMLWithStreamedResponse:
    def __init__(self, client: RunwayML) -> None:
        self.tasks = tasks.TasksResourceWithStreamingResponse(client.tasks)
        self.image_to_video = image_to_video.ImageToVideoResourceWithStreamingResponse(client.image_to_video)
        self.video_to_video = video_to_video.VideoToVideoResourceWithStreamingResponse(client.video_to_video)
        self.text_to_image = text_to_image.TextToImageResourceWithStreamingResponse(client.text_to_image)
        self.video_upscale = video_upscale.VideoUpscaleResourceWithStreamingResponse(client.video_upscale)
        self.character_performance = character_performance.CharacterPerformanceResourceWithStreamingResponse(
            client.character_performance
        )
        self.organization = organization.OrganizationResourceWithStreamingResponse(client.organization)


class AsyncRunwayMLWithStreamedResponse:
    def __init__(self, client: AsyncRunwayML) -> None:
        self.tasks = tasks.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.image_to_video = image_to_video.AsyncImageToVideoResourceWithStreamingResponse(client.image_to_video)
        self.video_to_video = video_to_video.AsyncVideoToVideoResourceWithStreamingResponse(client.video_to_video)
        self.text_to_image = text_to_image.AsyncTextToImageResourceWithStreamingResponse(client.text_to_image)
        self.video_upscale = video_upscale.AsyncVideoUpscaleResourceWithStreamingResponse(client.video_upscale)
        self.character_performance = character_performance.AsyncCharacterPerformanceResourceWithStreamingResponse(
            client.character_performance
        )
        self.organization = organization.AsyncOrganizationResourceWithStreamingResponse(client.organization)


Client = RunwayML

AsyncClient = AsyncRunwayML
