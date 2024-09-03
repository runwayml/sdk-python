# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskRetrieveResponse"]


class TaskRetrieveResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp that the task was submitted at."""

    status: Literal["RUNNING", "SUCCEEDED", "FAILED", "PENDING", "CANCELLED", "THROTTLED"]
    """
    - `PENDING` tasks have been enqueued and are waiting to run.
    - `THROTTLED` tasks are waiting to be enqueued until other jobs have finished
      running.
    - `RUNNING` tasks are currently being processed.
    - `SUCCEEDED` tasks have completed successfully.
    - `FAILED` tasks have failed.
    - `CANCELLED` tasks have been aborted.
    """

    failure: Optional[str] = None
    """
    If the status is `FAILED`, this will contain a human-friendly reason for the
    failure.
    """

    failure_code: Optional[str] = FieldInfo(alias="failureCode", default=None)
    """
    If the task has a status of `FAILED`, this contains a machine-readable error
    code. This is a dot-separated string, with the leftmost segment being the most
    generic and the rightmost segment being the most specific. For example,
    `SAFETY.INPUT.TEXT` would indicate that the task failed due to a content
    moderation error on the input text.
    """

    output: Optional[List[str]] = None
    """If the status is `SUCCEEDED`, this will contain an array of strings.

    Each string will be a URL that returns an output from the task. URLs expire
    within 24-48 hours; fetch the task again to get fresh URLs. It is expected that
    you download the assets at these URLs and store them in your own storage system.
    """

    progress: Optional[float] = None
    """
    If the task has a status of `RUNNING`, this will contain a floating point number
    between 0 and 1 representing the progress of the generation.
    """
