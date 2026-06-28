from datetime import datetime
from typing import Optional
import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object


class SavedStarGift(Object):
    """A saved Star Gift in a user's or chat's profile.

    Parameters:
        gift (:obj:`~pyrogram.types.StarGift`):
            The gift object.

        date (:py:obj:`~datetime.datetime`):
            Date the gift was received.

        from_id (``int``, *optional*):
            Sender user/chat ID.

        message (``str``, *optional*):
            Gift message text.

        msg_id (``int``, *optional*):
            Service message ID.

        saved_id (``int``, *optional*):
            Saved gift ID (for chat gifts).

        name_hidden (``bool``, *optional*):
            True if sender name is hidden.

        unsaved (``bool``, *optional*):
            True if the gift is not shown on profile.

        can_upgrade (``bool``, *optional*):
            True if the gift can be upgraded to unique.

        convert_stars (``int``, *optional*):
            Stars to receive if converted.

        upgrade_stars (``int``, *optional*):
            Stars needed to upgrade.

        transfer_stars (``int``, *optional*):
            Stars needed to transfer.
    """

    def __init__(self, *, client: "pyrogram.Client" = None,
                 gift: "types.StarGift", date: datetime,
                 from_id: Optional[int] = None, message: Optional[str] = None,
                 msg_id: Optional[int] = None, saved_id: Optional[int] = None,
                 name_hidden: bool = None, unsaved: bool = None, can_upgrade: bool = None,
                 convert_stars: Optional[int] = None, upgrade_stars: Optional[int] = None,
                 transfer_stars: Optional[int] = None):
        super().__init__(client)
        self.gift = gift
        self.date = date
        self.from_id = from_id
        self.message = message
        self.msg_id = msg_id
        self.saved_id = saved_id
        self.name_hidden = name_hidden
        self.unsaved = unsaved
        self.can_upgrade = can_upgrade
        self.convert_stars = convert_stars
        self.upgrade_stars = upgrade_stars
        self.transfer_stars = transfer_stars

    @staticmethod
    def _parse(client, saved: "raw.types.SavedStarGift", users: dict, chats: dict) -> "SavedStarGift":
        from_id = None
        if getattr(saved, "from_id", None):
            from_id = utils.get_raw_peer_id(saved.from_id)

        message = None
        if getattr(saved, "message", None):
            message = getattr(saved.message, "text", None)

        return SavedStarGift(
            client=client,
            gift=types.StarGift._parse(client, saved.gift),
            date=utils.timestamp_to_datetime(saved.date),
            from_id=from_id,
            message=message,
            msg_id=getattr(saved, "msg_id", None),
            saved_id=getattr(saved, "saved_id", None),
            name_hidden=getattr(saved, "name_hidden", None),
            unsaved=getattr(saved, "unsaved", None),
            can_upgrade=getattr(saved, "can_upgrade", None),
            convert_stars=getattr(saved, "convert_stars", None),
            upgrade_stars=getattr(saved, "upgrade_stars", None),
            transfer_stars=getattr(saved, "transfer_stars", None),
        )
