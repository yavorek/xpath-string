from xpath_string.two_xpath_addition import TwoXpathAddition


class Xpath:
    def __init__(self, xpath_string: str):
        self.xpath = xpath_string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return TwoXpathAddition(self.xpath, other.xpath).add_two_xpath_together()
        elif isinstance(other, str):
            return self.xpath + other
        else:
            raise TypeError('Only Xpath and string can be added to Xpath Object. Not {}'.format(type(other)))

