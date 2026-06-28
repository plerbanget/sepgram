from typing import Union, List
import pyrogram
from pyrogram import raw


class GetStoryAlbums:
    async def get_story_albums(
        self: "pyrogram.Client",
        peer: Union[int, str],
    ) -> List[dict]:
        """Get story albums for a peer.

        Parameters:
            peer (``int`` | ``str``):
                Target peer.

        Returns:
            List of ``dict``: Each dict has ``album_id`` and ``title``.

        Example:
            .. code-block:: python

                albums = await app.get_story_albums("me")
                for a in albums:
                    print(a["album_id"], a["title"])
        """
        r = await self.invoke(
            raw.functions.stories.GetAlbums(
                peer=await self.resolve_peer(peer),
                hash=0,
            )
        )
        if isinstance(r, raw.types.stories.AlbumsNotModified):
            return []
        return [{"album_id": a.album_id, "title": a.title} for a in r.albums]
