from typing import Optional, List
import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object


class StarsStatus(Object):
    """Stars balance and transaction history.

    Parameters:
        balance (``int``):
            Current Stars balance (whole).

        nanos (``int``):
            Current Stars balance (fractional nanos).

        history (List of :obj:`~pyrogram.types.StarsTransaction`, *optional*):
            List of transactions.

        next_offset (``str``, *optional*):
            Offset for next page of transactions.
    """

    def __init__(self, *, client: "pyrogram.Client" = None, balance: int, nanos: int,
                 history: Optional[List["types.StarsTransaction"]] = None,
                 next_offset: Optional[str] = None):
        super().__init__(client)
        self.balance = balance
        self.nanos = nanos
        self.history = history
        self.next_offset = next_offset

    @staticmethod
    def _parse(client, r: "raw.types.payments.StarsStatus") -> "StarsStatus":
        users = {u.id: u for u in r.users}
        chats = {c.id: c for c in r.chats}

        history = None
        if getattr(r, "history", None):
            history = types.List(
                types.StarsTransaction._parse(client, t) for t in r.history
            )

        return StarsStatus(
            client=client,
            balance=r.balance.amount,
            nanos=r.balance.nanos,
            history=history,
            next_offset=getattr(r, "next_offset", None),
        )
