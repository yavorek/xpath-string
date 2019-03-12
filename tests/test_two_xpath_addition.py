import unittest

from xpath_string.two_xpath_addition import TwoXpathAddition

param_list_add_two_xpath_without_contains = [
    ('//span', '//div', '//span//div'),
    ('//div|//svg', '//span', '//div//span|//svg//span'),
    ('//div', '//span|//svg', '//div//span|//div//svg'),
    ('//div|//span', '//avg|//span', '//div//avg|//span//avg|//div//span|//span//span'),
    ('//div//span', '|//avg', '//div//span|//div//span//avg'),
    ('//div//span', '//avg|', '//div//span|//div//span//avg'),
    ('//div|', '//avg', '//div//avg|//avg'),
    ('|//div', '//avg', '//div//avg|//avg'),
    ('|//div', '|//avg', '|//div|//avg|//div//avg'),
    ('|//div', '//avg|', '|//div|//avg|//div//avg'),
    ('//div|', '|//avg', '|//div|//avg|//div//avg'),
    ('//div|', '//avg|', '|//div|//avg|//div//avg'),
    ('//div[@class|@type="mine"]', '//avg', '//div[@class|@type="mine"]//avg'),
    ('//div|//span[@class="abc"]//a|//a', '//avg[@name="ans"]|//avg/span/span', '//div//avg[@name="ans"]|//div//avg/span/span|//span[@class="abc"]//a//avg[@name="ans"]|//span[@class="abc"]//a//avg/span/span|//a//avg[@name="ans"]|//a//avg/span/span')
]


param_list_add_two_xpath_with_contains = [
    ('//div[contains(a)]', '//a', '//div[contains(a)]//a'),
    ('//zdf', '//avg[@class="a"]//div[contains(@abc, "base")]', '//zdf//avg[@class="a"]//div[contains(@abc, "base")]'),
    ('//div[contains(a|b|c)]', '//a', '//div[contains(a|b|c)]//a'),
    ('//link', '//span[@contains(d|@name, "blob")]', '//link//span[@contains(d|@name, "blob")]'),
    ('//a[contains(b|c)]|//b', '/f', '//a[contains(b|c)]/f|//b/f'),
    ('//a|//b', '/f[contains(b|c)]', '//a/f[contains(b|c)]|//b/f[contains(b|c)]'),
    ('//a[contains(b|c|d)]', '//f|//avg/span', '//a[contains(b|c|d)]//f|//a[contains(b|c|d)]//avg/span'),
    ('//a', '//f[contains(b|c|d)]|//avg/span[contains(b|c|d)]', '//a//f[contains(b|c|d)]|//a//avg/span[contains(b|c|d)]'),
    ('//a[contains(b|c|d)]|//avg/span[contains(b|c|d)]', '//f', '//a[contains(b|c|d)]//f|//avg/span[contains(b|c|d)]//f'),
    ('//a[contains(b|c|d)]|//span/b[contains(blob|blob)]', '//a/f[contains(b|c)]|//b/f[contains(b|c)]', '//a[contains(b|c|d)]//a/f[contains(b|c)]|//span/b[contains(blob|blob)]//a/f[contains(b|c)]|//a[contains(b|c|d)]//b/f[contains(b|c)]|//span/b[contains(blob|blob)]//b/f[contains(b|c)]')
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

    def test_add_two_xpath_with_contains(self):
        for xpath_1, xpath_2, expected_result in param_list_add_two_xpath_with_contains:
            with self.subTest():
                set_result = set(TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together().split('|'))
                set_expected_result = set(expected_result.split('|'))
                assert set_result == set_expected_result, \
                    'Addition of {} and {} is "{}" different than expected "{}"'.format(
                        xpath_1, xpath_2, TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together(), expected_result)
