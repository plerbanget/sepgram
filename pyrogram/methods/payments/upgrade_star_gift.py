import pyrogram
from pyrogram import raw


class UpgradeStarGift:
    async def upgrade_star_gift(
        self: "pyrogram.Client",
        msg_id: int,
        keep_original_details: bool = False,
    ) -> bool:
        """Upgrade a Star Gift to a unique gift.

        Parameters:
            msg_id (``int``):
                Service message ID of the gift.

            keep_original_details (``bool``, *optional*):
                Keep the original sender/message details.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.upgrade_star_gift(msg_id=123)
        """
        await self.invoke(
            raw.functions.payments.UpgradeStarGift(
                stargift=raw.types.InputSavedStarGiftUser(msg_id=msg_id),
                keep_original_details=keep_original_details or None,
            )
        )
        return True
