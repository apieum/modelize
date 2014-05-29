# -*- coding: utf8 -*-
import re
from .validator import Validator


user_match = re.compile("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*$").match
domain_match = re.compile("^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$").match
strict_user_match = re.compile("^[a-z0-9][a-z0-9_-]+(?:\.[a-z0-9_-]+)*$").match


def instance_of_str(value):
    return isinstance(value, str)

def has_one_at(email):
    return email.count('@') == 1

def has_user(value):
    user = value[:value.index('@')]
    return user_match(user) is not None

def has_strict_user(value):
    user = value[:value.index('@')]
    return strict_user_match(user) is not None

def has_domain(value):
    domain = value[value.index('@') + 1:]
    return domain_match(domain) is not None

is_email = Validator()
is_email += instance_of_str, "{cls_name}.{name} = '{value}' must be a str."
is_email += has_one_at, "an email address must contains one @"
is_email += has_user, "'{value}' is not a valid user for an email address"
is_email += has_domain, "'{value}' is not a valid domain for an email address"

is_strict_email = is_email.duplicate()
is_strict_email.callbacks[2] = has_strict_user, "'{value}' is not a valid user for an email address"

is_string = Validator((instance_of_str, "{cls_name}.{name} = '{value}' must be a str."))
