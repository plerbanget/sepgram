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

from . import types, functions, base, core
from .all import objects as _objects_raw

from importlib import import_module


class _LazyObjects:
    def __init__(self, data):
        self._data = data

    def _resolve(self, k):
        v = self._data[k]
        if isinstance(v, str):
            path, name = v.rsplit(".", 1)
            obj = getattr(import_module(path), name)
            self._data[k] = obj
            return obj
        return v

    def __getitem__(self, k):
        return self._resolve(k)

    def __setitem__(self, k, v):
        self._data[k] = v

    def __contains__(self, k):
        return k in self._data

    def __iter__(self):
        return iter(self._data)

    def keys(self):
        return self._data.keys()

    def values(self):
        return (self._resolve(k) for k in self._data)

    def items(self):
        return ((k, self._resolve(k)) for k in self._data)

    def get(self, k, default=None):
        if k in self._data:
            return self._resolve(k)
        return default


objects = _LazyObjects(_objects_raw)
