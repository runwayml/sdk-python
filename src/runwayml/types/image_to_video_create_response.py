# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ImageToVideoCreateResponse"]


class ImageToVideoCreateResponse(BaseModel):
    id: str
    """The ID of the newly created task.

    Use this ID to query the task status and retrieve the generated video.
    """
