from typing import Union, List
import pyrogram
from pyrogram import raw


class CreateStoryAlbum:
    async def create_story_album(
        self: "pyrogram.Client",
        peer: Union[int, str],
        title: str,
        stories: List[int],
    ) -> dict:
        """Create a story album.

        Parameters:
            peer (``int`` | ``str``):
                The peer (channel/user) to create the album for.

            title (``str``):
                Album title.

            stories (List of ``int``):
                List of story IDs to include.

        Returns:
            ``dict``: Album info with ``album_id`` and ``title``.

        Example:
            .. code-block:: python

                album = await app.create_story_album("me", "My Album", [1, 2, 3])
        """
        r = await self.invoke(
            raw.functions.stories.CreateAlbum(
                peer=await self.resolve_peer(peer),
                title=title,
                stories=stories,
            )
        )
        return {"album_id": r.album_id, "title": r.title}
