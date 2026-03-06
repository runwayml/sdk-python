# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    content: Required[str]
    """The markdown or plain text content of the document."""

    name: Required[str]
    """A descriptive name for the document."""
