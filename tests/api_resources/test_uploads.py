# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import io
import os
from typing import Any
from pathlib import Path

import httpx
import pytest
from respx import MockRouter

from runwayml import RunwayML, AsyncRunwayML

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
sample_file = Path(__file__).parent.parent / "sample_file.txt"


class TestUploads:
    @pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])
    @pytest.mark.parametrize(
        "file",
        [
            b"raw bytes content",
            io.BytesIO(b"content"),
            (None, b"content"),
        ],
        ids=["raw_bytes", "bytesio_no_name", "tuple_none_filename"],
    )
    def test_create_ephemeral_rejects_invalid_files(self, client: RunwayML, file: Any) -> None:
        """Files without inferrable filename should be rejected with clear error."""
        with pytest.raises(ValueError, match="Cannot infer filename from file"):
            client.uploads.create_ephemeral(file=file)

    @pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])
    @pytest.mark.respx
    @pytest.mark.parametrize(
        "file_type",
        ["path", "tuple", "file_object"],
        ids=["path", "tuple_with_filename", "file_object_with_name"],
    )
    def test_create_ephemeral_accepts_valid_files(
        self, respx_mock: MockRouter, client: RunwayML, file_type: str
    ) -> None:
        """Files with inferrable filename should be accepted."""
        if file_type == "path":
            file: Any = sample_file
        elif file_type == "tuple":
            file = ("test.txt", b"content")
        else:  # file_object
            file = open(sample_file, "rb")

        respx_mock.post(f"{base_url}/v1/uploads").mock(
            return_value=httpx.Response(
                200,
                json={
                    "runwayUri": "runway://upload/test123",
                    "uploadUrl": "https://storage.example.com/upload",
                    "fields": {"key": "value"},
                },
            )
        )
        respx_mock.post("https://storage.example.com/upload").mock(return_value=httpx.Response(204))

        try:
            response = client.uploads.create_ephemeral(file=file)
            assert response.uri == "runway://upload/test123"
        finally:
            if file_type == "file_object":
                file.close()


class TestAsyncUploads:
    @pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])
    @pytest.mark.parametrize(
        "file",
        [
            b"raw bytes content",
            io.BytesIO(b"content"),
            (None, b"content"),
        ],
        ids=["raw_bytes", "bytesio_no_name", "tuple_none_filename"],
    )
    async def test_create_ephemeral_rejects_invalid_files(self, async_client: AsyncRunwayML, file: Any) -> None:
        """Files without inferrable filename should be rejected with clear error."""
        with pytest.raises(ValueError, match="Cannot infer filename from file"):
            await async_client.uploads.create_ephemeral(file=file)

    @pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])
    @pytest.mark.respx
    @pytest.mark.parametrize(
        "file_type",
        ["path", "tuple", "file_object"],
        ids=["path", "tuple_with_filename", "file_object_with_name"],
    )
    async def test_create_ephemeral_accepts_valid_files(
        self, respx_mock: MockRouter, async_client: AsyncRunwayML, file_type: str
    ) -> None:
        """Files with inferrable filename should be accepted."""
        if file_type == "path":
            file: Any = sample_file
        elif file_type == "tuple":
            file = ("test.txt", b"content")
        else:  # file_object
            file = open(sample_file, "rb")

        respx_mock.post(f"{base_url}/v1/uploads").mock(
            return_value=httpx.Response(
                200,
                json={
                    "runwayUri": "runway://upload/test123",
                    "uploadUrl": "https://storage.example.com/upload",
                    "fields": {"key": "value"},
                },
            )
        )
        respx_mock.post("https://storage.example.com/upload").mock(return_value=httpx.Response(204))

        try:
            response = await async_client.uploads.create_ephemeral(file=file)
            assert response.uri == "runway://upload/test123"
        finally:
            if file_type == "file_object":
                file.close()

