# -*- coding: utf8 -*-
from .validator import Validator


def instance_of_int(value):
    return isinstance(value, int)

def instance_of_float(value):
    return isinstance(value, float)


is_integer = Validator((instance_of_int, "{cls_name}.{name} = '{value}' must be an int."))
is_float = Validator((instance_of_float, "{cls_name}.{name} = '{value}' must be a float."))
