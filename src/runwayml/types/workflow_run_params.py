# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WorkflowRunParams",
    "NodeOutputsNodeOutputsItem",
    "NodeOutputsNodeOutputsItemPrimitive",
    "NodeOutputsNodeOutputsItemImage",
    "NodeOutputsNodeOutputsItemVideo",
    "NodeOutputsNodeOutputsItemAudio",
]


class WorkflowRunParams(TypedDict, total=False):
    node_outputs: Annotated[Dict[str, Dict[str, NodeOutputsNodeOutputsItem]], PropertyInfo(alias="nodeOutputs")]
    """Optional node outputs to override default values.

    Keys are node IDs from the workflow graph, values are objects mapping output
    keys to typed values.
    """


class NodeOutputsNodeOutputsItemPrimitive(TypedDict, total=False):
    """A primitive value (string, number, or boolean)"""

    type: Required[Literal["primitive"]]

    value: Required[Union[str, float, bool]]


class NodeOutputsNodeOutputsItemImage(TypedDict, total=False):
    """An image asset"""

    type: Required[Literal["image"]]

    uri: Required[str]
    """A HTTPS URL."""


class NodeOutputsNodeOutputsItemVideo(TypedDict, total=False):
    """A video asset"""

    type: Required[Literal["video"]]

    uri: Required[str]
    """A HTTPS URL."""


class NodeOutputsNodeOutputsItemAudio(TypedDict, total=False):
    """An audio asset"""

    type: Required[Literal["audio"]]

    uri: Required[str]
    """A HTTPS URL."""


NodeOutputsNodeOutputsItem: TypeAlias = Union[
    NodeOutputsNodeOutputsItemPrimitive,
    NodeOutputsNodeOutputsItemImage,
    NodeOutputsNodeOutputsItemVideo,
    NodeOutputsNodeOutputsItemAudio,
]
