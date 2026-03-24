from __future__ import annotations

from typing import Any
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from runwayml import RunwayML, AsyncRunwayML, TaskFailedError, TaskTimeoutError
from runwayml.types.workflow_invocation_retrieve_response import (
    Failed,
    Pending,
    Cancelled,
    Succeeded,
)


def _make_pending(id: str = "inv-1") -> Pending:
    return Pending(id=id, createdAt=datetime.now(tz=timezone.utc), status="PENDING")


def _make_succeeded(id: str = "inv-1") -> Succeeded:
    return Succeeded(
        id=id,
        createdAt=datetime.now(tz=timezone.utc),
        status="SUCCEEDED",
        output={"node-1": ["https://example.com/output.mp4"]},
    )


def _make_failed(id: str = "inv-1") -> Failed:
    return Failed(
        id=id,
        createdAt=datetime.now(tz=timezone.utc),
        status="FAILED",
        failure="Generation failed",
    )


def _make_cancelled(id: str = "inv-1") -> Cancelled:
    return Cancelled(id=id, createdAt=datetime.now(tz=timezone.utc), status="CANCELLED")


class TestSyncWorkflowInvocationPolling:
    @patch("runwayml.lib.polling.time.sleep", return_value=None)
    def test_resolves_on_succeeded(self, _mock_sleep: MagicMock) -> None:
        client = MagicMock(spec=RunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = MagicMock(return_value=_make_succeeded())

        from runwayml.lib.polling import inject_sync_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_sync_workflow_invocation_wait_method(client, response)
        result = patched.wait_for_task_output()

        assert result.status == "SUCCEEDED"
        client.workflow_invocations.retrieve.assert_called_once_with(response.id)

    @patch("runwayml.lib.polling.time.sleep", return_value=None)
    def test_polls_until_succeeded(self, _mock_sleep: MagicMock) -> None:
        client = MagicMock(spec=RunwayML)
        client.workflow_invocations = MagicMock()
        responses = [_make_pending(), _make_pending(), _make_succeeded()]
        client.workflow_invocations.retrieve = MagicMock(side_effect=responses)

        from runwayml.lib.polling import inject_sync_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_sync_workflow_invocation_wait_method(client, response)
        result = patched.wait_for_task_output()

        assert result.status == "SUCCEEDED"
        assert client.workflow_invocations.retrieve.call_count == 3

    @patch("runwayml.lib.polling.time.sleep", return_value=None)
    def test_raises_on_failed(self, _mock_sleep: MagicMock) -> None:
        client = MagicMock(spec=RunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = MagicMock(return_value=_make_failed())

        from runwayml.lib.polling import inject_sync_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_sync_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskFailedError) as exc_info:
            patched.wait_for_task_output()

        assert exc_info.value.task_details.status == "FAILED"

    @patch("runwayml.lib.polling.time.sleep", return_value=None)
    def test_raises_on_cancelled(self, _mock_sleep: MagicMock) -> None:
        client = MagicMock(spec=RunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = MagicMock(return_value=_make_cancelled())

        from runwayml.lib.polling import inject_sync_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_sync_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskFailedError) as exc_info:
            patched.wait_for_task_output()

        assert exc_info.value.task_details.status == "CANCELLED"

    @patch("runwayml.lib.polling.time.time")
    @patch("runwayml.lib.polling.time.sleep", return_value=None)
    def test_raises_on_timeout(self, _mock_sleep: MagicMock, mock_time: MagicMock) -> None:
        mock_time.side_effect = [0.0, 700.0]

        client = MagicMock(spec=RunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = MagicMock(return_value=_make_pending())

        from runwayml.lib.polling import inject_sync_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_sync_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskTimeoutError):
            patched.wait_for_task_output(timeout=600)


class TestAsyncWorkflowInvocationPolling:
    @patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock)
    @patch("runwayml.lib.polling.anyio.current_time", return_value=0.0)
    async def test_resolves_on_succeeded(self, _mock_time: MagicMock, _mock_sleep: AsyncMock) -> None:
        client = MagicMock(spec=AsyncRunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = AsyncMock(return_value=_make_succeeded())

        from runwayml.lib.polling import inject_async_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_async_workflow_invocation_wait_method(client, response)
        result = await patched.wait_for_task_output()

        assert result.status == "SUCCEEDED"
        client.workflow_invocations.retrieve.assert_called_once_with(response.id)

    @patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock)
    @patch("runwayml.lib.polling.anyio.current_time", return_value=0.0)
    async def test_polls_until_succeeded(self, _mock_time: MagicMock, _mock_sleep: AsyncMock) -> None:
        client = MagicMock(spec=AsyncRunwayML)
        client.workflow_invocations = MagicMock()
        responses = [_make_pending(), _make_pending(), _make_succeeded()]
        client.workflow_invocations.retrieve = AsyncMock(side_effect=responses)

        from runwayml.lib.polling import inject_async_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_async_workflow_invocation_wait_method(client, response)
        result = await patched.wait_for_task_output()

        assert result.status == "SUCCEEDED"
        assert client.workflow_invocations.retrieve.call_count == 3

    @patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock)
    @patch("runwayml.lib.polling.anyio.current_time", return_value=0.0)
    async def test_raises_on_failed(self, _mock_time: MagicMock, _mock_sleep: AsyncMock) -> None:
        client = MagicMock(spec=AsyncRunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = AsyncMock(return_value=_make_failed())

        from runwayml.lib.polling import inject_async_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_async_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskFailedError) as exc_info:
            await patched.wait_for_task_output()

        assert exc_info.value.task_details.status == "FAILED"

    @patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock)
    @patch("runwayml.lib.polling.anyio.current_time", return_value=0.0)
    async def test_raises_on_cancelled(self, _mock_time: MagicMock, _mock_sleep: AsyncMock) -> None:
        client = MagicMock(spec=AsyncRunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = AsyncMock(return_value=_make_cancelled())

        from runwayml.lib.polling import inject_async_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_async_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskFailedError) as exc_info:
            await patched.wait_for_task_output()

        assert exc_info.value.task_details.status == "CANCELLED"

    @patch("runwayml.lib.polling.anyio.sleep", new_callable=AsyncMock)
    @patch("runwayml.lib.polling.anyio.current_time")
    async def test_raises_on_timeout(self, mock_time: MagicMock, _mock_sleep: AsyncMock) -> None:
        mock_time.side_effect = [0.0, 700.0]

        client = MagicMock(spec=AsyncRunwayML)
        client.workflow_invocations = MagicMock()
        client.workflow_invocations.retrieve = AsyncMock(return_value=_make_pending())

        from runwayml.lib.polling import inject_async_workflow_invocation_wait_method

        response = _make_pending()
        patched: Any = inject_async_workflow_invocation_wait_method(client, response)

        with pytest.raises(TaskTimeoutError):
            await patched.wait_for_task_output(timeout=600)
