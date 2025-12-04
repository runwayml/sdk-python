# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from runwayml import RunwayML, AsyncRunwayML
from tests.utils import assert_matches_type
from runwayml.types import TextToImageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
            content_moderation={"public_figure_threshold": "auto"},
            seed=0,
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: RunwayML) -> None:
        response = client.text_to_image.with_raw_response.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: RunwayML) -> None:
        with client.text_to_image.with_streaming_response.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
            content_moderation={"public_figure_threshold": "auto"},
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
            seed=0,
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: RunwayML) -> None:
        response = client.text_to_image.with_raw_response.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: RunwayML) -> None:
        with client.text_to_image.with_streaming_response.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: RunwayML) -> None:
        text_to_image = client.text_to_image.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: RunwayML) -> None:
        response = client.text_to_image.with_raw_response.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: RunwayML) -> None:
        with client.text_to_image.with_streaming_response.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToImage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
            content_moderation={"public_figure_threshold": "auto"},
            seed=0,
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_image.with_raw_response.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = await response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_image.with_streaming_response.create(
            model="gen4_image_turbo",
            prompt_text="x",
            ratio="1024:1024",
            reference_images=[{"uri": "https://example.com/file"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = await response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
            content_moderation={"public_figure_threshold": "auto"},
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
            seed=0,
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_image.with_raw_response.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = await response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_image.with_streaming_response.create(
            model="gen4_image",
            prompt_text="x",
            ratio="1024:1024",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = await response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncRunwayML) -> None:
        text_to_image = await async_client.text_to_image.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
            reference_images=[
                {
                    "uri": "https://example.com/file",
                    "tag": "tag",
                }
            ],
        )
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncRunwayML) -> None:
        response = await async_client.text_to_image.with_raw_response.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_image = await response.parse()
        assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncRunwayML) -> None:
        async with async_client.text_to_image.with_streaming_response.create(
            model="gemini_2.5_flash",
            prompt_text="x",
            ratio="1344:768",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_image = await response.parse()
            assert_matches_type(TextToImageCreateResponse, text_to_image, path=["response"])

        assert cast(Any, response.is_closed) is True
