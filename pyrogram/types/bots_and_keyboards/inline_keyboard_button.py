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

from typing import Union, Optional

import pyrogram
from pyrogram import raw, enums
from pyrogram import types
from ..object import Object


def _build_raw_style(style: "enums.ButtonStyle", icon: int = None) -> Optional["raw.types.KeyboardButtonStyle"]:
    """Convert ButtonStyle enum to raw KeyboardButtonStyle TL object."""
    if style is None or style == enums.ButtonStyle.DEFAULT:
        return None
    return raw.types.KeyboardButtonStyle(
        bg_primary=(style == enums.ButtonStyle.PRIMARY),
        bg_danger=(style == enums.ButtonStyle.DANGER),
        bg_success=(style == enums.ButtonStyle.SUCCESS),
        icon=icon,
    )


def _read_raw_style(b) -> Optional["enums.ButtonStyle"]:
    """Read raw KeyboardButtonStyle and return ButtonStyle enum."""
    if not hasattr(b, "style") or b.style is None:
        return None
    s = b.style
    if getattr(s, "bg_primary", False):
        return enums.ButtonStyle.PRIMARY
    if getattr(s, "bg_danger", False):
        return enums.ButtonStyle.DANGER
    if getattr(s, "bg_success", False):
        return enums.ButtonStyle.SUCCESS
    return enums.ButtonStyle.DEFAULT


class InlineKeyboardButton(Object):
    """One button of an inline keyboard.

    You must use exactly one of the optional fields.

    Parameters:
        text (``str``):\n            Label text on the button.

        callback_data (``str`` | ``bytes``, *optional*):\n            Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes.

        url (``str``, *optional*):\n            HTTP url to be opened when button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):\n            Description of the Web App that will be launched when the user presses the button.

        login_url (:obj:`~pyrogram.types.LoginUrl`, *optional*):\n             An HTTP URL used to automatically authorize the user.

        user_id (``int``, *optional*):\n            User id, for links to the user profile.

        switch_inline_query (``str``, *optional*):\n            If set, pressing the button will prompt the user to select one of their chats.

        switch_inline_query_current_chat (``str``, *optional*):\n            If set, pressing the button will insert the bot's username in the current chat's input.

        callback_game (:obj:`~pyrogram.types.CallbackGame`, *optional*):\n            Description of the game that will be launched when the user presses the button.

        copy_text (``str``, *optional*):\n            A button that copies specified text to clipboard. Limited to 256 characters.

        style (:obj:`~pyrogram.enums.ButtonStyle`, *optional*):\n            Button color style. Use :obj:`~pyrogram.enums.ButtonStyle.PRIMARY` for blue,
            :obj:`~pyrogram.enums.ButtonStyle.DANGER` for red, or
            :obj:`~pyrogram.enums.ButtonStyle.SUCCESS` for green.
            Defaults to :obj:`~pyrogram.enums.ButtonStyle.DEFAULT` (no color).

        style_icon (``int``, *optional*):\n            Custom emoji ID to show as an icon on the button (used together with ``style``).
    """

    def __init__(
        self,
        text: str,
        callback_data: Union[str, bytes] = None,
        url: str = None,
        web_app: "types.WebAppInfo" = None,
        login_url: "types.LoginUrl" = None,
        user_id: int = None,
        switch_inline_query: str = None,
        switch_inline_query_current_chat: str = None,
        callback_game: "types.CallbackGame" = None,
        copy_text: Optional[str] = None,
        style: "enums.ButtonStyle" = None,
        style_icon: Optional[int] = None,
    ):
        super().__init__()

        self.text = str(text)
        self.callback_data = callback_data
        self.url = url
        self.web_app = web_app
        self.login_url = login_url
        self.user_id = user_id
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.copy_text = copy_text
        self.style = style
        self.style_icon = style_icon

    @staticmethod
    def read(b: "raw.base.KeyboardButton"):
        if isinstance(b, raw.types.KeyboardButtonCallback):
            try:
                data = b.data.decode()
            except UnicodeDecodeError:
                data = b.data

            return InlineKeyboardButton(
                text=b.text,
                callback_data=data,
                style=_read_raw_style(b),
                style_icon=getattr(b.style, "icon", None) if getattr(b, "style", None) else None,
            )

        if isinstance(b, raw.types.KeyboardButtonUrl):
            return InlineKeyboardButton(
                text=b.text,
                url=b.url,
                style=_read_raw_style(b),
                style_icon=getattr(b.style, "icon", None) if getattr(b, "style", None) else None,
            )

        if isinstance(b, raw.types.KeyboardButtonUrlAuth):
            return InlineKeyboardButton(
                text=b.text,
                login_url=types.LoginUrl.read(b)
            )

        if isinstance(b, raw.types.KeyboardButtonUserProfile):
            return InlineKeyboardButton(
                text=b.text,
                user_id=b.user_id
            )

        if isinstance(b, raw.types.KeyboardButtonSwitchInline):
            if b.same_peer:
                return InlineKeyboardButton(
                    text=b.text,
                    switch_inline_query_current_chat=b.query,
                    style=_read_raw_style(b),
                )
            else:
                return InlineKeyboardButton(
                    text=b.text,
                    switch_inline_query=b.query,
                    style=_read_raw_style(b),
                )

        if isinstance(b, raw.types.KeyboardButtonGame):
            return InlineKeyboardButton(
                text=b.text,
                callback_game=types.CallbackGame()
            )

        if isinstance(b, raw.types.KeyboardButtonWebView):
            return InlineKeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url)
            )

        if isinstance(b, raw.types.KeyboardButtonCopy):
            return InlineKeyboardButton(
                text=b.text,
                copy_text=b.copy_text,
                style=_read_raw_style(b),
            )

        if isinstance(b, raw.types.KeyboardButton):
            return InlineKeyboardButton(
                text=b.text,
                style=_read_raw_style(b),
            )

    async def write(self, client: "pyrogram.Client"):
        raw_style = _build_raw_style(self.style, self.style_icon)

        if self.callback_data is not None:
            data = bytes(self.callback_data, "utf-8") if isinstance(self.callback_data, str) else self.callback_data
            return raw.types.KeyboardButtonCallback(
                text=self.text,
                data=data,
                style=raw_style,
            )

        if self.url is not None:
            return raw.types.KeyboardButtonUrl(
                text=self.text,
                url=self.url,
                style=raw_style,
            )

        if self.login_url is not None:
            return self.login_url.write(
                text=self.text,
                bot=await client.resolve_peer(self.login_url.bot_username or "self")
            )

        if self.user_id is not None:
            return raw.types.InputKeyboardButtonUserProfile(
                text=self.text,
                user_id=await client.resolve_peer(self.user_id),
                style=raw_style,
            )

        if self.switch_inline_query is not None:
            return raw.types.KeyboardButtonSwitchInline(
                text=self.text,
                query=self.switch_inline_query,
                style=raw_style,
            )

        if self.switch_inline_query_current_chat is not None:
            return raw.types.KeyboardButtonSwitchInline(
                text=self.text,
                query=self.switch_inline_query_current_chat,
                same_peer=True,
                style=raw_style,
            )

        if self.callback_game is not None:
            return raw.types.KeyboardButtonGame(
                text=self.text,
                style=raw_style,
            )

        if self.web_app is not None:
            return raw.types.KeyboardButtonWebView(
                text=self.text,
                url=self.web_app.url,
                style=raw_style,
            )

        if self.copy_text is not None:
            return raw.types.KeyboardButtonCopy(
                text=self.text,
                copy_text=self.copy_text,
                style=raw_style,
            )

        # Plain button
        return raw.types.KeyboardButton(
            text=self.text,
            style=raw_style,
        )
