from xpath_string.two_xpath_addition import TwoXpathAddition


class Xpath(str):
    def __init__(self, xpath_string: str):
        super(Xpath, self).__init__()
        self.xpath = xpath_string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return TwoXpathAddition(self.xpath, other.xpath).add_two_xpath_together()
        elif isinstance(other, str):
            return self.xpath + other
        else:
            raise TypeError('Only Xpath and string can be added to Xpath Object. Not {}'.format(type(other)))

    def __str__(self):
        return self.xpath

    def format(self, *args, **kwargs):
        self.xpath = super(Xpath, self).format(*args, **kwargs)
        return self
