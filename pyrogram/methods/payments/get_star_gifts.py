from typing import List
import pyrogram
from pyrogram import raw, types


class GetStarGifts:
    async def get_star_gifts(self: "pyrogram.Client") -> List["types.StarGift"]:
        """Get the list of available Star Gifts.

        Returns:
            List of :obj:`~pyrogram.types.StarGift`: On success.

        Example:
            .. code-block:: python

                gifts = await app.get_star_gifts()
        """
        r = await self.invoke(raw.functions.payments.GetStarGifts(hash=0))

        if isinstance(r, raw.types.payments.StarGiftsNotModified):
            return types.List()

        return types.List(types.StarGift._parse(self, g) for g in r.gifts)
