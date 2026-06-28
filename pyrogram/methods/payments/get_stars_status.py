from typing import Union
import pyrogram
from pyrogram import raw, types


class GetStarsStatus:
    async def get_stars_status(
        self: "pyrogram.Client",
        peer: Union[int, str] = "me",
    ) -> "types.StarsStatus":
        """Get Stars balance and status for a peer.

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Target peer. Defaults to self.

        Returns:
            :obj:`~pyrogram.types.StarsStatus`: On success.

        Example:
            .. code-block:: python

                status = await app.get_stars_status()
                print(status.balance)
        """
        r = await self.invoke(
            raw.functions.payments.GetStarsStatus(peer=await self.resolve_peer(peer))
        )
        return types.StarsStatus._parse(self, r)
