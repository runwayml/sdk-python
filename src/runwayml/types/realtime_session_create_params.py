# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "RealtimeSessionCreateParams",
    "Avatar",
    "AvatarRunwayPreset",
    "AvatarCustom",
    "Tool",
    "ToolClientEvent",
    "ToolClientEventParameter",
    "ToolClientEventParameterString",
    "ToolClientEventParameterInteger",
    "ToolClientEventParameterNumber",
    "ToolClientEventParameterBoolean",
    "ToolClientEventParameterArray",
    "ToolClientEventParameterArrayItems",
    "ToolClientEventParameterObject",
    "ToolBackendRpc",
    "ToolBackendRpcParameter",
    "ToolBackendRpcParameterString",
    "ToolBackendRpcParameterInteger",
    "ToolBackendRpcParameterNumber",
    "ToolBackendRpcParameterBoolean",
    "ToolBackendRpcParameterArray",
    "ToolBackendRpcParameterArrayItems",
    "ToolBackendRpcParameterObject",
]


class RealtimeSessionCreateParams(TypedDict, total=False):
    avatar: Required[Avatar]
    """The avatar configuration for the session."""

    model: Required[Literal["gwm1_avatars"]]
    """The realtime session model type."""

    max_duration: Annotated[int, PropertyInfo(alias="maxDuration")]
    """Maximum session duration in seconds."""

    personality: str
    """Override the avatar personality for this session.

    If not provided, uses the avatar default.
    """

    start_script: Annotated[str, PropertyInfo(alias="startScript")]
    """Override the avatar start script for this session.

    If not provided, uses the avatar default.
    """

    tools: Iterable[Tool]
    """Tools available to the avatar during the session."""


class AvatarRunwayPreset(TypedDict, total=False):
    """A preset avatar from Runway."""

    preset_id: Required[
        Annotated[
            Literal[
                "game-character",
                "music-superstar",
                "game-character-man",
                "cat-character",
                "influencer",
                "tennis-coach",
                "human-resource",
                "fashion-designer",
                "cooking-teacher",
            ],
            PropertyInfo(alias="presetId"),
        ]
    ]
    """ID of a preset avatar."""

    type: Required[Literal["runway-preset"]]


class AvatarCustom(TypedDict, total=False):
    """A user-created avatar."""

    avatar_id: Required[Annotated[str, PropertyInfo(alias="avatarId")]]
    """ID of a user-created avatar."""

    type: Required[Literal["custom"]]


Avatar: TypeAlias = Union[AvatarRunwayPreset, AvatarCustom]


class ToolClientEventParameterString(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["string"]]

    enum: SequenceNotStr[str]
    """Allowed values for the parameter."""

    required: bool
    """Whether the parameter is required."""


class ToolClientEventParameterInteger(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["integer"]]

    required: bool
    """Whether the parameter is required."""


class ToolClientEventParameterNumber(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["number"]]

    required: bool
    """Whether the parameter is required."""


class ToolClientEventParameterBoolean(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["boolean"]]

    required: bool
    """Whether the parameter is required."""


class ToolClientEventParameterArrayItems(TypedDict, total=False):
    """Item schema for array elements."""

    type: Required[Literal["string", "integer", "number", "boolean"]]
    """The type of each element in the array."""


class ToolClientEventParameterArray(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    items: Required[ToolClientEventParameterArrayItems]
    """Item schema for array elements."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["array"]]

    required: bool
    """Whether the parameter is required."""


class ToolClientEventParameterObject(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    properties: Required[Iterable[object]]
    """The properties of the object."""

    type: Required[Literal["object"]]

    required: bool
    """Whether the parameter is required."""


ToolClientEventParameter: TypeAlias = Union[
    ToolClientEventParameterString,
    ToolClientEventParameterInteger,
    ToolClientEventParameterNumber,
    ToolClientEventParameterBoolean,
    ToolClientEventParameterArray,
    ToolClientEventParameterObject,
]


class ToolClientEvent(TypedDict, total=False):
    """
    A fire-and-forget tool that sends arguments to the frontend client of the realtime session.
    """

    description: Required[str]
    """A description of when and how the tool should be used.

    Be specific so the avatar understands the right context to invoke it.
    """

    name: Required[str]
    """The tool name.

    Must start with a letter or underscore, followed by alphanumeric characters or
    underscores.
    """

    type: Required[Literal["client_event"]]

    parameters: Iterable[ToolClientEventParameter]


class ToolBackendRpcParameterString(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["string"]]

    enum: SequenceNotStr[str]
    """Allowed values for the parameter."""

    required: bool
    """Whether the parameter is required."""


class ToolBackendRpcParameterInteger(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["integer"]]

    required: bool
    """Whether the parameter is required."""


class ToolBackendRpcParameterNumber(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["number"]]

    required: bool
    """Whether the parameter is required."""


class ToolBackendRpcParameterBoolean(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["boolean"]]

    required: bool
    """Whether the parameter is required."""


class ToolBackendRpcParameterArrayItems(TypedDict, total=False):
    """Item schema for array elements."""

    type: Required[Literal["string", "integer", "number", "boolean"]]
    """The type of each element in the array."""


class ToolBackendRpcParameterArray(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    items: Required[ToolBackendRpcParameterArrayItems]
    """Item schema for array elements."""

    name: Required[str]
    """The parameter name."""

    type: Required[Literal["array"]]

    required: bool
    """Whether the parameter is required."""


class ToolBackendRpcParameterObject(TypedDict, total=False):
    description: Required[str]
    """A description of the parameter."""

    name: Required[str]
    """The parameter name."""

    properties: Required[Iterable[object]]
    """The properties of the object."""

    type: Required[Literal["object"]]

    required: bool
    """Whether the parameter is required."""


ToolBackendRpcParameter: TypeAlias = Union[
    ToolBackendRpcParameterString,
    ToolBackendRpcParameterInteger,
    ToolBackendRpcParameterNumber,
    ToolBackendRpcParameterBoolean,
    ToolBackendRpcParameterArray,
    ToolBackendRpcParameterObject,
]


class ToolBackendRpc(TypedDict, total=False):
    """
    A tool that makes a round-trip RPC call to your backend server during the session.
    """

    description: Required[str]
    """A description of when and how the tool should be used.

    Be specific so the avatar understands the right context to invoke it.
    """

    name: Required[str]
    """The tool name.

    Must start with a letter or underscore, followed by alphanumeric characters or
    underscores.
    """

    type: Required[Literal["backend_rpc"]]

    parameters: Iterable[ToolBackendRpcParameter]

    timeout_seconds: Annotated[float, PropertyInfo(alias="timeoutSeconds")]
    """Maximum time to wait for the backend to respond."""


Tool: TypeAlias = Union[ToolClientEvent, ToolBackendRpc]
