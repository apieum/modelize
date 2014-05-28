# -*- coding: utf8 -*-
from ..handlers import Attribute, AttrModule
from ..validators.strings import is_string

class String(Attribute, str):
    on_set = AttrModule.Get(condition=is_string)
    on_get = AttrModule.Set()
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()

