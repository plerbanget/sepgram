from typing import Union, List
import pyrogram
from pyrogram import raw, types


class GetBotRecommendations:
    async def get_bot_recommendations(
        self: "pyrogram.Client",
        bot: Union[int, str],
    ) -> List["types.User"]:
        """Get recommended bots similar to the given bot.

        Parameters:
            bot (``int`` | ``str``):
                Target bot username or ID.

        Returns:
            List of :obj:`~pyrogram.types.User`: On success.

        Example:
            .. code-block:: python

                bots = await app.get_bot_recommendations("@mybot")
        """
        r = await self.invoke(
            raw.functions.bots.GetBotRecommendations(bot=await self.resolve_peer(bot))
        )
        users = {u.id: u for u in r.users}
        return types.List(
            types.User._parse(self, users[u.id]) for u in r.users
        )
