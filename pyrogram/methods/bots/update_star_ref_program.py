from typing import Union, Optional
import pyrogram
from pyrogram import raw


class UpdateStarRefProgram:
    async def update_star_ref_program(
        self: "pyrogram.Client",
        bot: Union[int, str],
        commission_permille: int,
        duration_months: Optional[int] = None,
    ) -> bool:
        """Update the Star referral program for a bot.

        Parameters:
            bot (``int`` | ``str``):
                Target bot.

            commission_permille (``int``):
                Commission in permille (e.g. 100 = 10%).

            duration_months (``int``, *optional*):
                Program duration in months.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.update_star_ref_program("@mybot", commission_permille=100)
        """
        await self.invoke(
            raw.functions.bots.UpdateStarRefProgram(
                bot=await self.resolve_peer(bot),
                commission_permille=commission_permille,
                duration_months=duration_months,
            )
        )
        return True
