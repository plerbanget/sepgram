from datetime import datetime
from typing import Optional
import pyrogram
from pyrogram import raw, utils
from ..object import Object


class StarsTransaction(Object):
    """A Telegram Stars transaction.

    Parameters:
        id (``str``):
            Transaction ID.

        amount (``int``):
            Stars amount (whole).

        nanos (``int``):
            Stars amount (fractional nanos).

        date (:py:obj:`~datetime.datetime`):
            Transaction date.

        refund (``bool``, *optional*):
            True if this is a refund.

        pending (``bool``, *optional*):
            True if transaction is pending.

        failed (``bool``, *optional*):
            True if transaction failed.

        gift (``bool``, *optional*):
            True if this is a gift transaction.

        title (``str``, *optional*):
            Transaction title.

        description (``str``, *optional*):
            Transaction description.

        transaction_url (``str``, *optional*):
            URL for transaction details.

        peer_type (``str``, *optional*):
            Peer type string (e.g. "user", "fragment", "ads", etc.).
    """

    def __init__(self, *, client: "pyrogram.Client" = None, id: str, amount: int, nanos: int,
                 date: datetime, refund: bool = None, pending: bool = None, failed: bool = None,
                 gift: bool = None, title: Optional[str] = None, description: Optional[str] = None,
                 transaction_url: Optional[str] = None, peer_type: Optional[str] = None):
        super().__init__(client)
        self.id = id
        self.amount = amount
        self.nanos = nanos
        self.date = date
        self.refund = refund
        self.pending = pending
        self.failed = failed
        self.gift = gift
        self.title = title
        self.description = description
        self.transaction_url = transaction_url
        self.peer_type = peer_type

    @staticmethod
    def _parse(client, t: "raw.types.StarsTransaction") -> "StarsTransaction":
        peer_type_map = {
            raw.types.StarsTransactionPeer: "user",
            raw.types.StarsTransactionPeerFragment: "fragment",
            raw.types.StarsTransactionPeerAds: "ads",
            raw.types.StarsTransactionPeerAppStore: "appstore",
            raw.types.StarsTransactionPeerPlayMarket: "playmarket",
            raw.types.StarsTransactionPeerPremiumBot: "premium_bot",
            raw.types.StarsTransactionPeerApi: "api",
            raw.types.StarsTransactionPeerUnsupported: "unsupported",
        }
        peer_type = peer_type_map.get(type(t.peer), "unknown")

        return StarsTransaction(
            client=client,
            id=t.id,
            amount=t.amount.amount,
            nanos=t.amount.nanos,
            date=utils.timestamp_to_datetime(t.date),
            refund=getattr(t, "refund", None),
            pending=getattr(t, "pending", None),
            failed=getattr(t, "failed", None),
            gift=getattr(t, "gift", None),
            title=getattr(t, "title", None),
            description=getattr(t, "description", None),
            transaction_url=getattr(t, "transaction_url", None),
            peer_type=peer_type,
        )
