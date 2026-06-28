<p align="center">
    <a href="https://github.com/maxsepp/sepgram">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Sepgram" width="128">
    </a>
    <br>
    <b>Sepgram</b>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
</p>

<p align="center">
    <a href="https://github.com/maxsepp/sepgram">
        GitHub
    </a>
    •
    <a href="https://docs.pyrogram.org">
        Documentation
    </a>
</p>

---

## About

**Sepgram** is a modern, elegant and asynchronous Telegram MTProto API framework in Python for users and bots. Dengan fitur tambahan dan update layer terbaru.

- **Layer**: 225 (terbaru)
- **Version**: 2.0.225
- **Python**: 3.8+

```python
from pyrogram import Client, filters

app = Client("my_account")

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Sepgram!")

app.run()
```

---

## Installation

```bash
pip install git+https://github.com/maxsepp/sepgram
```

---

## Features & Support

### 🔌 Core

| Feature | Status |
|---------|--------|
| MTProto API Layer 225 | ✅ |
| Userbot & Bot support | ✅ |
| Async & Sync mode | ✅ |
| TgCrypto (C crypto) | ✅ |
| Type-hinted | ✅ |
| Session string support | ✅ |
| SQLite / Memory storage | ✅ |
| Proxy support (TCP) | ✅ |
| Multiple sessions | ✅ |
| Auto-reconnect | ✅ |

### 💬 Messages

| Feature | Status |
|---------|--------|
| Send text, photo, video, audio, document, sticker | ✅ |
| Send animation (GIF) | ✅ |
| Send voice & video note | ✅ |
| Send location & venue | ✅ |
| Send contact | ✅ |
| Send dice | ✅ |
| Send poll | ✅ |
| Send media group | ✅ |
| Send cached media | ✅ |
| Send game | ✅ |
| Forward messages | ✅ |
| Copy messages | ✅ |
| Edit messages (text, caption, media, reply_markup) | ✅ |
| Delete messages | ✅ |
| Pin / unpin messages | ✅ |
| Search messages (chat & global) | ✅ |
| Get chat history | ✅ |
| Get media group | ✅ |
| Download & stream media | ✅ |
| Send reactions | ✅ |
| Read reactions | ✅ |
| Schedule messages | ✅ |
| Discussion replies | ✅ |
| Screenshot notification | ✅ |

### 📖 Stories

| Feature | Status |
|---------|--------|
| Send story | ✅ |
| Edit story | ✅ |
| Delete stories | ✅ |
| Forward story | ✅ |
| Copy story | ✅ |
| Get stories (peer, pinned, archive, all) | ✅ |
| Pin / hide stories | ✅ |
| Story albums (create, update, delete, get) | ✅ |
| Increment story views | ✅ |
| Read stories | ✅ |
| Export story link | ✅ |
| Can send story check | ✅ |

### ⭐ Premium & Stars

| Feature | Status |
|---------|--------|
| Get stars balance | ✅ |
| Get stars status | ✅ |
| Get stars transactions | ✅ |
| Send star gift | ✅ |
| Save star gift | ✅ |
| Convert star gift | ✅ |
| Upgrade star gift | ✅ |
| Get star gifts | ✅ |
| Update star referral program | ✅ |
| Apply boost | ✅ |
| Get boosts / boosts status | ✅ |
| Custom emoji stickers | ✅ |
| Emoji status | ✅ |

### 👥 Chats & Groups

| Feature | Status |
|---------|--------|
| Create channel / group / supergroup | ✅ |
| Delete channel / supergroup | ✅ |
| Join / leave chat | ✅ |
| Get chat info | ✅ |
| Get chat members | ✅ |
| Ban / unban / restrict / promote members | ✅ |
| Set chat title, photo, description, username | ✅ |
| Set permissions | ✅ |
| Set slow mode | ✅ |
| Set protected content | ✅ |
| Archive / unarchive chats | ✅ |
| Mark chat unread | ✅ |
| Get common chats | ✅ |
| Get online count | ✅ |
| Transfer chat ownership | ✅ |
| Delete user history | ✅ |
| Get send as chats | ✅ |
| Chat notifications | ✅ |
| Chat event log | ✅ |

### 📂 Forum Topics

| Feature | Status |
|---------|--------|
| Create forum topic | ✅ |
| Edit forum topic | ✅ |
| Delete forum topic | ✅ |
| Close / reopen forum topic | ✅ |
| Get forum topics | ✅ |
| Toggle forum topics | ✅ |
| Hide / unhide general topic | ✅ |
| Edit / reopen general topic | ✅ |

### 🔗 Invite Links

| Feature | Status |
|---------|--------|
| Export chat invite link | ✅ |
| Create chat invite link | ✅ |
| Edit chat invite link | ✅ |
| Revoke chat invite link | ✅ |
| Delete chat invite links | ✅ |
| Get invite link joiners | ✅ |
| Get chat join requests | ✅ |
| Approve / decline join requests | ✅ |
| Export folder link | ✅ |

### 🤖 Bots

| Feature | Status |
|---------|--------|
| Answer callback query | ✅ |
| Answer inline query | ✅ |
| Answer web app query | ✅ |
| Answer guest query | ✅ |
| Get inline bot results | ✅ |
| Send inline bot result | ✅ |
| Set/get bot commands | ✅ |
| Set/get bot default privileges | ✅ |
| Set/get chat menu button | ✅ |
| Get bot recommendations | ✅ |
| Request callback answer | ✅ |
| Set game score / get high scores | ✅ |
| Edit inline text/caption/media/reply_markup | ✅ |

### 💳 Payments

| Feature | Status |
|---------|--------|
| Stars payments | ✅ |
| Stars transactions | ✅ |
| Star gifts (send, save, convert, upgrade) | ✅ |

### 👤 Users & Contacts

| Feature | Status |
|---------|--------|
| Get users | ✅ |
| Get me | ✅ |
| Get contacts | ✅ |
| Add / import / delete contacts | ✅ |
| Block / unblock user | ✅ |
| Update profile | ✅ |
| Set profile photo | ✅ |
| Delete profile photos | ✅ |
| Set username | ✅ |
| Update color | ✅ |
| Update status | ✅ |
| Get sessions | ✅ |
| Set custom verification | ✅ |

### 📁 Folders

| Feature | Status |
|---------|--------|
| Get folders | ✅ |
| Get folder | ✅ |
| Update folder | ✅ |
| Delete folder | ✅ |
| Export folder link | ✅ |

### 🎨 Stickers

| Feature | Status |
|---------|--------|
| Get sticker set | ✅ |
| Create sticker set | ✅ |
| Add sticker to set | ✅ |
| Get custom emoji stickers | ✅ |

### 🔐 Auth & Password

| Feature | Status |
|---------|--------|
| Send code | ✅ |
| Resend code | ✅ |
| Sign in / sign up | ✅ |
| Sign in bot | ✅ |
| Check password | ✅ |
| Enable / change / remove cloud password | ✅ |
| Get password hint | ✅ |
| Recover password | ✅ |
| Two-step verification | ✅ |
| Terms of service accept | ✅ |

### 🔧 Pyromod Extensions

| Feature | Status |
|---------|--------|
| `client.listen()` — wait for message/callback | ✅ |
| `client.ask()` — send & wait for reply | ✅ |
| `register_next_step_handler()` | ✅ |
| `stop_listener()` / `stop_listening()` | ✅ |
| Listener timeout handling | ✅ |
| Custom keyboard helpers (ikb, kb) | ✅ |
| InlineKeyboard with pagination | ✅ |
| Secret eval/shell commands (owner only) | ✅ |

### 🛠 Utilities

| Feature | Status |
|---------|--------|
| Compose (multi-client) | ✅ |
| Idle | ✅ |
| Export session string | ✅ |
| Text formatter (bold, italic, code, etc.) | ✅ |
| Available effects | ✅ |

### 📦 Handlers

| Handler | Event |
|---------|-------|
| `on_message` | New messages |
| `on_edited_message` | Edited messages |
| `on_deleted_messages` | Deleted messages |
| `on_callback_query` | Callback query (button press) |
| `on_inline_query` | Inline query |
| `on_chosen_inline_result` | Chosen inline result |
| `on_chat_member_updated` | Chat member changes |
| `on_chat_join_request` | Join requests |
| `on_poll` | Poll updates |
| `on_user_status` | User online/offline |
| `on_story` | New stories |
| `on_disconnect` | Client disconnect |
| `on_raw_update` | Raw MTProto updates |
| `ErrorHandler` | Exception handling |

### 🔍 Filters

Built-in filters: `private`, `group`, `channel`, `text`, `photo`, `video`, `audio`, `document`, `sticker`, `animation`, `voice`, `video_note`, `contact`, `location`, `venue`, `dice`, `game`, `poll`, `media`, `command`, `regex`, `user`, `chat`, `forwarded`, `reply`, `caption`, `mentioned`, `via_bot`, `service`, `media_group`, `scheduled`, `from_scheduled`, `linked_channel`, `forum_topic`, `story`, `bot`, `new_chat_members`, `left_chat_member`, dan lainnya.

---

## Quick Examples

### Listen for reply (Pyromod)

```python
response = await client.ask(chat_id, "What's your name?")
await client.send_message(chat_id, f"Hello {response.text}!")
```

### Inline Keyboard

```python
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("Button 1", callback_data="btn1"),
     InlineKeyboardButton("Button 2", callback_data="btn2")],
    [InlineKeyboardButton("URL", url="https://telegram.org")]
])

await client.send_message(chat_id, "Choose:", reply_markup=markup)
```

### Download Media

```python
@app.on_message(filters.photo)
async def download(client, message):
    await message.download()
```

### Stories

```python
await client.send_story(privacy=enums.StoriesPrivacyRules.PUBLIC, photo="pic.jpg", caption="My story!")
```

---

## License

Sepgram is licensed under the [GNU Lesser General Public License v3.0](COPYING.lesser).
