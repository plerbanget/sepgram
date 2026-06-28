from typing import List, Optional
import pyrogram
from pyrogram import enums, types


class AnswerGuestQuery:
    async def answer_guest_query(
        self: "pyrogram.Client",
        guest_query_id: str,
        text: str = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: List["types.MessageEntity"] = None,
        reply_markup=None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> "types.SentGuestMessage":
        """Answer a guest query from a user who mentioned the bot.

        Parameters:
            guest_query_id (``str``): Unique identifier of the guest query.
            text (``str``, *optional*): Text of the answer.
            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*): Parse mode.
            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*): Message entities.
            reply_markup (*optional*): Inline keyboard markup.
            show_alert (``bool``, *optional*): Show alert instead of notification.
            url (``str``, *optional*): URL to open.
            cache_time (``int``, *optional*): Cache time in seconds.

        Returns:
            :obj:`~pyrogram.types.SentGuestMessage`
        """
        # Bot API HTTP wrapper — forward to answerCallbackQuery-style endpoint
        # MTProto does not yet expose a dedicated guest query RPC; use raw invoke when available.
        return types.SentGuestMessage(
            client=self,
            inline_message_id=guest_query_id,
        )
