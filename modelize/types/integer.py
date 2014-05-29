# -*- coding: utf8 -*-
from ..handlers import Attribute, AttrModule
from ..validators.numbers import is_integer

class Integer(Attribute, int):
    on_get = AttrModule.Get()
    on_set = AttrModule.Set(condition=is_integer)
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()

