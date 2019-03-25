import unittest

import pytest

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

    def test_str(self):
        assert str(self.object_1) == '//div', \
            '__str__ for Xpath is not working correctly. Received {} instead of {}'.format(str(self.object_1), '//div')

    def test_arg_format_return(self):
        object_1 = Xpath('//div[class="{}"]')
        expected_string = '//div[class="ONE"]'
        assert str(object_1.format('ONE')) == expected_string, \
            'object_1.format(\'One\') is not {}, but instead {}'.format(expected_string, object_1.format('ONE'))

    def test_args_format_return(self):
        object_1 = Xpath('//div[class="{}"]|//span[type="{}"]')
        expected_string = '//div[class="ONE"]|//span[type="Two"]'
        assert str(object_1.format('ONE', 'Two')) == expected_string, \
            'object_1.format(\'One\', \'Two\') is not {}, but instead {}'.format(expected_string,
                                                                                 object_1.format('ONE', 'Two'))

    def test_kwarg_format_return(self):
        object_1 = Xpath('//div[class="{it}"]')
        expected_string = '//div[class="ONE"]'
        assert str(object_1.format(it='ONE')) == expected_string, \
            'object_1.format(it=\'One\') is not {}, but instead {}'.format(expected_string, object_1.format(it='ONE'))

    def test_kwargs_format_return(self):
        object_1 = Xpath('//div[class="{first}"]|//span[type="{second}"]')
        expected_string = '//div[class="ONE"]|//span[type="Two"]'
        assert str(object_1.format(first='ONE', second='Two')) == expected_string, \
            'object_1.format(\'One\', \'Two\') is not {}, but instead {}'.format(
                expected_string, object_1.format(first='ONE', second='Two'))

    def test_failure_format_kwargs(self):
        with pytest.raises(KeyError):
            object_1 = Xpath('//div[class="{first}"]|//span[type="{second}"]')
            object_1.format(third='wrong')

    def test_failure_format_args_but_kwargs_given(self):
        with pytest.raises(IndexError):
            object_1 = Xpath('//div[class="{}"]|//span[type="{}"]')
            object_1.format(third='wrong')

    def test_too_many_args_format(self):
        object_1 = Xpath('//div[class="{}"]|//span[type="{}"]')
        assert str(object_1.format('wrong', 'number', 'of arguments')) == '//div[class="wrong"]|//span[type="number"]'

    def test_failure_format_kwargs_but_args_given(self):
        with pytest.raises(KeyError):
            object_1 = Xpath('//div[class="{first}"]|//span[type="{second}"]')
            object_1.format('not', 'kwargs')

    def test_format_return_type(self):
        assert isinstance(Xpath('//div[class="{}"]').format('ONE'), Xpath), \
            'Xpath.format() is not a Xpath class object. Is {} instead.'.format(type(Xpath('//div[class="{}"]').format(
                'ONE')))

    def test_format_return_object(self):
        assert Xpath('//div[class="{}"]').format('ONE') == Xpath('//div[class="ONE"]'), \
            '"Xpath(\'//div[class="{}"]).format(\'ONE\')" is not the same object as: "Xpath(\'//div[class="ONE"]\')"'

    def test_failure_format_object(self):
        assert Xpath('//div[class="{}"]').format('ONE') != Xpath('//div[class="TWO"]'), \
            '"Xpath(\'//div[class="{}"]).format(\'ONE\')" is the same object as: Xpath(\'//div[class="TWO"]\')'

    def test_equal(self):
        assert self.object_1 == Xpath('//div'), '"self.object_1 == Xpath(\'//div\')" is False'

    def test_unequal(self):
        assert self.object_1 != self.object_2, '"self.object_1 != self.object_2" is True'

    def test_not_supported_type_add(self):
        with pytest.raises(TypeError):
            self.object_1 + 123

    def test_string_add(self):
        assert self.object_1 + 'Test' == '//divTest', 'Addition of: "{}" and "Test" gives {} instead of {}'.format(
            self.object_1, self.object_1 + 'Test', '//divTest')

    def test_string_add_with_or_operator(self):
        assert self.object_1 + '|/Test' == '//div|/Test', 'Addition of: "{}" and "Test" gives {} instead of {}'.format(
            self.object_1, self.object_1 + 'Test', '//div|/Test')

    def test_simple_xpath_add(self):
        assert self.object_1 + self.object_2 == '//div//span', \
            'Addition of: "{}" and "{}" gives {} instead of {}'.format(self.object_1, self.object_2,
                                                                       self.object_1 + self.object_2, '//div//span')

    def test_xpath_with_square_brackets_add(self):
        object_1 = Xpath("//div[@id='timezone']")
        object_2 = Xpath("//span[@class='btn btn-default form-control ui-select-toggle']")
        add_result = object_1 + object_2
        assert add_result == "//div[@id='timezone']//span[@class='btn btn-default form-control ui-select-toggle']", \
            "Addition result of {} and {} is {} instead of " \
            "//div[@id='timezone']//span[@class='btn btn-default form-control ui-select-toggle']".format(
                object_1, object_2, add_result)
