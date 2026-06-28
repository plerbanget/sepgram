from typing import Union
import pyrogram
from pyrogram import raw


class DeleteStoryAlbum:
    async def delete_story_album(
        self: "pyrogram.Client",
        peer: Union[int, str],
        album_id: int,
    ) -> bool:
        """Delete a story album.

        Parameters:
            peer (``int`` | ``str``):
                The peer that owns the album.

            album_id (``int``):
                Album ID to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_story_album("me", album_id=1)
        """
        await self.invoke(
            raw.functions.stories.DeleteAlbum(
                peer=await self.resolve_peer(peer),
                album_id=album_id,
            )
        )
        return True
