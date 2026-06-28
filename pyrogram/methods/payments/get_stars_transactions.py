from typing import Union, Optional
import pyrogram
from pyrogram import raw, types


class GetStarsTransactions:
    async def get_stars_transactions(
        self: "pyrogram.Client",
        peer: Union[int, str] = "me",
        offset: str = "",
        limit: int = 20,
        inbound: bool = None,
        outbound: bool = None,
        ascending: bool = None,
    ) -> "types.StarsStatus":
        """Get Stars transaction history.

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Target peer. Defaults to self.

            offset (``str``, *optional*):
                Pagination offset.

            limit (``int``, *optional*):
                Max number of transactions to return.

            inbound (``bool``, *optional*):
                Only inbound transactions.

            outbound (``bool``, *optional*):
                Only outbound transactions.

            ascending (``bool``, *optional*):
                Sort ascending.

        Returns:
            :obj:`~pyrogram.types.StarsStatus`: On success.

        Example:
            .. code-block:: python

                result = await app.get_stars_transactions(limit=10)
                for tx in result.history:
                    print(tx.id, tx.amount)
        """
        r = await self.invoke(
            raw.functions.payments.GetStarsTransactions(
                peer=await self.resolve_peer(peer),
                offset=offset,
                limit=limit,
                inbound=inbound or None,
                outbound=outbound or None,
                ascending=ascending or None,
            )
        )
        return types.StarsStatus._parse(self, r)
