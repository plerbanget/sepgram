from typing import Union
import pyrogram
from pyrogram import raw


class GetStarsBalance:
    async def get_stars_balance(
        self: "pyrogram.Client",
        peer: Union[int, str] = "me",
    ) -> int:
        """Get Stars balance for a peer.

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Target peer. Defaults to self.

        Returns:
            ``int``: Stars balance.

        Example:
            .. code-block:: python

                balance = await app.get_stars_balance()
                print(f"Balance: {balance} stars")
        """
        r = await self.invoke(
            raw.functions.payments.GetStarsStatus(peer=await self.resolve_peer(peer))
        )
        return r.balance.amount
