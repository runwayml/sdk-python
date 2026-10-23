from __future__ import annotations

from unittest.mock import AsyncMock, patch

import httpx

from runwayml import RunwayML, AsyncRunwayML


def test_video_to_audio_waits_for_created_task() -> None:
    paths: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        paths.append(request.url.path)
        if request.method == "POST":
            return httpx.Response(200, json={"id": "task-1", "estimatedCost": {"credits": 2}})
        return httpx.Response(
            200,
            json={
                "id": "task-1",
                "createdAt": "2026-01-01T00:00:00Z",
                "status": "SUCCEEDED",
                "output": ["https://example.com/audio.mp3"],
            },
        )

    with RunwayML(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handler))) as client:
        response = client.video_to_audio.create(
            duration=5, model="mirelo_sfx_2_0", video_uri="https://example.com/video.mp4"
        )
        assert response.estimated_cost.credits == 2
        with patch("runwayml.lib.polling.time.sleep"):
            result = response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/audio.mp3"]
    assert paths == ["/v1/video_to_audio", "/v1/tasks/task-1"]


async def test_async_video_to_audio_waits_for_created_task() -> None:
    paths: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        paths.append(request.url.path)
        if request.method == "POST":
            return httpx.Response(200, json={"id": "task-1", "estimatedCost": {"credits": 2}})
        return httpx.Response(
            200,
            json={
                "id": "task-1",
                "createdAt": "2026-01-01T00:00:00Z",
                "status": "SUCCEEDED",
                "output": ["https://example.com/audio.mp3"],
            },
        )

    async with AsyncRunwayML(
        api_key="test", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
    ) as client:
        response = await client.video_to_audio.create(
            duration=5, model="mirelo_sfx_2_0", video_uri="https://example.com/video.mp4"
        )
        assert response.estimated_cost.credits == 2
        with patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock):
            result = await response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/audio.mp3"]
    assert paths == ["/v1/video_to_audio", "/v1/tasks/task-1"]
