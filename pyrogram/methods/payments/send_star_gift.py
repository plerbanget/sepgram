from typing import Union, Optional
import pyrogram
from pyrogram import raw


class SendStarGift:
    async def send_star_gift(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        gift_id: int,
        message: Optional[str] = None,
        hide_name: bool = False,
        include_upgrade: bool = False,
    ) -> bool:
        """Send a Star Gift to a user.

        Parameters:
            user_id (``int`` | ``str``):
                Target user.

            gift_id (``int``):
                Gift ID from :meth:`~pyrogram.Client.get_star_gifts`.

            message (``str``, *optional*):
                Optional message to include with the gift.

            hide_name (``bool``, *optional*):
                Hide your name from the recipient.

            include_upgrade (``bool``, *optional*):
                Include upgrade option.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.send_star_gift(user_id="username", gift_id=123)
        """
        peer = await self.resolve_peer(user_id)

        invoice = raw.types.InputInvoiceStarGift(
            peer=peer,
            gift_id=gift_id,
            hide_name=hide_name or None,
            include_upgrade=include_upgrade or None,
            message=raw.types.TextWithEntities(text=message, entities=[]) if message else None,
        )

        form = await self.invoke(raw.functions.payments.GetPaymentForm(invoice=invoice))
        await self.invoke(raw.functions.payments.SendStarsForm(form_id=form.form_id, invoice=invoice))
        return True
