from typing import Any

from xpath_string.two_xpath_addition import TwoXpathAddition


class Xpath(str):
    def __init__(self, xpath_string: str):
        super(Xpath, self).__init__()
        self.xpath = xpath_string

    def __add__(self, other):
        """ Override the default Addition behavior"""
        if isinstance(other, self.__class__):
            return TwoXpathAddition(self.xpath, other.xpath).add_two_xpath_together()
        elif isinstance(other, str):
            return self.xpath + other
        else:
            raise TypeError('Only Xpath and string can be added to Xpath Object. Not {}'.format(type(other)))

    def __str__(self):
        """ Override the default str() behavior"""
        return self.xpath

    def __eq__(self, other):
        """ Override the default Equals behavior"""
        return self.xpath == other.xpath

    def __ne__(self, other):
        """ Override the default Unequals behavior"""
        return self.xpath != other.xpath

    def format(self, *args: Any, **kwargs: Any):
        """
        Returns Xpath obj with formatted version of it's .xpath attribute.
        :param args:
        :param kwargs:
        :return:
        """
        return Xpath(self.xpath.format(*args, **kwargs))
