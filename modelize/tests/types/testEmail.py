# -*- coding: utf8 -*-
from .. import TestCase
from modelize.types import Email

def StringTest():
    from .testString import StringTest
    return StringTest


class EmailTest(StringTest()):
    def test_it_raises_type_error_if_value_has_not_at(self):
        expected = 'test'
        class model(object):
            text = self.make_obj(expected)
        with self.assertRaises(TypeError):
            obj = model()
            obj.text

    def test_it_raises_type_error_if_value_has_not_correct_userand_domain_name(self):
        class model(object):
            text = self.make_obj()
        obj = model()

        with self.assertRaises(TypeError):
            obj.text = '@domain.com'

        with self.assertRaises(TypeError):
            obj.text = 'user.good@domain'

        expected = 'user.good@domain.good'
        obj.text = expected
        self.assertEqual(obj.text, expected)

    def make_obj(self, *args):
        return Email(*args)
