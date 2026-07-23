# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types.generate import ImageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RunwayML) -> None:
        image = client.generate.image.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        )
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RunwayML) -> None:
        image = client.generate.image.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "aspect_ratio": "16:9",
                "content_moderation": {"public_figure_threshold": "auto"},
                "output_count": 1,
                "reference_images": [{"uri": "https://example.com/file"}],
                "resolution": "1k",
                "seed": 0,
            },
        )
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RunwayML) -> None:
        response = client.generate.image.with_raw_response.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RunwayML) -> None:
        with client.generate.image.with_streaming_response.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageCreateResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRunwayML) -> None:
        image = await async_client.generate.image.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        )
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRunwayML) -> None:
        image = await async_client.generate.image.create(
            config_id="n6_",
            input={
                "prompt_text": "x",
                "aspect_ratio": "16:9",
                "content_moderation": {"public_figure_threshold": "auto"},
                "output_count": 1,
                "reference_images": [{"uri": "https://example.com/file"}],
                "resolution": "1k",
                "seed": 0,
            },
        )
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.generate.image.with_raw_response.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageCreateResponse, image, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRunwayML) -> None:
        async with async_client.generate.image.with_streaming_response.create(
            config_id="n6_",
            input={"prompt_text": "x"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageCreateResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True
