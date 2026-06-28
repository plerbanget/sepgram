#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Optional

from pyrogram import raw, enums, types
from ..object import Object


def _build_raw_style(style: "enums.ButtonStyle", icon: int = None) -> Optional["raw.types.KeyboardButtonStyle"]:
    if style is None or style == enums.ButtonStyle.DEFAULT:
        return None
    return raw.types.KeyboardButtonStyle(
        bg_primary=(style == enums.ButtonStyle.PRIMARY),
        bg_danger=(style == enums.ButtonStyle.DANGER),
        bg_success=(style == enums.ButtonStyle.SUCCESS),
        icon=icon,
    )


class KeyboardButton(Object):
    """One button of the reply keyboard.

    For simple text buttons String can be used instead of this object to specify text of the button.
    Optional fields are mutually exclusive.

    Parameters:
        text (``str``):\n            Text of the button.

        request_contact (``bool``, *optional*):\n            If True, the user's phone number will be sent as a contact when the button is pressed.

        request_location (``bool``, *optional*):\n            If True, the user's current location will be sent when the button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):\n            If specified, the described Web App will be launched when the button is pressed.

        style (:obj:`~pyrogram.enums.ButtonStyle`, *optional*):\n            Button color style. Use PRIMARY, DANGER, or SUCCESS.

        style_icon (``int``, *optional*):\n            Custom emoji ID to use as an icon on the button.
    """

    def __init__(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        web_app: "types.WebAppInfo" = None,
        style: "enums.ButtonStyle" = None,
        style_icon: Optional[int] = None,
    ):
        super().__init__()

        self.text = str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
        self.style = style
        self.style_icon = style_icon

    @staticmethod
    def read(b):
        if isinstance(b, raw.types.KeyboardButton):
            return b.text

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            return KeyboardButton(
                text=b.text,
                request_contact=True
            )

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            return KeyboardButton(
                text=b.text,
                request_location=True
            )

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            return KeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url)
            )

    def write(self):
        raw_style = _build_raw_style(self.style, self.style_icon)

        if self.request_contact:
            return raw.types.KeyboardButtonRequestPhone(text=self.text, style=raw_style)
        elif self.request_location:
            return raw.types.KeyboardButtonRequestGeoLocation(text=self.text, style=raw_style)
        elif self.web_app:
            return raw.types.KeyboardButtonSimpleWebView(text=self.text, url=self.web_app.url, style=raw_style)
        else:
            return raw.types.KeyboardButton(text=self.text, style=raw_style)
