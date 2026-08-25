# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import video_to_video_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..lib.polling import (
    NewTaskCreatedResponse,
    AsyncNewTaskCreatedResponse,
    create_waitable_resource,
    create_async_waitable_resource,
)
from .._base_client import make_request_options
from ..types.video_to_video_create_response import VideoToVideoCreateResponse

__all__ = ["VideoToVideoResource", "AsyncVideoToVideoResource"]


class VideoToVideoResource(SyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> VideoToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return VideoToVideoResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: Literal["aleph2"],
        video_uri: str,
        content_moderation: video_to_video_create_params.Variant0ContentModeration | Omit = omit,
        keyframes: Iterable[video_to_video_create_params.Variant0Keyframe] | Omit = omit,
        output_format: Literal["mp4", "prores", "png_sequence", "sdr_rec709_10bit"] | Omit = omit,
        prompt_text: str | Omit = omit,
        prores_profile: Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"] | Omit = omit,
        ratio: str | Omit = omit,
        seed: int | Omit = omit,
        target_aspect_ratio: Literal["16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "21:9"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          content_moderation: Settings that affect the behavior of the content moderation system.

          keyframes: Timed guidance images placed at specific points in the input video. Up to 5
              keyframes.

          output_format: The container/encoding of the output. `mp4` (default) returns an H.264 .mp4.
              `prores` returns a ProRes .mov. `png_sequence` returns a .zip of PNG frames.
              `sdr_rec709_10bit` returns a 10-bit Rec.709 HEVC .mp4 for SDR grading pipelines.
              Non-mp4 formats incur an additional surcharge: 5 credits per second for `prores`
              and `png_sequence`, and 20 credits per second for `sdr_rec709_10bit` — 40
              credits per second when the output is larger than 4 megapixels (roughly 4K).

          prompt_text: A non-empty and optional string describing what should appear in the output.

          prores_profile: The ProRes profile to use. Only valid when `outputFormat` is `prores`. Defaults
              to `4444`.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          target_aspect_ratio: Target aspect ratio for expand/outpaint. Letterboxes the input video and
              keyframes before generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["hailuo3"],
        prompt_text: str,
        prompt_video: str,
        duration: int | Omit = omit,
        ratio: Literal["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"] | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Hailuo3ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Hailuo3Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Hailuo3ReferenceVideo] | Omit = omit,
        resolution: Literal["2K", "768P"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty text prompt describing what should appear in the output.

          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          duration: The number of seconds of duration for the output video.

          ratio: The aspect ratio of the output video. Use adaptive only when image or video
              references are provided; text-only requests require a concrete ratio.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          resolution: The output resolution. MiniMax H3 supports 768P and 2K.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["seedance2"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["seedance2_fast"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2FastReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2FastReference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2FastReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["seedance2_mini"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2MiniReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2MiniReference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2MiniReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["gemini_omni_flash"],
        prompt_text: str,
        video_uri: str,
        references: Iterable[video_to_video_create_params.GeminiOmniFlashReference] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty instruction describing the edit to apply.

          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          references: An optional array of image references to guide the edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: Literal["seedance2_5"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        mode: Literal["reference", "extend"] | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "854:480",
            "752:560",
            "640:640",
            "560:752",
            "480:854",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2_5ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2_5Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2_5ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video. Defaults to 5.

          mode: How the input video is used. `reference` (the default) generates a new video
              conditioned on the input video and accepts `duration` and `ratio`. `extend`
              continues the input video, requires `promptText`, and matches the input aspect
              ratio, so `ratio` may not be provided.

          prompt_text: An optional text prompt up to 15000 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.5 supports 480p, 720p, and 1080p.

          reference_audio: An optional array of audio references. The total combined duration must be less
              than 30 seconds.

          references: An optional array of image references (up to 30). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "video_uri"],
        ["model", "prompt_text", "prompt_video"],
        ["model", "prompt_video"],
        ["model", "prompt_text", "video_uri"],
    )
    def create(
        self,
        *,
        model: Literal["aleph2"]
        | Literal["hailuo3"]
        | Literal["seedance2"]
        | Literal["seedance2_fast"]
        | Literal["seedance2_mini"]
        | Literal["gemini_omni_flash"]
        | Literal["seedance2_5"],
        video_uri: str | Omit = omit,
        content_moderation: video_to_video_create_params.Variant0ContentModeration | Omit = omit,
        keyframes: Iterable[video_to_video_create_params.Variant0Keyframe] | Omit = omit,
        output_format: Literal["mp4", "prores", "png_sequence", "sdr_rec709_10bit"] | Omit = omit,
        prompt_text: str | Omit = omit,
        prores_profile: Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"] | Omit = omit,
        ratio: str
        | Literal["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Literal[
            "992:432",
            "854:480",
            "752:560",
            "640:640",
            "560:752",
            "480:854",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
        ]
        | Omit = omit,
        seed: int | Omit = omit,
        target_aspect_ratio: Literal["16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "21:9"] | Omit = omit,
        prompt_video: str | Omit = omit,
        duration: int | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Hailuo3ReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2ReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2FastReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2MiniReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2_5ReferenceAudio]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Hailuo3Reference]
        | Iterable[video_to_video_create_params.Seedance2Reference]
        | Iterable[video_to_video_create_params.Seedance2FastReference]
        | Iterable[video_to_video_create_params.Seedance2MiniReference]
        | Iterable[video_to_video_create_params.GeminiOmniFlashReference]
        | Iterable[video_to_video_create_params.Seedance2_5Reference]
        | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Hailuo3ReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2ReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2FastReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2MiniReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2_5ReferenceVideo]
        | Omit = omit,
        resolution: Literal["2K", "768P"] | Omit = omit,
        audio: bool | Omit = omit,
        mode: Literal["reference", "extend"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewTaskCreatedResponse:
        return self._post(
            "/v1/video_to_video",
            body=maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "keyframes": keyframes,
                    "output_format": output_format,
                    "prompt_text": prompt_text,
                    "prores_profile": prores_profile,
                    "ratio": ratio,
                    "seed": seed,
                    "target_aspect_ratio": target_aspect_ratio,
                    "prompt_video": prompt_video,
                    "duration": duration,
                    "reference_audio": reference_audio,
                    "references": references,
                    "reference_videos": reference_videos,
                    "resolution": resolution,
                    "audio": audio,
                    "mode": mode,
                },
                video_to_video_create_params.VideoToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_waitable_resource(VideoToVideoCreateResponse, self._client),
        )


class AsyncVideoToVideoResource(AsyncAPIResource):
    """These endpoints all kick off tasks to create generations."""

    @cached_property
    def with_raw_response(self) -> AsyncVideoToVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/runwayml/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoToVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoToVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/runwayml/sdk-python#with_streaming_response
        """
        return AsyncVideoToVideoResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: Literal["aleph2"],
        video_uri: str,
        content_moderation: video_to_video_create_params.Variant0ContentModeration | Omit = omit,
        keyframes: Iterable[video_to_video_create_params.Variant0Keyframe] | Omit = omit,
        output_format: Literal["mp4", "prores", "png_sequence", "sdr_rec709_10bit"] | Omit = omit,
        prompt_text: str | Omit = omit,
        prores_profile: Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"] | Omit = omit,
        ratio: str | Omit = omit,
        seed: int | Omit = omit,
        target_aspect_ratio: Literal["16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "21:9"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          content_moderation: Settings that affect the behavior of the content moderation system.

          keyframes: Timed guidance images placed at specific points in the input video. Up to 5
              keyframes.

          output_format: The container/encoding of the output. `mp4` (default) returns an H.264 .mp4.
              `prores` returns a ProRes .mov. `png_sequence` returns a .zip of PNG frames.
              `sdr_rec709_10bit` returns a 10-bit Rec.709 HEVC .mp4 for SDR grading pipelines.
              Non-mp4 formats incur an additional surcharge: 5 credits per second for `prores`
              and `png_sequence`, and 20 credits per second for `sdr_rec709_10bit` — 40
              credits per second when the output is larger than 4 megapixels (roughly 4K).

          prompt_text: A non-empty and optional string describing what should appear in the output.

          prores_profile: The ProRes profile to use. Only valid when `outputFormat` is `prores`. Defaults
              to `4444`.

          seed: If unspecified, a random number is chosen. Varying the seed integer is a way to
              get different results for the same other request parameters. Using the same seed
              integer for an identical request will produce similar results.

          target_aspect_ratio: Target aspect ratio for expand/outpaint. Letterboxes the input video and
              keyframes before generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["hailuo3"],
        prompt_text: str,
        prompt_video: str,
        duration: int | Omit = omit,
        ratio: Literal["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"] | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Hailuo3ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Hailuo3Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Hailuo3ReferenceVideo] | Omit = omit,
        resolution: Literal["2K", "768P"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty text prompt describing what should appear in the output.

          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          duration: The number of seconds of duration for the output video.

          ratio: The aspect ratio of the output video. Use adaptive only when image or video
              references are provided; text-only requests require a concrete ratio.

          reference_audio: An optional array of audio references. Audio references require a text prompt,
              and the total combined duration must not exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          resolution: The output resolution. MiniMax H3 supports 768P and 2K.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["seedance2"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["seedance2_fast"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2FastReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2FastReference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2FastReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["seedance2_mini"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2MiniReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2MiniReference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2MiniReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video.

          prompt_text: An optional text prompt up to 3500 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p
              only.

          reference_audio: An optional array of audio references. The total combined duration must not
              exceed 15 seconds.

          references: An optional array of image references (up to 9). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["gemini_omni_flash"],
        prompt_text: str,
        video_uri: str,
        references: Iterable[video_to_video_create_params.GeminiOmniFlashReference] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_text: A non-empty instruction describing the edit to apply.

          video_uri: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          references: An optional array of image references to guide the edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: Literal["seedance2_5"],
        prompt_video: str,
        audio: bool | Omit = omit,
        duration: int | Omit = omit,
        mode: Literal["reference", "extend"] | Omit = omit,
        prompt_text: str | Omit = omit,
        ratio: Literal[
            "992:432",
            "854:480",
            "752:560",
            "640:640",
            "560:752",
            "480:854",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
        ]
        | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Seedance2_5ReferenceAudio] | Omit = omit,
        references: Iterable[video_to_video_create_params.Seedance2_5Reference] | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Seedance2_5ReferenceVideo] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        """
        This endpoint will start a new task to generate a video from a video.

        Args:
          prompt_video: A HTTPS URL, Runway upload URI, or base64 data URI (e.g.
              `data:video/mp4;base64,...`, up to 16MB) containing an encoded video. See
              [our docs](/assets/inputs#videos) on video inputs for more information.

          audio: Whether to generate audio for the video.

          duration: The number of seconds of duration for the output video. Defaults to 5.

          mode: How the input video is used. `reference` (the default) generates a new video
              conditioned on the input video and accepts `duration` and `ratio`. `extend`
              continues the input video, requires `promptText`, and matches the input aspect
              ratio, so `ratio` may not be provided.

          prompt_text: An optional text prompt up to 15000 characters describing what should appear in
              the output.

          ratio: The resolution of the output video. Seedance 2.5 supports 480p, 720p, and 1080p.

          reference_audio: An optional array of audio references. The total combined duration must be less
              than 30 seconds.

          references: An optional array of image references (up to 30). See
              [our docs](/assets/inputs#images) on image inputs for more information.

          reference_videos: An optional array of video references. The combined duration across all video
              references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on
              video inputs for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["model", "video_uri"],
        ["model", "prompt_text", "prompt_video"],
        ["model", "prompt_video"],
        ["model", "prompt_text", "video_uri"],
    )
    async def create(
        self,
        *,
        model: Literal["aleph2"]
        | Literal["hailuo3"]
        | Literal["seedance2"]
        | Literal["seedance2_fast"]
        | Literal["seedance2_mini"]
        | Literal["gemini_omni_flash"]
        | Literal["seedance2_5"],
        video_uri: str | Omit = omit,
        content_moderation: video_to_video_create_params.Variant0ContentModeration | Omit = omit,
        keyframes: Iterable[video_to_video_create_params.Variant0Keyframe] | Omit = omit,
        output_format: Literal["mp4", "prores", "png_sequence", "sdr_rec709_10bit"] | Omit = omit,
        prompt_text: str | Omit = omit,
        prores_profile: Literal["422", "4444", "422 Proxy", "422 LT", "422 HQ", "4444 XQ"] | Omit = omit,
        ratio: str
        | Literal["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
            "3840:1646",
            "3840:2160",
            "3840:2880",
            "3840:3840",
            "2880:3840",
            "2160:3840",
        ]
        | Literal[
            "992:432",
            "864:496",
            "752:560",
            "640:640",
            "560:752",
            "496:864",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
        ]
        | Literal[
            "992:432",
            "854:480",
            "752:560",
            "640:640",
            "560:752",
            "480:854",
            "1470:630",
            "1280:720",
            "1112:834",
            "960:960",
            "834:1112",
            "720:1280",
            "2206:946",
            "1920:1080",
            "1664:1248",
            "1440:1440",
            "1248:1664",
            "1080:1920",
        ]
        | Omit = omit,
        seed: int | Omit = omit,
        target_aspect_ratio: Literal["16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "21:9"] | Omit = omit,
        prompt_video: str | Omit = omit,
        duration: int | Omit = omit,
        reference_audio: Iterable[video_to_video_create_params.Hailuo3ReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2ReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2FastReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2MiniReferenceAudio]
        | Iterable[video_to_video_create_params.Seedance2_5ReferenceAudio]
        | Omit = omit,
        references: Iterable[video_to_video_create_params.Hailuo3Reference]
        | Iterable[video_to_video_create_params.Seedance2Reference]
        | Iterable[video_to_video_create_params.Seedance2FastReference]
        | Iterable[video_to_video_create_params.Seedance2MiniReference]
        | Iterable[video_to_video_create_params.GeminiOmniFlashReference]
        | Iterable[video_to_video_create_params.Seedance2_5Reference]
        | Omit = omit,
        reference_videos: Iterable[video_to_video_create_params.Hailuo3ReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2ReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2FastReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2MiniReferenceVideo]
        | Iterable[video_to_video_create_params.Seedance2_5ReferenceVideo]
        | Omit = omit,
        resolution: Literal["2K", "768P"] | Omit = omit,
        audio: bool | Omit = omit,
        mode: Literal["reference", "extend"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNewTaskCreatedResponse:
        return await self._post(
            "/v1/video_to_video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "video_uri": video_uri,
                    "content_moderation": content_moderation,
                    "keyframes": keyframes,
                    "output_format": output_format,
                    "prompt_text": prompt_text,
                    "prores_profile": prores_profile,
                    "ratio": ratio,
                    "seed": seed,
                    "target_aspect_ratio": target_aspect_ratio,
                    "prompt_video": prompt_video,
                    "duration": duration,
                    "reference_audio": reference_audio,
                    "references": references,
                    "reference_videos": reference_videos,
                    "resolution": resolution,
                    "audio": audio,
                    "mode": mode,
                },
                video_to_video_create_params.VideoToVideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=create_async_waitable_resource(VideoToVideoCreateResponse, self._client),
        )


class VideoToVideoResourceWithRawResponse:
    def __init__(self, video_to_video: VideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = to_raw_response_wrapper(
            video_to_video.create,
        )


class AsyncVideoToVideoResourceWithRawResponse:
    def __init__(self, video_to_video: AsyncVideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = async_to_raw_response_wrapper(
            video_to_video.create,
        )


class VideoToVideoResourceWithStreamingResponse:
    def __init__(self, video_to_video: VideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = to_streamed_response_wrapper(
            video_to_video.create,
        )


class AsyncVideoToVideoResourceWithStreamingResponse:
    def __init__(self, video_to_video: AsyncVideoToVideoResource) -> None:
        self._video_to_video = video_to_video

        self.create = async_to_streamed_response_wrapper(
            video_to_video.create,
        )
