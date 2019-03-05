import unittest

from xpath_string.xpath import Xpath


class TestXpath(unittest.TestCase):

    def test_object_creation(self):
        object_1 = Xpath('//div')
        assert type(object_1) is Xpath, 'object is not a Xpath class object. Is {} instead'.format(type(object_1))

    def test_object_arg_check(self):
        object_2 = Xpath('//lin')
        assert object_2.xpath == '//lin', 'object xpath arg has value {} instead of {}'.format(object_2.xpath, '//lin')
