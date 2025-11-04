# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import TextToVideoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToVideo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: RunwayML) -> None:
        text_to_video = client.text_to_video.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: RunwayML) -> None:
        text_to_video = client.text_to_video.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
            duration=4,
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: RunwayML) -> None:
        response = client.text_to_video.with_raw_response.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: RunwayML) -> None:
        with client.text_to_video.with_streaming_response.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: RunwayML) -> None:
        text_to_video = client.text_to_video.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: RunwayML) -> None:
        text_to_video = client.text_to_video.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
            duration=4,
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: RunwayML) -> None:
        response = client.text_to_video.with_raw_response.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: RunwayML) -> None:
        with client.text_to_video.with_streaming_response.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: RunwayML) -> None:
        text_to_video = client.text_to_video.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: RunwayML) -> None:
        response = client.text_to_video.with_raw_response.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: RunwayML) -> None:
        with client.text_to_video.with_streaming_response.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToVideo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_video = await async_client.text_to_video.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_video = await async_client.text_to_video.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
            duration=4,
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_video.with_raw_response.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = await response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_video.with_streaming_response.create(
            model="veo3.1",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = await response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        text_to_video = await async_client.text_to_video.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRunwayML) -> None:
        text_to_video = await async_client.text_to_video.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
            duration=4,
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_video.with_raw_response.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = await response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_video.with_streaming_response.create(
            model="veo3.1_fast",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = await response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncRunwayML) -> None:
        text_to_video = await async_client.text_to_video.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        )
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_video.with_raw_response.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_video = await response.parse()
        assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_video.with_streaming_response.create(
            duration=8,
            model="veo3",
            prompt_text="x",
            ratio="1280:720",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_video = await response.parse()
            assert_matches_type(TextToVideoCreateResponse, text_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True
