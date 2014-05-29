# -*- coding: utf8 -*-
from .validator import Validator


def instance_of_int(value):
    return isinstance(value, int)


is_integer = Validator((instance_of_int, "{cls_name}.{name} = '{value}' must be an int."))
