# -*- coding: utf8 -*-
from .. import TestCase
from modelize.types import Integer

class IntegerTest(TestCase):
    def test_it_is_instance_of_int(self):
        obj = self.make_obj()
        self.assertIsInstance(obj, int)

    def test_it_can_be_converted_to_int(self):
        expected = 10
        obj = self.make_obj(expected)
        self.assertEqual(obj, expected)

    def test_it_can_be_converted_to_float(self):
        expected = 42
        obj = self.make_obj(expected)
        self.assertEqual(float(obj), float(expected))

    def test_it_raise_type_error_if_value_is_not_an_int(self):
        expected = 10.42
        class model(object):
            number = self.make_obj(expected)
        with self.assertRaises(TypeError):
            obj = model()
            obj.number

    def make_obj(self, *args):
        return Integer(*args)
