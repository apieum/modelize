# -*- coding: utf8 -*-
from ..handlers import Attribute, AttrModule
from ..validators.strings import is_string

class String(Attribute, str):
    on_get = AttrModule.Get()
    on_set = AttrModule.Set(condition=is_string)
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()

