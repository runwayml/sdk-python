# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoToHdrCreateParams"]


class VideoToHdrCreateParams(TypedDict, total=False):
    model: Required[Literal["ruby"]]

    video_uri: Required[Annotated[str, PropertyInfo(alias="videoUri")]]
    """A HTTPS URL, Runway upload URI, or base64 data URI (e.g.

    `data:video/mp4;base64,...`, up to 5MB) containing an encoded video. See
    [our docs](/assets/inputs#videos) on video inputs for more information.
    """

    output_format: Annotated[
        Literal["hdr10", "hlg", "hdr_prores", "hdr_exr_sequence"], PropertyInfo(alias="outputFormat")
    ]
    """The HDR delivery profile of the output.

    `hdr10` (default) returns an HEVC Main 10, BT.2020 + PQ .mp4; `hlg` returns an
    HEVC Main 10, BT.2020 + HLG .mp4; `hdr_prores` returns a BT.2020 + PQ ProRes
    .mov editorial mezzanine, whose tier is selectable with `proresProfile`;
    `hdr_exr_sequence` returns a .zip of half-float OpenEXR frames holding the HDR
    signal as linear BT.2020 display light, 1.0 = 100 nits, ready to composite. The
    EXR zip is the whole delivery — the frames, a colorimetry.json sidecar, a
    provenance.json sidecar declaring the upconvert, and the source audio as
    audio.wav when the source has any. All four profiles bill at the same rate: 20
    credits per second of output, rising to 40 credits per second when the source is
    larger than 4 megapixels (roughly 4K).
    """

    prores_profile: Annotated[Literal["422", "4444", "422 HQ"], PropertyInfo(alias="proresProfile")]
    """The ProRes tier of the `hdr_prores` mezzanine.

    Only valid when `outputFormat` is `hdr_prores`. Defaults to `422 HQ`.
    """
