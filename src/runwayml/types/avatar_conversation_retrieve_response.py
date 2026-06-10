# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AvatarConversationRetrieveResponse",
    "InProgress",
    "InProgressAvatar",
    "InProgressAvatarRunwayPreset",
    "InProgressAvatarCustom",
    "InProgressTool",
    "InProgressTranscript",
    "InProgressTranscriptToolCall",
    "InProgressTranscriptToolResult",
    "Ended",
    "EndedAvatar",
    "EndedAvatarRunwayPreset",
    "EndedAvatarCustom",
    "EndedTool",
    "EndedTranscript",
    "EndedTranscriptToolCall",
    "EndedTranscriptToolResult",
    "Failed",
    "FailedAvatar",
    "FailedAvatarRunwayPreset",
    "FailedAvatarCustom",
    "FailedTool",
    "FailedTranscript",
    "FailedTranscriptToolCall",
    "FailedTranscriptToolResult",
]


class InProgressAvatarRunwayPreset(BaseModel):
    """A preset avatar."""

    preset_id: str = FieldInfo(alias="presetId")
    """The preset avatar ID."""

    type: Literal["runway-preset"]


class InProgressAvatarCustom(BaseModel):
    """A custom avatar created by the user."""

    id: Optional[str] = None
    """The custom avatar ID, or null if deleted."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to the avatar image, or null if unavailable."""

    name: Optional[str] = None
    """The avatar name, or null if unavailable."""

    type: Literal["custom"]


InProgressAvatar: TypeAlias = Annotated[
    Union[InProgressAvatarRunwayPreset, InProgressAvatarCustom, None], PropertyInfo(discriminator="type")
]


class InProgressTool(BaseModel):
    """Summary of a tool configured for the session."""

    description: str
    """A description of when and how the tool should be used."""

    name: str
    """The tool name."""

    type: Literal["client_event", "backend_rpc"]
    """The tool type."""


class InProgressTranscriptToolCall(BaseModel):
    """A tool invocation by the assistant."""

    arguments: Dict[str, object]
    """The arguments passed to the tool."""

    name: str
    """The name of the tool that was called."""

    id: Optional[str] = None
    """Optional identifier linking this call to its result."""


class InProgressTranscriptToolResult(BaseModel):
    """The result of a tool invocation."""

    name: str
    """The name of the tool that returned a result."""

    id: Optional[str] = None
    """Optional identifier linking this result to its call."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)
    """How long the tool call took in milliseconds."""

    error: Optional[str] = None
    """Error message if the tool call failed."""

    result: Union[Dict[str, object], str, None] = None
    """The tool result (object, string, or null)."""


class InProgressTranscript(BaseModel):
    """A single entry in the conversation transcript."""

    content: Optional[str] = None
    """The spoken text, or null for tool-only turns."""

    role: Literal["user", "assistant"]
    """Who produced this transcript entry."""

    timestamp: Optional[datetime] = None
    """When this entry occurred, or null if unavailable."""

    tool_calls: Optional[List[InProgressTranscriptToolCall]] = FieldInfo(alias="toolCalls", default=None)
    """Tool invocations made during this assistant turn.

    Only present on assistant entries.
    """

    tool_results: Optional[List[InProgressTranscriptToolResult]] = FieldInfo(alias="toolResults", default=None)
    """Tool results received during this assistant turn.

    Only present on assistant entries.
    """


class InProgress(BaseModel):
    """A conversation that is currently active."""

    id: str
    """Unique conversation identifier.

    This is the same value as the realtime session ID for the call.
    """

    avatar: Optional[InProgressAvatar] = None
    """The avatar used in this conversation."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the conversation was created."""

    duration: Optional[int] = None
    """Elapsed duration in seconds, or null if not yet started."""

    max_duration: Optional[int] = FieldInfo(alias="maxDuration", default=None)
    """Maximum allowed duration in seconds, or null if not set."""

    name: str
    """Conversation name."""

    recording_url: Optional[str] = FieldInfo(alias="recordingUrl", default=None)
    """
    A URL to download the conversation recording, or null if no recording is
    available. This URL will expire within 24-48 hours, fetch the conversation again
    to get a fresh download URL.
    """

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the conversation started, or null if not yet started."""

    status: Literal["in_progress"]

    tools: List[InProgressTool]
    """The tools that were configured for this conversation session.

    Empty if no tools were used.
    """

    transcript: List[InProgressTranscript]
    """The conversation transcript."""


class EndedAvatarRunwayPreset(BaseModel):
    """A preset avatar."""

    preset_id: str = FieldInfo(alias="presetId")
    """The preset avatar ID."""

    type: Literal["runway-preset"]


class EndedAvatarCustom(BaseModel):
    """A custom avatar created by the user."""

    id: Optional[str] = None
    """The custom avatar ID, or null if deleted."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to the avatar image, or null if unavailable."""

    name: Optional[str] = None
    """The avatar name, or null if unavailable."""

    type: Literal["custom"]


EndedAvatar: TypeAlias = Annotated[
    Union[EndedAvatarRunwayPreset, EndedAvatarCustom, None], PropertyInfo(discriminator="type")
]


class EndedTool(BaseModel):
    """Summary of a tool configured for the session."""

    description: str
    """A description of when and how the tool should be used."""

    name: str
    """The tool name."""

    type: Literal["client_event", "backend_rpc"]
    """The tool type."""


class EndedTranscriptToolCall(BaseModel):
    """A tool invocation by the assistant."""

    arguments: Dict[str, object]
    """The arguments passed to the tool."""

    name: str
    """The name of the tool that was called."""

    id: Optional[str] = None
    """Optional identifier linking this call to its result."""


class EndedTranscriptToolResult(BaseModel):
    """The result of a tool invocation."""

    name: str
    """The name of the tool that returned a result."""

    id: Optional[str] = None
    """Optional identifier linking this result to its call."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)
    """How long the tool call took in milliseconds."""

    error: Optional[str] = None
    """Error message if the tool call failed."""

    result: Union[Dict[str, object], str, None] = None
    """The tool result (object, string, or null)."""


class EndedTranscript(BaseModel):
    """A single entry in the conversation transcript."""

    content: Optional[str] = None
    """The spoken text, or null for tool-only turns."""

    role: Literal["user", "assistant"]
    """Who produced this transcript entry."""

    timestamp: Optional[datetime] = None
    """When this entry occurred, or null if unavailable."""

    tool_calls: Optional[List[EndedTranscriptToolCall]] = FieldInfo(alias="toolCalls", default=None)
    """Tool invocations made during this assistant turn.

    Only present on assistant entries.
    """

    tool_results: Optional[List[EndedTranscriptToolResult]] = FieldInfo(alias="toolResults", default=None)
    """Tool results received during this assistant turn.

    Only present on assistant entries.
    """


class Ended(BaseModel):
    """A conversation that completed successfully."""

    id: str
    """Unique conversation identifier.

    This is the same value as the realtime session ID for the call.
    """

    avatar: Optional[EndedAvatar] = None
    """The avatar used in this conversation."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the conversation was created."""

    duration: Optional[int] = None
    """Duration of the conversation in seconds."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the conversation ended."""

    max_duration: Optional[int] = FieldInfo(alias="maxDuration", default=None)
    """Maximum allowed duration in seconds, or null if not set."""

    name: str
    """Conversation name."""

    recording_url: Optional[str] = FieldInfo(alias="recordingUrl", default=None)
    """
    A URL to download the conversation recording, or null if no recording is
    available. This URL will expire within 24-48 hours, fetch the conversation again
    to get a fresh download URL.
    """

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the conversation started."""

    status: Literal["ended"]

    tools: List[EndedTool]
    """The tools that were configured for this conversation session.

    Empty if no tools were used.
    """

    transcript: List[EndedTranscript]
    """The conversation transcript."""


class FailedAvatarRunwayPreset(BaseModel):
    """A preset avatar."""

    preset_id: str = FieldInfo(alias="presetId")
    """The preset avatar ID."""

    type: Literal["runway-preset"]


class FailedAvatarCustom(BaseModel):
    """A custom avatar created by the user."""

    id: Optional[str] = None
    """The custom avatar ID, or null if deleted."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to the avatar image, or null if unavailable."""

    name: Optional[str] = None
    """The avatar name, or null if unavailable."""

    type: Literal["custom"]


FailedAvatar: TypeAlias = Annotated[
    Union[FailedAvatarRunwayPreset, FailedAvatarCustom, None], PropertyInfo(discriminator="type")
]


class FailedTool(BaseModel):
    """Summary of a tool configured for the session."""

    description: str
    """A description of when and how the tool should be used."""

    name: str
    """The tool name."""

    type: Literal["client_event", "backend_rpc"]
    """The tool type."""


class FailedTranscriptToolCall(BaseModel):
    """A tool invocation by the assistant."""

    arguments: Dict[str, object]
    """The arguments passed to the tool."""

    name: str
    """The name of the tool that was called."""

    id: Optional[str] = None
    """Optional identifier linking this call to its result."""


class FailedTranscriptToolResult(BaseModel):
    """The result of a tool invocation."""

    name: str
    """The name of the tool that returned a result."""

    id: Optional[str] = None
    """Optional identifier linking this result to its call."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)
    """How long the tool call took in milliseconds."""

    error: Optional[str] = None
    """Error message if the tool call failed."""

    result: Union[Dict[str, object], str, None] = None
    """The tool result (object, string, or null)."""


class FailedTranscript(BaseModel):
    """A single entry in the conversation transcript."""

    content: Optional[str] = None
    """The spoken text, or null for tool-only turns."""

    role: Literal["user", "assistant"]
    """Who produced this transcript entry."""

    timestamp: Optional[datetime] = None
    """When this entry occurred, or null if unavailable."""

    tool_calls: Optional[List[FailedTranscriptToolCall]] = FieldInfo(alias="toolCalls", default=None)
    """Tool invocations made during this assistant turn.

    Only present on assistant entries.
    """

    tool_results: Optional[List[FailedTranscriptToolResult]] = FieldInfo(alias="toolResults", default=None)
    """Tool results received during this assistant turn.

    Only present on assistant entries.
    """


class Failed(BaseModel):
    """A conversation that ended due to an error."""

    id: str
    """Unique conversation identifier.

    This is the same value as the realtime session ID for the call.
    """

    avatar: Optional[FailedAvatar] = None
    """The avatar used in this conversation."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the conversation was created."""

    duration: Optional[int] = None
    """Duration in seconds, or null if the conversation failed before starting."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the conversation ended, or null if it failed before starting."""

    failure: str
    """A human-friendly reason for the failure.

    We do not recommend returning this to users directly without adding context.
    """

    failure_code: str = FieldInfo(alias="failureCode")
    """A machine-readable error code for the failure.

    See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
    """

    max_duration: Optional[int] = FieldInfo(alias="maxDuration", default=None)
    """Maximum allowed duration in seconds, or null if not set."""

    name: str
    """Conversation name."""

    recording_url: Optional[str] = FieldInfo(alias="recordingUrl", default=None)
    """
    A URL to download the conversation recording, or null if no recording is
    available. This URL will expire within 24-48 hours, fetch the conversation again
    to get a fresh download URL.
    """

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the conversation started, or null if it failed before starting."""

    status: Literal["failed"]

    tools: List[FailedTool]
    """The tools that were configured for this conversation session.

    Empty if no tools were used.
    """

    transcript: List[FailedTranscript]
    """The conversation transcript."""


AvatarConversationRetrieveResponse: TypeAlias = Annotated[
    Union[InProgress, Ended, Failed], PropertyInfo(discriminator="status")
]
