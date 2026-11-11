from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from runwayml import RunwayML, AsyncRunwayML


@pytest.mark.parametrize("resource", ["image_to_vector", "text_to_music"])
def test_new_resources_wait_for_created_task(resource: str) -> None:
    paths: list[str] = []
    request_bodies: list[dict[str, object]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        paths.append(request.url.path)
        if request.method == "POST":
            request_bodies.append(json.loads(request.read()))
            return httpx.Response(200, json={"id": "task-1", "estimatedCost": {"credits": 2}})
        return httpx.Response(
            200,
            json={
                "id": "task-1",
                "createdAt": "2026-01-01T00:00:00Z",
                "status": "SUCCEEDED",
                "output": ["https://example.com/output"],
                "cost": {"credits": 2},
            },
        )

    with RunwayML(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handler))) as client:
        if resource == "image_to_vector":
            response = client.image_to_vector.create(model="ideogram_vector", image_uri="https://example.com/input.png")
        else:
            response = client.text_to_music.create(model="eleven_music_v2_5", prompt_text="instrumental")
        assert response.estimated_cost.credits == 2
        with patch("runwayml.lib.polling.time.sleep"):
            result = response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/output"]
    assert paths == [f"/v1/{resource}", "/v1/tasks/task-1"]
    expected_body = (
        {"model": "ideogram_vector", "imageUri": "https://example.com/input.png"}
        if resource == "image_to_vector"
        else {"model": "eleven_music_v2_5", "promptText": "instrumental"}
    )
    assert request_bodies == [expected_body]


@pytest.mark.parametrize("resource", ["image_to_vector", "text_to_music"])
async def test_async_new_resources_wait_for_created_task(resource: str) -> None:
    paths: list[str] = []
    request_bodies: list[dict[str, object]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        paths.append(request.url.path)
        if request.method == "POST":
            request_bodies.append(json.loads(request.read()))
            return httpx.Response(200, json={"id": "task-1", "estimatedCost": {"credits": 2}})
        return httpx.Response(
            200,
            json={
                "id": "task-1",
                "createdAt": "2026-01-01T00:00:00Z",
                "status": "SUCCEEDED",
                "output": ["https://example.com/output"],
                "cost": {"credits": 2},
            },
        )

    async with AsyncRunwayML(
        api_key="test", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
    ) as client:
        if resource == "image_to_vector":
            response = await client.image_to_vector.create(
                model="ideogram_vector", image_uri="https://example.com/input.png"
            )
        else:
            response = await client.text_to_music.create(model="eleven_music_v2_5", prompt_text="instrumental")
        assert response.estimated_cost.credits == 2
        with patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock):
            result = await response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/output"]
    assert paths == [f"/v1/{resource}", "/v1/tasks/task-1"]
    expected_body = (
        {"model": "ideogram_vector", "imageUri": "https://example.com/input.png"}
        if resource == "image_to_vector"
        else {"model": "eleven_music_v2_5", "promptText": "instrumental"}
    )
    assert request_bodies == [expected_body]
