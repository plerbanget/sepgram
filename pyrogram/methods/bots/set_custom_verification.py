from typing import Union, Optional
import pyrogram
from pyrogram import raw


class SetCustomVerification:
    async def set_custom_verification(
        self: "pyrogram.Client",
        peer: Union[int, str],
        enabled: bool = True,
        bot: Optional[Union[int, str]] = None,
        custom_description: Optional[str] = None,
    ) -> bool:
        """Set custom verification for a peer via a bot.

        Parameters:
            peer (``int`` | ``str``):
                Target peer to verify.

            enabled (``bool``, *optional*):
                Enable or disable verification. Defaults to True.

            bot (``int`` | ``str``, *optional*):
                Bot to use for verification.

            custom_description (``str``, *optional*):
                Custom verification description.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_custom_verification("@channel", bot="@verifybot")
        """
        bot_peer = await self.resolve_peer(bot) if bot else None
        await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(peer),
                enabled=enabled or None,
                bot=bot_peer,
                custom_description=custom_description,
            )
        )
        return True
