class Xpath:
    def __init__(self, xpath_string: str):
        self.xpath = xpath_string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.xpath + other.xpath
        elif isinstance(other, str):
            return self.xpath + other
        else:
            raise TypeError('Only Xpath and string can be added to Xpath Object. Not {}'.format(type(other)))

