import pyrogram
from pyrogram import raw


class ConvertStarGift:
    async def convert_star_gift(
        self: "pyrogram.Client",
        msg_id: int,
    ) -> bool:
        """Convert a received Star Gift to Stars.

        Parameters:
            msg_id (``int``):
                Service message ID of the gift.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.convert_star_gift(msg_id=123)
        """
        await self.invoke(
            raw.functions.payments.ConvertStarGift(
                stargift=raw.types.InputSavedStarGiftUser(msg_id=msg_id)
            )
        )
        return True
