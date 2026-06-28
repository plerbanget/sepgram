from datetime import datetime
from typing import Optional, List
import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object


class StarGift(Object):
    """A Telegram Star Gift.

    Parameters:
        id (``int``):
            Gift unique ID.

        stars (``int``):
            Price in stars.

        convert_stars (``int``):
            Stars received if converted.

        limited (``bool``, *optional*):
            True if the gift is limited edition.

        sold_out (``bool``, *optional*):
            True if the gift is sold out.

        birthday (``bool``, *optional*):
            True if this is a birthday gift.

        require_premium (``bool``, *optional*):
            True if recipient must have Telegram Premium.

        availability_remains (``int``, *optional*):
            Remaining availability count.

        availability_total (``int``, *optional*):
            Total availability count.

        upgrade_stars (``int``, *optional*):
            Stars needed to upgrade to unique gift.

        first_sale_date (:py:obj:`~datetime.datetime`, *optional*):
            Date of first sale.

        last_sale_date (:py:obj:`~datetime.datetime`, *optional*):
            Date of last sale.

        title (``str``, *optional*):
            Title (for unique gifts).

        is_unique (``bool``):
            True if this is a unique (NFT-style) gift.

        slug (``str``, *optional*):
            Unique gift slug.

        num (``int``, *optional*):
            Unique gift number.

        attributes (List of :obj:`~pyrogram.types.StarGiftAttribute`, *optional*):
            Attributes of unique gift.
    """

    def __init__(self, *, client: "pyrogram.Client" = None, id: int, stars: int = 0,
                 convert_stars: int = 0, limited: bool = None, sold_out: bool = None,
                 birthday: bool = None, require_premium: bool = None,
                 availability_remains: Optional[int] = None, availability_total: Optional[int] = None,
                 upgrade_stars: Optional[int] = None, first_sale_date: Optional[datetime] = None,
                 last_sale_date: Optional[datetime] = None, title: Optional[str] = None,
                 is_unique: bool = False, slug: Optional[str] = None, num: Optional[int] = None,
                 attributes: Optional[List["types.StarGiftAttribute"]] = None):
        super().__init__(client)
        self.id = id
        self.stars = stars
        self.convert_stars = convert_stars
        self.limited = limited
        self.sold_out = sold_out
        self.birthday = birthday
        self.require_premium = require_premium
        self.availability_remains = availability_remains
        self.availability_total = availability_total
        self.upgrade_stars = upgrade_stars
        self.first_sale_date = first_sale_date
        self.last_sale_date = last_sale_date
        self.title = title
        self.is_unique = is_unique
        self.slug = slug
        self.num = num
        self.attributes = attributes

    @staticmethod
    def _parse(client, gift) -> "StarGift":
        if isinstance(gift, raw.types.StarGiftUnique):
            return StarGift(
                client=client,
                id=gift.id,
                stars=0,
                convert_stars=0,
                is_unique=True,
                title=gift.title,
                slug=gift.slug,
                num=gift.num,
                attributes=types.List(
                    types.StarGiftAttribute._parse(client, a) for a in gift.attributes
                ) or None,
            )
        # StarGift (regular)
        return StarGift(
            client=client,
            id=gift.id,
            stars=gift.stars,
            convert_stars=gift.convert_stars,
            limited=getattr(gift, "limited", None),
            sold_out=getattr(gift, "sold_out", None),
            birthday=getattr(gift, "birthday", None),
            require_premium=getattr(gift, "require_premium", None),
            availability_remains=getattr(gift, "availability_remains", None),
            availability_total=getattr(gift, "availability_total", None),
            upgrade_stars=getattr(gift, "upgrade_stars", None),
            first_sale_date=utils.timestamp_to_datetime(gift.first_sale_date) if getattr(gift, "first_sale_date", None) else None,
            last_sale_date=utils.timestamp_to_datetime(gift.last_sale_date) if getattr(gift, "last_sale_date", None) else None,
            title=getattr(gift, "title", None),
            is_unique=False,
        )
