from ..object import Object


class PaidMediaLivePhoto(Object):
    """A paid media live photo.

    Parameters:
        live_photo (:obj:`~pyrogram.types.LivePhoto`): The live photo.
    """

    def __init__(self, *, client=None, live_photo):
        super().__init__(client)
        self.live_photo = live_photo
