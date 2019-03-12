import re


class _OperationKey:
    _or_operator_in_square_brackets_part_regex = re.compile(r'(?P<content>\[((?!\]).)*\])')

    def __init__(self, xpath_1: str, xpath_2: str):
        self.xpath_1 = xpath_1
        self.xpath_2 = xpath_2

    @property
    def operation_key(self):
        """
        Return operation key:
        11 - '|' present in self.xpath_1 and self.xpath_2
        10 - '|' present in self.xpath_1 and not present in self.xpath_2
        01 - '|' not present in self.xpath_1 and present in self.xpath_2
        00 - '|' not present in self.xpath_1 and self.xpath_2
        :return:
        """
        first_part = '1' if self.__or_operator_present_in_main_part_xpath_1() else '0'
        second_part = '1' if self.__or_operator_present_in_main_part_xpath_2() else '0'
        return first_part + second_part

    def __or_operator_present_in_main_part_xpath_1(self):
        xpath_without_square_brackets_part = re.sub(self._or_operator_in_square_brackets_part_regex, '', self.xpath_1)
        return True if '|' in xpath_without_square_brackets_part else False

    def __or_operator_present_in_main_part_xpath_2(self):
        xpath_without_square_brackets_part = re.sub(self._or_operator_in_square_brackets_part_regex, '', self.xpath_2)
        return True if '|' in xpath_without_square_brackets_part else False
