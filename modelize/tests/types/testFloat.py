# -*- coding: utf8 -*-
from .. import TestCase
from modelize.types import Float

class FloatTest(TestCase):
    def test_it_is_instance_of_float(self):
        obj = self.make_obj()
        self.assertIsInstance(obj, float)

    def test_it_can_be_converted_to_float(self):
        expected = -10.0
        obj = self.make_obj(expected)
        self.assertEqual(obj, expected)

    def test_it_can_be_converted_to_int(self):
        expected = -42.2
        obj = self.make_obj(expected)
        self.assertEqual(int(obj), int(expected))

    def test_it_raise_type_error_if_value_is_not_a_float(self):
        class model(object):
            number = self.make_obj()
        with self.assertRaises(TypeError):
            obj = model()
            obj.number = 0o10

    def make_obj(self, *args):
        return Float(*args)
