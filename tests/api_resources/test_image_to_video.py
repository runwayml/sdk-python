# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import ImageToVideoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImageToVideo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        image_to_video = client.image_to_video.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        )
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        image_to_video = client.image_to_video.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
            duration=5,
            prompt_text="promptText",
            ratio="16:9",
            seed=0,
            watermark=True,
        )
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.image_to_video.with_raw_response.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image_to_video = response.parse()
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.image_to_video.with_streaming_response.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image_to_video = response.parse()
            assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImageToVideo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        image_to_video = await async_client.image_to_video.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        )
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        image_to_video = await async_client.image_to_video.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
            duration=5,
            prompt_text="promptText",
            ratio="16:9",
            seed=0,
            watermark=True,
        )
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.image_to_video.with_raw_response.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image_to_video = await response.parse()
        assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.image_to_video.with_streaming_response.create(
            model="gen3a_turbo",
            prompt_image="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image_to_video = await response.parse()
            assert_matches_type(ImageToVideoCreateResponse, image_to_video, path=["response"])

        assert cast(Any, response.is_closed) is True
