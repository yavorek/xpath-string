import unittest

from xpath_string.two_xpath_addition import TwoXpathAddition

param_list_add_two_xpath_without_contains = [
    ('//span', '//div', '//span//div'),
    ('//div|//svg', '//span', '//div//span|//svg//span'),
    ('//div', '//span|//svg', '//div//span|//div//svg'),
    ('//div|//span', '//avg|//span', '//div//avg|//span//avg|//div//span|//span//span')
]


class TestTwoXpathAddition(unittest.TestCase):

    def test_add_two_xpath_without_contains(self):
        for xpath_1, xpath_2, expected_result in param_list_add_two_xpath_without_contains:
            with self.subTest():
                set_result = set(TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together().split('|'))
                set_expected_result = set(expected_result.split('|'))
                assert set_result == set_expected_result, \
                    'Addition of {} and {} is "{}" different than expected "{}"'.format(
                        xpath_1, xpath_2, TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together(), expected_result)
