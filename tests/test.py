import unittest

from xpath_string.xpath import Xpath


class TestXpath(unittest.TestCase):
    def setUp(self):
        self.object_1 = Xpath('//div')

    def test_object_creation(self):
        assert type(self.object_1) is Xpath, \
            'object is not a Xpath class object. Is {} instead'.format(type(self.object_1))

    def test_object_arg_check(self):
        assert self.object_1.xpath == '//div', \
            'object xpath arg has value {} instead of {}'.format(self.object_1.xpath, '//div')
