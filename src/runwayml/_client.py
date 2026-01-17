# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import RunwayMLError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        tasks,
        uploads,
        organization,
        sound_effect,
        text_to_image,
        text_to_video,
        voice_dubbing,
        image_to_video,
        text_to_speech,
        video_to_video,
        voice_isolation,
        speech_to_speech,
        character_performance,
    )
    from .resources.tasks import TasksResource, AsyncTasksResource
    from .resources.uploads import UploadsResource, AsyncUploadsResource
    from .resources.organization import OrganizationResource, AsyncOrganizationResource
    from .resources.sound_effect import SoundEffectResource, AsyncSoundEffectResource
    from .resources.text_to_image import TextToImageResource, AsyncTextToImageResource
    from .resources.text_to_video import TextToVideoResource, AsyncTextToVideoResource
    from .resources.voice_dubbing import VoiceDubbingResource, AsyncVoiceDubbingResource
    from .resources.image_to_video import ImageToVideoResource, AsyncImageToVideoResource
    from .resources.text_to_speech import TextToSpeechResource, AsyncTextToSpeechResource
    from .resources.video_to_video import VideoToVideoResource, AsyncVideoToVideoResource
    from .resources.voice_isolation import VoiceIsolationResource, AsyncVoiceIsolationResource
    from .resources.speech_to_speech import SpeechToSpeechResource, AsyncSpeechToSpeechResource
    from .resources.character_performance import CharacterPerformanceResource, AsyncCharacterPerformanceResource

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
    # client options
    api_key: str
    runway_version: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = "2024-11-06",
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def tasks(self) -> TasksResource:
        from .resources.tasks import TasksResource

        return TasksResource(self)

    @cached_property
    def uploads(self) -> UploadsResource:
        from .resources.uploads import UploadsResource

        return UploadsResource(self)

    @cached_property
    def image_to_video(self) -> ImageToVideoResource:
        from .resources.image_to_video import ImageToVideoResource

        return ImageToVideoResource(self)

    @cached_property
    def video_to_video(self) -> VideoToVideoResource:
        from .resources.video_to_video import VideoToVideoResource

        return VideoToVideoResource(self)

    @cached_property
    def text_to_video(self) -> TextToVideoResource:
        from .resources.text_to_video import TextToVideoResource

        return TextToVideoResource(self)

    @cached_property
    def text_to_image(self) -> TextToImageResource:
        from .resources.text_to_image import TextToImageResource

        return TextToImageResource(self)

    @cached_property
    def character_performance(self) -> CharacterPerformanceResource:
        from .resources.character_performance import CharacterPerformanceResource

        return CharacterPerformanceResource(self)

    @cached_property
    def text_to_speech(self) -> TextToSpeechResource:
        from .resources.text_to_speech import TextToSpeechResource

        return TextToSpeechResource(self)

    @cached_property
    def sound_effect(self) -> SoundEffectResource:
        from .resources.sound_effect import SoundEffectResource

        return SoundEffectResource(self)

    @cached_property
    def voice_isolation(self) -> VoiceIsolationResource:
        from .resources.voice_isolation import VoiceIsolationResource

        return VoiceIsolationResource(self)

    @cached_property
    def voice_dubbing(self) -> VoiceDubbingResource:
        from .resources.voice_dubbing import VoiceDubbingResource

        return VoiceDubbingResource(self)

    @cached_property
    def speech_to_speech(self) -> SpeechToSpeechResource:
        from .resources.speech_to_speech import SpeechToSpeechResource

        return SpeechToSpeechResource(self)

    @cached_property
    def organization(self) -> OrganizationResource:
        from .resources.organization import OrganizationResource

        return OrganizationResource(self)

    @cached_property
    def with_raw_response(self) -> RunwayMLWithRawResponse:
        return RunwayMLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunwayMLWithStreamedResponse:
        return RunwayMLWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    api_key: str
    runway_version: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        runway_version: str | None = "2024-11-06",
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        from .resources.tasks import AsyncTasksResource

        return AsyncTasksResource(self)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        from .resources.uploads import AsyncUploadsResource

        return AsyncUploadsResource(self)

    @cached_property
    def image_to_video(self) -> AsyncImageToVideoResource:
        from .resources.image_to_video import AsyncImageToVideoResource

        return AsyncImageToVideoResource(self)

    @cached_property
    def video_to_video(self) -> AsyncVideoToVideoResource:
        from .resources.video_to_video import AsyncVideoToVideoResource

        return AsyncVideoToVideoResource(self)

    @cached_property
    def text_to_video(self) -> AsyncTextToVideoResource:
        from .resources.text_to_video import AsyncTextToVideoResource

        return AsyncTextToVideoResource(self)

    @cached_property
    def text_to_image(self) -> AsyncTextToImageResource:
        from .resources.text_to_image import AsyncTextToImageResource

        return AsyncTextToImageResource(self)

    @cached_property
    def character_performance(self) -> AsyncCharacterPerformanceResource:
        from .resources.character_performance import AsyncCharacterPerformanceResource

        return AsyncCharacterPerformanceResource(self)

    @cached_property
    def text_to_speech(self) -> AsyncTextToSpeechResource:
        from .resources.text_to_speech import AsyncTextToSpeechResource

        return AsyncTextToSpeechResource(self)

    @cached_property
    def sound_effect(self) -> AsyncSoundEffectResource:
        from .resources.sound_effect import AsyncSoundEffectResource

        return AsyncSoundEffectResource(self)

    @cached_property
    def voice_isolation(self) -> AsyncVoiceIsolationResource:
        from .resources.voice_isolation import AsyncVoiceIsolationResource

        return AsyncVoiceIsolationResource(self)

    @cached_property
    def voice_dubbing(self) -> AsyncVoiceDubbingResource:
        from .resources.voice_dubbing import AsyncVoiceDubbingResource

        return AsyncVoiceDubbingResource(self)

    @cached_property
    def speech_to_speech(self) -> AsyncSpeechToSpeechResource:
        from .resources.speech_to_speech import AsyncSpeechToSpeechResource

        return AsyncSpeechToSpeechResource(self)

    @cached_property
    def organization(self) -> AsyncOrganizationResource:
        from .resources.organization import AsyncOrganizationResource

        return AsyncOrganizationResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRunwayMLWithRawResponse:
        return AsyncRunwayMLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunwayMLWithStreamedResponse:
        return AsyncRunwayMLWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: RunwayML

    def __init__(self, client: RunwayML) -> None:
        self._client = client

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithRawResponse:
        from .resources.tasks import TasksResourceWithRawResponse

        return TasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithRawResponse:
        from .resources.uploads import UploadsResourceWithRawResponse

        return UploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def image_to_video(self) -> image_to_video.ImageToVideoResourceWithRawResponse:
        from .resources.image_to_video import ImageToVideoResourceWithRawResponse

        return ImageToVideoResourceWithRawResponse(self._client.image_to_video)

    @cached_property
    def video_to_video(self) -> video_to_video.VideoToVideoResourceWithRawResponse:
        from .resources.video_to_video import VideoToVideoResourceWithRawResponse

        return VideoToVideoResourceWithRawResponse(self._client.video_to_video)

    @cached_property
    def text_to_video(self) -> text_to_video.TextToVideoResourceWithRawResponse:
        from .resources.text_to_video import TextToVideoResourceWithRawResponse

        return TextToVideoResourceWithRawResponse(self._client.text_to_video)

    @cached_property
    def text_to_image(self) -> text_to_image.TextToImageResourceWithRawResponse:
        from .resources.text_to_image import TextToImageResourceWithRawResponse

        return TextToImageResourceWithRawResponse(self._client.text_to_image)

    @cached_property
    def character_performance(self) -> character_performance.CharacterPerformanceResourceWithRawResponse:
        from .resources.character_performance import CharacterPerformanceResourceWithRawResponse

        return CharacterPerformanceResourceWithRawResponse(self._client.character_performance)

    @cached_property
    def text_to_speech(self) -> text_to_speech.TextToSpeechResourceWithRawResponse:
        from .resources.text_to_speech import TextToSpeechResourceWithRawResponse

        return TextToSpeechResourceWithRawResponse(self._client.text_to_speech)

    @cached_property
    def sound_effect(self) -> sound_effect.SoundEffectResourceWithRawResponse:
        from .resources.sound_effect import SoundEffectResourceWithRawResponse

        return SoundEffectResourceWithRawResponse(self._client.sound_effect)

    @cached_property
    def voice_isolation(self) -> voice_isolation.VoiceIsolationResourceWithRawResponse:
        from .resources.voice_isolation import VoiceIsolationResourceWithRawResponse

        return VoiceIsolationResourceWithRawResponse(self._client.voice_isolation)

    @cached_property
    def voice_dubbing(self) -> voice_dubbing.VoiceDubbingResourceWithRawResponse:
        from .resources.voice_dubbing import VoiceDubbingResourceWithRawResponse

        return VoiceDubbingResourceWithRawResponse(self._client.voice_dubbing)

    @cached_property
    def speech_to_speech(self) -> speech_to_speech.SpeechToSpeechResourceWithRawResponse:
        from .resources.speech_to_speech import SpeechToSpeechResourceWithRawResponse

        return SpeechToSpeechResourceWithRawResponse(self._client.speech_to_speech)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        from .resources.organization import OrganizationResourceWithRawResponse

        return OrganizationResourceWithRawResponse(self._client.organization)


class AsyncRunwayMLWithRawResponse:
    _client: AsyncRunwayML

    def __init__(self, client: AsyncRunwayML) -> None:
        self._client = client

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithRawResponse:
        from .resources.tasks import AsyncTasksResourceWithRawResponse

        return AsyncTasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithRawResponse:
        from .resources.uploads import AsyncUploadsResourceWithRawResponse

        return AsyncUploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def image_to_video(self) -> image_to_video.AsyncImageToVideoResourceWithRawResponse:
        from .resources.image_to_video import AsyncImageToVideoResourceWithRawResponse

        return AsyncImageToVideoResourceWithRawResponse(self._client.image_to_video)

    @cached_property
    def video_to_video(self) -> video_to_video.AsyncVideoToVideoResourceWithRawResponse:
        from .resources.video_to_video import AsyncVideoToVideoResourceWithRawResponse

        return AsyncVideoToVideoResourceWithRawResponse(self._client.video_to_video)

    @cached_property
    def text_to_video(self) -> text_to_video.AsyncTextToVideoResourceWithRawResponse:
        from .resources.text_to_video import AsyncTextToVideoResourceWithRawResponse

        return AsyncTextToVideoResourceWithRawResponse(self._client.text_to_video)

    @cached_property
    def text_to_image(self) -> text_to_image.AsyncTextToImageResourceWithRawResponse:
        from .resources.text_to_image import AsyncTextToImageResourceWithRawResponse

        return AsyncTextToImageResourceWithRawResponse(self._client.text_to_image)

    @cached_property
    def character_performance(self) -> character_performance.AsyncCharacterPerformanceResourceWithRawResponse:
        from .resources.character_performance import AsyncCharacterPerformanceResourceWithRawResponse

        return AsyncCharacterPerformanceResourceWithRawResponse(self._client.character_performance)

    @cached_property
    def text_to_speech(self) -> text_to_speech.AsyncTextToSpeechResourceWithRawResponse:
        from .resources.text_to_speech import AsyncTextToSpeechResourceWithRawResponse

        return AsyncTextToSpeechResourceWithRawResponse(self._client.text_to_speech)

    @cached_property
    def sound_effect(self) -> sound_effect.AsyncSoundEffectResourceWithRawResponse:
        from .resources.sound_effect import AsyncSoundEffectResourceWithRawResponse

        return AsyncSoundEffectResourceWithRawResponse(self._client.sound_effect)

    @cached_property
    def voice_isolation(self) -> voice_isolation.AsyncVoiceIsolationResourceWithRawResponse:
        from .resources.voice_isolation import AsyncVoiceIsolationResourceWithRawResponse

        return AsyncVoiceIsolationResourceWithRawResponse(self._client.voice_isolation)

    @cached_property
    def voice_dubbing(self) -> voice_dubbing.AsyncVoiceDubbingResourceWithRawResponse:
        from .resources.voice_dubbing import AsyncVoiceDubbingResourceWithRawResponse

        return AsyncVoiceDubbingResourceWithRawResponse(self._client.voice_dubbing)

    @cached_property
    def speech_to_speech(self) -> speech_to_speech.AsyncSpeechToSpeechResourceWithRawResponse:
        from .resources.speech_to_speech import AsyncSpeechToSpeechResourceWithRawResponse

        return AsyncSpeechToSpeechResourceWithRawResponse(self._client.speech_to_speech)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        from .resources.organization import AsyncOrganizationResourceWithRawResponse

        return AsyncOrganizationResourceWithRawResponse(self._client.organization)


class RunwayMLWithStreamedResponse:
    _client: RunwayML

    def __init__(self, client: RunwayML) -> None:
        self._client = client

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithStreamingResponse:
        from .resources.tasks import TasksResourceWithStreamingResponse

        return TasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithStreamingResponse:
        from .resources.uploads import UploadsResourceWithStreamingResponse

        return UploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def image_to_video(self) -> image_to_video.ImageToVideoResourceWithStreamingResponse:
        from .resources.image_to_video import ImageToVideoResourceWithStreamingResponse

        return ImageToVideoResourceWithStreamingResponse(self._client.image_to_video)

    @cached_property
    def video_to_video(self) -> video_to_video.VideoToVideoResourceWithStreamingResponse:
        from .resources.video_to_video import VideoToVideoResourceWithStreamingResponse

        return VideoToVideoResourceWithStreamingResponse(self._client.video_to_video)

    @cached_property
    def text_to_video(self) -> text_to_video.TextToVideoResourceWithStreamingResponse:
        from .resources.text_to_video import TextToVideoResourceWithStreamingResponse

        return TextToVideoResourceWithStreamingResponse(self._client.text_to_video)

    @cached_property
    def text_to_image(self) -> text_to_image.TextToImageResourceWithStreamingResponse:
        from .resources.text_to_image import TextToImageResourceWithStreamingResponse

        return TextToImageResourceWithStreamingResponse(self._client.text_to_image)

    @cached_property
    def character_performance(self) -> character_performance.CharacterPerformanceResourceWithStreamingResponse:
        from .resources.character_performance import CharacterPerformanceResourceWithStreamingResponse

        return CharacterPerformanceResourceWithStreamingResponse(self._client.character_performance)

    @cached_property
    def text_to_speech(self) -> text_to_speech.TextToSpeechResourceWithStreamingResponse:
        from .resources.text_to_speech import TextToSpeechResourceWithStreamingResponse

        return TextToSpeechResourceWithStreamingResponse(self._client.text_to_speech)

    @cached_property
    def sound_effect(self) -> sound_effect.SoundEffectResourceWithStreamingResponse:
        from .resources.sound_effect import SoundEffectResourceWithStreamingResponse

        return SoundEffectResourceWithStreamingResponse(self._client.sound_effect)

    @cached_property
    def voice_isolation(self) -> voice_isolation.VoiceIsolationResourceWithStreamingResponse:
        from .resources.voice_isolation import VoiceIsolationResourceWithStreamingResponse

        return VoiceIsolationResourceWithStreamingResponse(self._client.voice_isolation)

    @cached_property
    def voice_dubbing(self) -> voice_dubbing.VoiceDubbingResourceWithStreamingResponse:
        from .resources.voice_dubbing import VoiceDubbingResourceWithStreamingResponse

        return VoiceDubbingResourceWithStreamingResponse(self._client.voice_dubbing)

    @cached_property
    def speech_to_speech(self) -> speech_to_speech.SpeechToSpeechResourceWithStreamingResponse:
        from .resources.speech_to_speech import SpeechToSpeechResourceWithStreamingResponse

        return SpeechToSpeechResourceWithStreamingResponse(self._client.speech_to_speech)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        from .resources.organization import OrganizationResourceWithStreamingResponse

        return OrganizationResourceWithStreamingResponse(self._client.organization)


class AsyncRunwayMLWithStreamedResponse:
    _client: AsyncRunwayML

    def __init__(self, client: AsyncRunwayML) -> None:
        self._client = client

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithStreamingResponse:
        from .resources.tasks import AsyncTasksResourceWithStreamingResponse

        return AsyncTasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithStreamingResponse:
        from .resources.uploads import AsyncUploadsResourceWithStreamingResponse

        return AsyncUploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def image_to_video(self) -> image_to_video.AsyncImageToVideoResourceWithStreamingResponse:
        from .resources.image_to_video import AsyncImageToVideoResourceWithStreamingResponse

        return AsyncImageToVideoResourceWithStreamingResponse(self._client.image_to_video)

    @cached_property
    def video_to_video(self) -> video_to_video.AsyncVideoToVideoResourceWithStreamingResponse:
        from .resources.video_to_video import AsyncVideoToVideoResourceWithStreamingResponse

        return AsyncVideoToVideoResourceWithStreamingResponse(self._client.video_to_video)

    @cached_property
    def text_to_video(self) -> text_to_video.AsyncTextToVideoResourceWithStreamingResponse:
        from .resources.text_to_video import AsyncTextToVideoResourceWithStreamingResponse

        return AsyncTextToVideoResourceWithStreamingResponse(self._client.text_to_video)

    @cached_property
    def text_to_image(self) -> text_to_image.AsyncTextToImageResourceWithStreamingResponse:
        from .resources.text_to_image import AsyncTextToImageResourceWithStreamingResponse

        return AsyncTextToImageResourceWithStreamingResponse(self._client.text_to_image)

    @cached_property
    def character_performance(self) -> character_performance.AsyncCharacterPerformanceResourceWithStreamingResponse:
        from .resources.character_performance import AsyncCharacterPerformanceResourceWithStreamingResponse

        return AsyncCharacterPerformanceResourceWithStreamingResponse(self._client.character_performance)

    @cached_property
    def text_to_speech(self) -> text_to_speech.AsyncTextToSpeechResourceWithStreamingResponse:
        from .resources.text_to_speech import AsyncTextToSpeechResourceWithStreamingResponse

        return AsyncTextToSpeechResourceWithStreamingResponse(self._client.text_to_speech)

    @cached_property
    def sound_effect(self) -> sound_effect.AsyncSoundEffectResourceWithStreamingResponse:
        from .resources.sound_effect import AsyncSoundEffectResourceWithStreamingResponse

        return AsyncSoundEffectResourceWithStreamingResponse(self._client.sound_effect)

    @cached_property
    def voice_isolation(self) -> voice_isolation.AsyncVoiceIsolationResourceWithStreamingResponse:
        from .resources.voice_isolation import AsyncVoiceIsolationResourceWithStreamingResponse

        return AsyncVoiceIsolationResourceWithStreamingResponse(self._client.voice_isolation)

    @cached_property
    def voice_dubbing(self) -> voice_dubbing.AsyncVoiceDubbingResourceWithStreamingResponse:
        from .resources.voice_dubbing import AsyncVoiceDubbingResourceWithStreamingResponse

        return AsyncVoiceDubbingResourceWithStreamingResponse(self._client.voice_dubbing)

    @cached_property
    def speech_to_speech(self) -> speech_to_speech.AsyncSpeechToSpeechResourceWithStreamingResponse:
        from .resources.speech_to_speech import AsyncSpeechToSpeechResourceWithStreamingResponse

        return AsyncSpeechToSpeechResourceWithStreamingResponse(self._client.speech_to_speech)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        from .resources.organization import AsyncOrganizationResourceWithStreamingResponse

        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)


Client = RunwayML

AsyncClient = AsyncRunwayML
