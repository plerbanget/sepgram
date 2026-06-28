from ..object import Object


class SentGuestMessage(Object):
    """A sent guest message result.

    Parameters:
        inline_message_id (``str``):
            Identifier of the sent inline message.
    """

    def __init__(self, *, client=None, inline_message_id: str):
        super().__init__(client)
        self.inline_message_id = inline_message_id
