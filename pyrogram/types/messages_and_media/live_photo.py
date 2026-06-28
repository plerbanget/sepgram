from typing import Optional
from ..object import Object


class LivePhoto(Object):
    """A live photo (photo with short video loop).

    Parameters:
        file_id (``str``): File identifier.
        file_unique_id (``str``): Unique file identifier.
        width (``int``): Photo width.
        height (``int``): Photo height.
        duration (``int``): Video duration in seconds.
        file_size (``int``, *optional*): File size in bytes.
        thumbnail (*optional*): Photo thumbnail.
    """

    def __init__(self, *, client=None, file_id: str, file_unique_id: str,
                 width: int, height: int, duration: int,
                 file_size: int = None, thumbnail=None):
        super().__init__(client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.file_size = file_size
        self.thumbnail = thumbnail
