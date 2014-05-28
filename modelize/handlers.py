# -*- coding: utf8 -*-
from eventize.attribute import Attribute, Subject, OnGetHandler, OnSetHandler, OnDelHandler, OnChangeHandler

class GetHandler(OnGetHandler):
    __alias__ = 'on_get'

class SetHandler(OnSetHandler):
    __alias__ = 'on_set'

class DelHandler(OnDelHandler):
    __alias__ = 'on_del'

class ChangeHandler(OnChangeHandler):
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
