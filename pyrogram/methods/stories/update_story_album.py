from typing import Union, List, Optional
import pyrogram
from pyrogram import raw


class UpdateStoryAlbum:
    async def update_story_album(
        self: "pyrogram.Client",
        peer: Union[int, str],
        album_id: int,
        title: Optional[str] = None,
        add_stories: Optional[List[int]] = None,
        delete_stories: Optional[List[int]] = None,
        order: Optional[List[int]] = None,
    ) -> dict:
        """Update a story album.

        Parameters:
            peer (``int`` | ``str``):
                The peer that owns the album.

            album_id (``int``):
                Album ID to update.

            title (``str``, *optional*):
                New title.

            add_stories (List of ``int``, *optional*):
                Story IDs to add.

            delete_stories (List of ``int``, *optional*):
                Story IDs to remove.

            order (List of ``int``, *optional*):
                New story order.

        Returns:
            ``dict``: Updated album info.

        Example:
            .. code-block:: python

                await app.update_story_album("me", album_id=1, title="New Title")
        """
        r = await self.invoke(
            raw.functions.stories.UpdateAlbum(
                peer=await self.resolve_peer(peer),
                album_id=album_id,
                title=title,
                add_stories=add_stories,
                delete_stories=delete_stories,
                order=order,
            )
        )
        return {"album_id": r.album_id, "title": r.title}
