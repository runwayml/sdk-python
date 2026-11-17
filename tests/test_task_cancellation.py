from __future__ import annotations

from typing import Any

import anyio
import httpx
import pytest

from runwayml import RunwayML, AsyncRunwayML, TaskFailedError


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("entry_point", ["create", "retrieve"])
@pytest.mark.parametrize("status", ["CANCELLED", "FAILED", "SUCCEEDED"])
async def test_public_task_wait_handles_terminal_status(
    monkeypatch: pytest.MonkeyPatch, asynchronous: bool, entry_point: str, status: str
) -> None:
    monkeypatch.setattr("runwayml.lib.polling.time.sleep", lambda _delay: None)

    async def no_sleep(_delay: float) -> None:
        pass

    monkeypatch.setattr(anyio, "sleep", no_sleep)
    gets = 0
    expected_gets = 2 if entry_point == "retrieve" else 1

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal gets
        if request.method == "POST":
            return httpx.Response(200, json={"id": "task-example"})
        gets += 1
        assert gets <= expected_gets, "polled again after a terminal task response"
        payload: dict[str, Any] = {
            "id": "task-example",
            "createdAt": "2026-01-01T00:00:00Z",
            "status": status,
            "cost": {"credits": 0},
        }
        if status == "FAILED":
            payload["failure"] = "test failure"
        if status == "SUCCEEDED":
            payload["output"] = ["https://example.com/output.png"]
        return httpx.Response(200, json=payload)

    if asynchronous:
        async with AsyncRunwayML(
            api_key="test", max_retries=0, http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
        ) as client:
            response = (
                await client.generate.image.create(config_id="test", input={"prompt_text": "A test image"})
                if entry_point == "create"
                else await client.tasks.retrieve("task-example")
            )
            if status == "SUCCEEDED":
                assert (await response.wait_for_task_output()).status == status
            else:
                with pytest.raises(TaskFailedError) as error:
                    await response.wait_for_task_output()
                assert error.value.task_details.status == status
    else:
        with RunwayML(
            api_key="test", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(respond))
        ) as sync_client:
            sync_response = (
                sync_client.generate.image.create(config_id="test", input={"prompt_text": "A test image"})
                if entry_point == "create"
                else sync_client.tasks.retrieve("task-example")
            )
            if status == "SUCCEEDED":
                assert sync_response.wait_for_task_output().status == status
            else:
                with pytest.raises(TaskFailedError) as sync_error:
                    sync_response.wait_for_task_output()
                assert sync_error.value.task_details.status == status
    assert gets == expected_gets
