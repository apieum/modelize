# -*- coding: utf8 -*-
from .string import String
from .integer import Integer
from .float import Float
from .email import Email, StrictEmail

__all__ = ['String', 'Email', 'StrictEmail', 'Integer', 'Float']
