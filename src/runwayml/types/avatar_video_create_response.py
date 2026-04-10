# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AvatarVideoCreateResponse"]


class AvatarVideoCreateResponse(BaseModel):
    id: str
    """The ID of the avatar video task.

    Use `GET /v1/tasks/:id` to poll for status and output.
    """
