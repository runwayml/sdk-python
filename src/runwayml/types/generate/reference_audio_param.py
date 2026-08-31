# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReferenceAudioParam"]


class ReferenceAudioParam(TypedDict, total=False):
    uri: Required[str]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:audio/mp3;base64,...`, up to 5MB) containing an encoded audio. See
    [our docs](/assets/inputs#audio) on audio inputs for more information.
    """
