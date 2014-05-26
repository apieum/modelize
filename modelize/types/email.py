# -*- coding: utf8 -*-
import re
from ..handlers import Attribute, AttrModule
from .string import is_string, String


user_match = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*").match
domain_match = re.compile("(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?").match


def is_mail(event):
    is_string(event)
    address = event.value.split('@')
    if len(address) != 2:
        raise TypeError("an email address must contains @")

    user, domain = address
    if user_match(user) is None:
        raise TypeError("'%s' is not a valid user for an email address" % user)
    if domain_match(domain) is None:
        raise TypeError("'%s' is not a valid domain for an email address" % domain)
    return True



class Email(String):
    on_set = AttrModule.Set(condition=is_mail)
    on_get = AttrModule.Get()
    on_del = AttrModule.Del()
    on_change = AttrModule.Change()
