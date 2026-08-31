# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from runwayml.lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)

from ..types import video_to_hdr_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.video_to_hdr_create_response import VideoToHdrCreateResponse

__all__ = ["VideoToHdrResource", "AsyncVideoToHdrResource"]


class VideoToHdrResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> VideoToHdrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoToHdrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoToHdrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VideoToHdrResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["ruby"],
        video_uri: str,
        output_format: Literal["hdr10", "hlg", "hdr_prores", "hdr_exr_sequence"] | Omit = omit,
        prores_profile: Literal["422", "4444", "422 HQ"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint starts a task to upconvert an SDR video to true HDR with Ruby,
        Runway's HDR grading model. The output keeps the source's own pixels — luma and
        color are extended into the HDR range, nothing is re-synthesized. Set
        `outputFormat` to choose the delivery profile: `hdr10` (HEVC Main 10, BT.2020 +
        PQ, the default), `hlg` (HEVC Main 10, BT.2020 + HLG), `hdr_prores` (BT.2020 +
        PQ ProRes .mov editorial mezzanine, tier selectable with `proresProfile`), or
        `hdr_exr_sequence` (a .zip of half-float OpenEXR frames in linear BT.2020
        display light, for compositing). Tasks bill per second of output at 20 credits
        per second, rising to 40 credits per second when the source is larger than 4
        megapixels (roughly 4K) — an upconvert delivers at the source's own resolution.

        Args:
          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          output_format: The HDR delivery profile of the output. `hdr10` (default) returns an HEVC Main
              10, BT.2020 + PQ .mp4; `hlg` returns an HEVC Main 10, BT.2020 + HLG .mp4;
              `hdr_prores` returns a BT.2020 + PQ ProRes .mov editorial mezzanine, whose tier
              is selectable with `proresProfile`; `hdr_exr_sequence` returns a .zip of
              half-float OpenEXR frames holding the HDR signal as linear BT.2020 display
              light, 1.0 = 100 nits, ready to composite. The EXR zip is the whole delivery —
              the frames, a colorimetry.json sidecar, a provenance.json sidecar declaring the
              upconvert, and the source audio as audio.wav when the source has any. All four
              profiles bill at the same rate: 20 credits per second of output, rising to 40
              credits per second when the source is larger than 4 megapixels (roughly 4K).

          prores_profile: The ProRes tier of the `hdr_prores` mezzanine. Only valid when `outputFormat` is
              `hdr_prores`. Defaults to `422 HQ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/video_to_hdr",
            body=maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "output_format": output_format,
                    "prores_profile": prores_profile,
                },
                video_to_hdr_create_params.VideoToHdrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VideoToHdrCreateResponse, self._client),
        )


class AsyncVideoToHdrResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncVideoToHdrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoToHdrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoToHdrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVideoToHdrResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["ruby"],
        video_uri: str,
        output_format: Literal["hdr10", "hlg", "hdr_prores", "hdr_exr_sequence"] | Omit = omit,
        prores_profile: Literal["422", "4444", "422 HQ"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint starts a task to upconvert an SDR video to true HDR with Ruby,
        Runway's HDR grading model. The output keeps the source's own pixels — luma and
        color are extended into the HDR range, nothing is re-synthesized. Set
        `outputFormat` to choose the delivery profile: `hdr10` (HEVC Main 10, BT.2020 +
        PQ, the default), `hlg` (HEVC Main 10, BT.2020 + HLG), `hdr_prores` (BT.2020 +
        PQ ProRes .mov editorial mezzanine, tier selectable with `proresProfile`), or
        `hdr_exr_sequence` (a .zip of half-float OpenEXR frames in linear BT.2020
        display light, for compositing). Tasks bill per second of output at 20 credits
        per second, rising to 40 credits per second when the source is larger than 4
        megapixels (roughly 4K) — an upconvert delivers at the source's own resolution.

        Args:
          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          output_format: The HDR delivery profile of the output. `hdr10` (default) returns an HEVC Main
              10, BT.2020 + PQ .mp4; `hlg` returns an HEVC Main 10, BT.2020 + HLG .mp4;
              `hdr_prores` returns a BT.2020 + PQ ProRes .mov editorial mezzanine, whose tier
              is selectable with `proresProfile`; `hdr_exr_sequence` returns a .zip of
              half-float OpenEXR frames holding the HDR signal as linear BT.2020 display
              light, 1.0 = 100 nits, ready to composite. The EXR zip is the whole delivery —
              the frames, a colorimetry.json sidecar, a provenance.json sidecar declaring the
              upconvert, and the source audio as audio.wav when the source has any. All four
              profiles bill at the same rate: 20 credits per second of output, rising to 40
              credits per second when the source is larger than 4 megapixels (roughly 4K).

          prores_profile: The ProRes tier of the `hdr_prores` mezzanine. Only valid when `outputFormat` is
              `hdr_prores`. Defaults to `422 HQ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/video_to_hdr",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "output_format": output_format,
                    "prores_profile": prores_profile,
                },
                video_to_hdr_create_params.VideoToHdrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VideoToHdrCreateResponse, self._client),
        )


class VideoToHdrResourceWithRawResponse:
    def __init__(self, video_to_hdr: VideoToHdrResource) -> None:
        self._video_to_hdr = video_to_hdr

        self.create = to_raw_response_wrapper(
            video_to_hdr.create,
        )


class AsyncVideoToHdrResourceWithRawResponse:
    def __init__(self, video_to_hdr: AsyncVideoToHdrResource) -> None:
        self._video_to_hdr = video_to_hdr

        self.create = async_to_raw_response_wrapper(
            video_to_hdr.create,
        )


class VideoToHdrResourceWithStreamingResponse:
    def __init__(self, video_to_hdr: VideoToHdrResource) -> None:
        self._video_to_hdr = video_to_hdr

        self.create = to_streamed_response_wrapper(
            video_to_hdr.create,
        )


class AsyncVideoToHdrResourceWithStreamingResponse:
    def __init__(self, video_to_hdr: AsyncVideoToHdrResource) -> None:
        self._video_to_hdr = video_to_hdr

        self.create = async_to_streamed_response_wrapper(
            video_to_hdr.create,
        )
