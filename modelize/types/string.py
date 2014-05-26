# -*- coding: utf8 -*-
import re
from ..handlers import Attribute, AttrModule

def is_string(event):
    if isinstance(event.value, str): return True
    value = getattr(event, 'value', 'undefined_value')
    name = getattr(event, 'name', 'unknown_attribute')
    cls_name = getattr(type(event.subject), '__name__', 'class')
    raise TypeError("%s.%s = '%s' must be a str." % (cls_name, name, value))


class String(Attribute, str):
    on_set = AttrModule.Get(condition=is_string)
    on_get = AttrModule.Set()
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()

