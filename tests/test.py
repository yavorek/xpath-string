import unittest

from xpath_string.xpath import Xpath


class TestXpath(unittest.TestCase):
    def setUp(self):
        self.object_1 = Xpath('//div')
        self.object_2 = Xpath('//span')

    def test_object_creation(self):
        assert isinstance(self.object_1, Xpath), \
            'object is not a Xpath class object. Is {} instead'.format(type(self.object_1))

    def test_object_arg_check(self):
        assert self.object_1.xpath == '//div', \
            'object xpath arg has value {} instead of {}'.format(self.object_1.xpath, '//div')

    def test_string_add(self):
        assert self.object_1 + 'Test', 'Addition of: "{}" and "Test" gives {} instead of {}'.format(
            self.object_1, self.object_1 + 'Test', '//divTest')

    def test_simple_xpath_add(self):
        assert self.object_1 + self.object_2 == '//div//span', \
            'Addition of: "{}" and "{}" gives {} instead of {}'.format(self.object_1, self.object_2,
                                                                       self.object_1 + self.object_2, '//div//span')
