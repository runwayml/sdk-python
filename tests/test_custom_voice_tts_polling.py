from __future__ import annotations

import json
from typing import Literal
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from runwayml import RunwayML, AsyncRunwayML

Model = Literal["eleven_multilingual_v2", "eleven_v3", "eleven_v4"]
VOICE_ID = "4c42c9dc-d99e-44ea-8e3b-c54e077ed374"


def transport_for(model: Model) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "POST":
            assert request.url.path == "/v1/text_to_speech"
            assert json.loads(request.read()) == {
                "model": model,
                "promptText": "Hello",
                "voice": {"type": "custom", "id": VOICE_ID},
            }
            return httpx.Response(200, json={"id": "task-1", "estimatedCost": {"credits": 1}})
        assert request.url.path == "/v1/tasks/task-1"
        return httpx.Response(
            200,
            json={
                "id": "task-1",
                "createdAt": "2026-11-11T00:00:00Z",
                "status": "SUCCEEDED",
                "output": ["https://example.com/speech.mp3"],
            },
        )

    return httpx.MockTransport(handler)


@pytest.mark.parametrize("model", ["eleven_multilingual_v2", "eleven_v3", "eleven_v4"])
def test_custom_voice_speech_response_remains_waitable(model: Model) -> None:
    with RunwayML(api_key="test", http_client=httpx.Client(transport=transport_for(model))) as client:
        response = client.text_to_speech.create(
            model=model, prompt_text="Hello", voice={"type": "custom", "id": VOICE_ID}
        )
        assert response.to_dict()["estimatedCost"] == {"credits": 1}
        with patch("runwayml.lib.polling.time.sleep"):
            result = response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/speech.mp3"]


@pytest.mark.parametrize("model", ["eleven_multilingual_v2", "eleven_v3", "eleven_v4"])
async def test_async_custom_voice_speech_response_remains_waitable(model: Model) -> None:
    async with AsyncRunwayML(api_key="test", http_client=httpx.AsyncClient(transport=transport_for(model))) as client:
        response = await client.text_to_speech.create(
            model=model, prompt_text="Hello", voice={"type": "custom", "id": VOICE_ID}
        )
        assert response.to_dict()["estimatedCost"] == {"credits": 1}
        with patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock):
            result = await response.wait_for_task_output()
        assert result.status == "SUCCEEDED"
        assert result.output == ["https://example.com/speech.mp3"]
