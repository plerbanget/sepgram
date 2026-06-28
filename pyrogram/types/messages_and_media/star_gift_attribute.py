from typing import Optional
import pyrogram
from pyrogram import raw
from ..object import Object


class StarGiftAttribute(Object):
    """An attribute of a unique Star Gift.

    Parameters:
        type (``str``):
            Attribute type: "model", "pattern", "backdrop", or "original_details".

        name (``str``, *optional*):
            Attribute name.

        rarity_permille (``int``, *optional*):
            Rarity in permille (out of 1000).

        backdrop_id (``int``, *optional*):
            Backdrop ID (backdrop type only).

        center_color (``int``, *optional*):
            Center color hex (backdrop type only).

        edge_color (``int``, *optional*):
            Edge color hex (backdrop type only).

        pattern_color (``int``, *optional*):
            Pattern color hex (backdrop type only).

        text_color (``int``, *optional*):
            Text color hex (backdrop type only).
    """

    def __init__(self, *, client: "pyrogram.Client" = None, type: str,
                 name: Optional[str] = None, rarity_permille: Optional[int] = None,
                 backdrop_id: Optional[int] = None, center_color: Optional[int] = None,
                 edge_color: Optional[int] = None, pattern_color: Optional[int] = None,
                 text_color: Optional[int] = None):
        super().__init__(client)
        self.type = type
        self.name = name
        self.rarity_permille = rarity_permille
        self.backdrop_id = backdrop_id
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color

    @staticmethod
    def _parse(client, attr) -> "StarGiftAttribute":
        if isinstance(attr, raw.types.StarGiftAttributeModel):
            return StarGiftAttribute(client=client, type="model", name=attr.name,
                                     rarity_permille=attr.rarity.permille)
        if isinstance(attr, raw.types.StarGiftAttributePattern):
            return StarGiftAttribute(client=client, type="pattern", name=attr.name,
                                     rarity_permille=attr.rarity.permille)
        if isinstance(attr, raw.types.StarGiftAttributeBackdrop):
            return StarGiftAttribute(client=client, type="backdrop", name=attr.name,
                                     backdrop_id=attr.backdrop_id, center_color=attr.center_color,
                                     edge_color=attr.edge_color, pattern_color=attr.pattern_color,
                                     text_color=attr.text_color, rarity_permille=attr.rarity.permille)
        if isinstance(attr, raw.types.StarGiftAttributeOriginalDetails):
            return StarGiftAttribute(client=client, type="original_details")
        return StarGiftAttribute(client=client, type="unknown")
