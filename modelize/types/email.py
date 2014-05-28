# -*- coding: utf8 -*-
from ..handlers import Attribute, AttrModule
from .string import String
from ..validators.strings import is_email, is_strict_email


class Email(String):
    on_set = AttrModule.Set(condition=is_email)
    on_get = AttrModule.Get()
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()


class StrictEmail(String):
    on_set = AttrModule.Set(condition=is_strict_email)
    on_get = AttrModule.Get()
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()
