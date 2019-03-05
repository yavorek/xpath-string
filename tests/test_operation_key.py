import unittest

from xpath_string.two_xpath_addition import TwoXpathAddition

param_list_two_xpath_without_contains = [
    ('//div', '//span', '00'),
    ('//div|', '//span', '10'),
    ('//div', '//span|', '01'),
    ('//div|', '//span|', '11'),
    ('//div/span[1]', '//none', '00'),
    ('//div|//span|//afv', '//node', '10')
]

param_list_two_xpath_with_contains = [
    ('//*[contains(@options|@lol)]/div', '//span', '00'),
    ('//*[contains(@options|@lol)]/div|//span', '//span', '10'),
    ('//div', '//*[contains(@options|@lol)]/div|//span', '01'),
    ('//*[contains(@options|@lol|@more, "that")]/div|//span', '//*[contains(@options|@lol)]/div|//span', '11'),
    ('//*[contains(@more, "that|thing")]/div', '//span', '00'),
    ('//*[contains(@more, "that|thing")]/div|//multiple/div|//span', '//span', '10')
]


class TestOperationKey(unittest.TestCase):

    def test_two_xpath_without_contains(self):
        for xpath_1, xpath_2, result in param_list_two_xpath_without_contains:
            with self.subTest():
                assert TwoXpathAddition(xpath_1, xpath_2).operation_key == result, \
                    'Operation Key is {} instead of {} for xpath: "{}" and "{}"'.format(
                        TwoXpathAddition(xpath_1, xpath_2).operation_key, result, xpath_1, xpath_2)

    def test_two_xpath_with_contains(self):
        for xpath_1, xpath_2, result in param_list_two_xpath_with_contains:
            with self.subTest():
                assert TwoXpathAddition(xpath_1, xpath_2).operation_key == result, \
                    'Operation Key is {} instead of {} for xpath: "{}" and "{}"'.format(
                        TwoXpathAddition(xpath_1, xpath_2).operation_key, result, xpath_1, xpath_2)
