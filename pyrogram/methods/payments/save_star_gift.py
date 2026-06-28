import pyrogram
from pyrogram import raw


class SaveStarGift:
    async def save_star_gift(
        self: "pyrogram.Client",
        msg_id: int,
        unsave: bool = False,
    ) -> bool:
        """Save or unsave a received Star Gift to your profile.

        Parameters:
            msg_id (``int``):
                Service message ID of the gift.

            unsave (``bool``, *optional*):
                Pass True to hide the gift from profile.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.save_star_gift(msg_id=123)
                await app.save_star_gift(msg_id=123, unsave=True)
        """
        await self.invoke(
            raw.functions.payments.SaveStarGift(
                stargift=raw.types.InputSavedStarGiftUser(msg_id=msg_id),
                unsave=unsave or None,
            )
        )
        return True
