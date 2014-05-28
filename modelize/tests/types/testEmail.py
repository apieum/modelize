# -*- coding: utf8 -*-
from .. import TestCase
from modelize.types import Email, StrictEmail

def StringTest():
    from .testString import StringTest
    return StringTest


class EmailTest(StringTest()):
    def setUp(self):
        class model(object):
            text = self.make_obj()
        self.obj = model()

    def test_it_must_have_at(self):
        with self.assertRaises(TypeError):
            self.obj.text = 'test'

    def test_it_must_have_user_and_domain(self):
        with self.assertRaises(TypeError):
            self.obj.text = '@domain.com'

        with self.assertRaises(TypeError):
            self.obj.text = 'user12.good@domain'

        with self.assertRaises(TypeError):
            self.obj.text = 'user12@bad@domain'

        expected = 'user12.good@domain.good'
        self.obj.text = expected
        self.assertEqual(self.obj.text, expected)

    def make_obj(self, *args):
        return Email(*args)

class StrictEmailTest(EmailTest):
    def test_user_and_domain_must_not_have_special_chars_except_dash_and_underscore(self):
        with self.assertRaises(TypeError):
            self.obj.text = '~user13.good@domain.good'

        with self.assertRaises(TypeError):
            self.obj.text = 'user13-good?@domain.good'

    def test_user_must_start_by_letter_or_number_and_have_more_than_one_char(self):
        with self.assertRaises(TypeError):
            self.obj.text = 'a@domain.good'

        with self.assertRaises(TypeError):
            self.obj.text = '_a@domain.good'

        with self.assertRaises(TypeError):
            self.obj.text = '-a@domain.good'

        expected = 'aa@domain.good'
        self.obj.text = expected
        self.assertEqual(self.obj.text, expected)


    def make_obj(self, *args):
        return StrictEmail(*args)
