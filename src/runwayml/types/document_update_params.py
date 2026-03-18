# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    content: str
    """New markdown or plain text content for the document."""

    name: str
    """A new name for the document."""
