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
        Literal[
            "hdr10",
            "hlg",
            "hdr_prores",
            "hdr_exr_sequence",
            "hdr_exr_acescg_sequence_1_3",
            "hdr_exr_acescg_sequence_2_0",
        ],
        PropertyInfo(alias="outputFormat"),
    ]
    """The HDR delivery profile of the output.

    `hdr10` (default) returns an HEVC Main 10, BT.2020 + PQ .mp4; `hlg` returns an
    HEVC Main 10, BT.2020 + HLG .mp4; `hdr_prores` returns a BT.2020 + PQ ProRes
    .mov editorial mezzanine, whose tier is selectable with `proresProfile`;
    `hdr_exr_sequence` returns a .zip of half-float OpenEXR frames holding the HDR
    signal as linear BT.2020 display light, 1.0 = 100 nits, ready to composite;
    `hdr_exr_acescg_sequence_1_3` returns a scene-referred ACEScg sequence with VFX
    frame naming (frame.0001.exr): the source plate brought into ACES through the
    inverse ACES 1.3 SDR (Rec.709) Output Transform, with the highlight detail Ruby
    recovers added on top — read it with the stock `ACES - ACEScg` input transform;
    the ACES SDR view reproduces your source, and the ACES HDR views render the same
    scene with the recovered highlights (this is a scene, not the `hdr10` display
    grade, so an ACES HDR view is not expected to match `hdr10`). An EXR zip is the
    whole delivery — the frames, a colorimetry.json sidecar, a provenance.json
    sidecar declaring the upconvert, and the source audio as audio.wav when the
    source has any. A source with an alpha channel (ProRes 4444, WebM with alpha,
    RGBA codecs) keeps it where the container can carry one: the EXR profiles write
    it as the A channel and `hdr_prores` delivers a 4444 with an alpha plane; the
    alpha is passed through as received (not premultiplied). `hdr10` and `hlg`
    cannot carry alpha and deliver the picture without it. All five profiles bill at
    the same rate: 20 credits per second of output, rising to 40 credits per second
    when the source is larger than 4 megapixels — that includes anything larger than
    1440p, up through 4K.
    """

    prores_profile: Annotated[Literal["422", "4444", "422 HQ"], PropertyInfo(alias="proresProfile")]
    """The ProRes tier of the `hdr_prores` mezzanine.

    Only valid when `outputFormat` is `hdr_prores`. Defaults to `422 HQ`. A source
    with an alpha channel is always delivered as `4444`, the only tier with an alpha
    plane, whatever tier is requested.
    """
