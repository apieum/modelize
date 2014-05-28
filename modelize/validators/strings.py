# -*- coding: utf8 -*-
import re
from .exception import ValidationError

def is_string(event):
    if isinstance(event.value, str): return True
    value = getattr(event, 'value', 'undefined_value')
    name = getattr(event, 'name', 'unknown_attribute')
    cls_name = getattr(type(event.subject), '__name__', 'class')
    raise ValidationError("%s.%s = '%s' must be a str." % (cls_name, name, value))




user_match = re.compile("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*$").match
domain_match = re.compile("^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$").match

strict_user_match = re.compile("^[a-z0-9][a-z0-9_-]+(?:\.[a-z0-9_-]+)*$").match

def has_user_and_domain(email):
    address = email.split('@')
    if len(address) != 2:
        raise ValidationError("an email address must contains @")
    return address


def is_email(event):
    is_string(event)
    user, domain = has_user_and_domain(event.value)
    if user_match(user) is None:
        raise ValidationError("'%s' is not a valid user for an email address" % user)
    if domain_match(domain) is None:
        raise ValidationError("'%s' is not a valid domain for an email address" % domain)
    return True

def is_strict_email(event):
    is_string(event)
    user, domain = has_user_and_domain(event.value)
    if strict_user_match(user) is None:
        raise ValidationError("'%s' is not a valid user for an email address" % user)
    if domain_match(domain) is None:
        raise ValidationError("'%s' is not a valid domain for an email address" % domain)
    return True

