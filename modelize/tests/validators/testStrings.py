# -*- coding: utf8 -*-
from .. import TestCase
from modelize.validators import strings


class StringsValidateTest(TestCase):
    def test_has_one_at(self):
        self.assertTrue(strings.has_one_at('@'))
        self.assertFalse(strings.has_one_at('@@'))
        self.assertTrue(strings.has_one_at('\@'))

    def test_has_user(self):
        self.assertTrue(strings.has_user('-_-user@'))
        self.assertFalse(strings.has_user('@domain'))

    def test_has_strict_user(self):
        self.assertTrue(strings.has_strict_user('user@'))
        self.assertFalse(strings.has_strict_user('User@domain'))
        self.assertTrue(strings.has_strict_user('us@'))
        self.assertFalse(strings.has_strict_user('-u@domain'))

    def test_has_domain(self):
        self.assertTrue(strings.has_domain('@domain.com'))
        self.assertFalse(strings.has_domain('user@'))
        self.assertFalse(strings.has_domain('@domain'))

