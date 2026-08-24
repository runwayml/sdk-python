# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .audio import (
    AudioResource,
    AsyncAudioResource,
    AudioResourceWithRawResponse,
    AsyncAudioResourceWithRawResponse,
    AudioResourceWithStreamingResponse,
    AsyncAudioResourceWithStreamingResponse,
)
from .image import (
    ImageResource,
    AsyncImageResource,
    ImageResourceWithRawResponse,
    AsyncImageResourceWithRawResponse,
    ImageResourceWithStreamingResponse,
    AsyncImageResourceWithStreamingResponse,
)
from .video import (
    VideoResource,
    AsyncVideoResource,
    VideoResourceWithRawResponse,
    AsyncVideoResourceWithRawResponse,
    VideoResourceWithStreamingResponse,
    AsyncVideoResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def video(self) -> VideoResource:
        return VideoResource(self._client)

    @cached_property
    def image(self) -> ImageResource:
        return ImageResource(self._client)

    @cached_property
    def audio(self) -> AudioResource:
        return AudioResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def video(self) -> AsyncVideoResource:
        return AsyncVideoResource(self._client)

    @cached_property
    def image(self) -> AsyncImageResource:
        return AsyncImageResource(self._client)

    @cached_property
    def audio(self) -> AsyncAudioResource:
        return AsyncAudioResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

    @cached_property
    def video(self) -> VideoResourceWithRawResponse:
        return VideoResourceWithRawResponse(self._generate.video)

    @cached_property
    def image(self) -> ImageResourceWithRawResponse:
        return ImageResourceWithRawResponse(self._generate.image)

    @cached_property
    def audio(self) -> AudioResourceWithRawResponse:
        return AudioResourceWithRawResponse(self._generate.audio)


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

    @cached_property
    def video(self) -> AsyncVideoResourceWithRawResponse:
        return AsyncVideoResourceWithRawResponse(self._generate.video)

    @cached_property
    def image(self) -> AsyncImageResourceWithRawResponse:
        return AsyncImageResourceWithRawResponse(self._generate.image)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithRawResponse:
        return AsyncAudioResourceWithRawResponse(self._generate.audio)


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

    @cached_property
    def video(self) -> VideoResourceWithStreamingResponse:
        return VideoResourceWithStreamingResponse(self._generate.video)

    @cached_property
    def image(self) -> ImageResourceWithStreamingResponse:
        return ImageResourceWithStreamingResponse(self._generate.image)

    @cached_property
    def audio(self) -> AudioResourceWithStreamingResponse:
        return AudioResourceWithStreamingResponse(self._generate.audio)


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

    @cached_property
    def video(self) -> AsyncVideoResourceWithStreamingResponse:
        return AsyncVideoResourceWithStreamingResponse(self._generate.video)

    @cached_property
    def image(self) -> AsyncImageResourceWithStreamingResponse:
        return AsyncImageResourceWithStreamingResponse(self._generate.image)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithStreamingResponse:
        return AsyncAudioResourceWithStreamingResponse(self._generate.audio)
