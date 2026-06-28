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

from .can_send_story import CanSendStory
from .copy_story import CopyStory
from .create_story_album import CreateStoryAlbum
from .delete_stories import DeleteStories
from .delete_story_album import DeleteStoryAlbum
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .forward_story import ForwardStory
from .get_all_stories import GetAllStories
from .get_peer_stories import GetPeerStories
from .get_pinned_stories import GetPinnedStories
from .get_stories import GetStories
from .get_stories_archive import GetStoriesArchive
from .get_story_albums import GetStoryAlbums
from .hide_stories import HideStories
from .increment_story_views import IncrementStoryViews
from .pin_stories import PinStories
from .read_stories import ReadStories
from .send_story import SendStory
from .update_story_album import UpdateStoryAlbum

class Stories(
    CanSendStory,
    CopyStory,
    CreateStoryAlbum,
    DeleteStories,
    DeleteStoryAlbum,
    EditStory,
    ExportStoryLink,
    ForwardStory,
    GetAllStories,
    GetPeerStories,
    GetPinnedStories,
    GetStories,
    GetStoriesArchive,
    GetStoryAlbums,
    HideStories,
    IncrementStoryViews,
    PinStories,
    ReadStories,
    SendStory,
    UpdateStoryAlbum,
):
    pass
