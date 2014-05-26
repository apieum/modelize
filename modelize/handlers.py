# -*- coding: utf8 -*-
from eventize.attribute import Attribute, Subject, OnGetDescriptor, OnSetDescriptor, OnDelDescriptor, OnChangeDescriptor

class GetHandler(OnGetDescriptor):
    __alias__ = 'on_get'

class SetHandler(OnSetDescriptor):
    __alias__ = 'on_set'

class DelHandler(OnDelDescriptor):
    __alias__ = 'on_del'

class ChangeHandler(OnChangeDescriptor):
    __alias__ = 'on_change'


class Attribute(Attribute):
    on_get    = GetHandler()
    on_set    = SetHandler()
    on_del    = DelHandler()
    on_change = ChangeHandler()


class AttrModule(object):
    Get = GetHandler
    Set = SetHandler
    Del = DelHandler
    Change = ChangeHandler
