# -*- coding: utf8 -*-
from .. import TestCase
from modelize.types import String

class StringTest(TestCase):
    def test_it_is_instance_of_str(self):
        obj = self.make_obj()
        self.assertIsInstance(obj, str)

    def test_it_can_be_converted_to_str(self):
        expected = "a string"
        obj = self.make_obj(expected)
        self.assertEqual(obj, expected)

    def test_it_raise_type_error_if_value_is_not_a_string(self):
        expected = 10.42
        class model(object):
            text = self.make_obj(expected)
        with self.assertRaises(TypeError):
            obj = model()
            obj.text

    def make_obj(self, value=None):
        if value is None:
            return String()
        else:
            return String(value)
