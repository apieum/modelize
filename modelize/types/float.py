# -*- coding: utf8 -*-
from ..handlers import Attribute, AttrModule
from ..validators.numbers import is_float

class Float(Attribute, float):
    on_get = AttrModule.Get()
    on_set = AttrModule.Set(condition=is_float)
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()

