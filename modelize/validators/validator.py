# -*- coding: utf8 -*-
from string import Formatter


class Validator(object):
    formatter = Formatter()
    def __init__(self, *callbacks):
        self.callbacks = list(callbacks)

    def check(self, event):
        value = getattr(event, 'value')
        subject = getattr(event, 'subject', 'undefined_subject')
        name = getattr(event, 'name', 'unknown_attribute')
        cls_name = getattr(type(subject), '__name__', 'class')
        for callback, message in self.callbacks:
            if not callback(value):
                self.trigger_error(message, name=name, value=value, subject=subject, cls_name=cls_name)

    def trigger_error(self, message, *args, **kwargs):
        raise ValidationError(self.formatter.format(message, *args, **kwargs))

    __call__ = check

    def __iadd__(self, value):
        self.callbacks.append(value)
        return self

    def __isub__(self, value):
        while value in self.callbacks:
            self.callbacks.remove(value)
        return self

    def duplicate(self):
        return type(self)(*self.callbacks)



class ValidationError(TypeError):
    pass

