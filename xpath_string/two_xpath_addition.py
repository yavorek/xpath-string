import copy
import itertools
import re

from xpath_string._operation_key import _OperationKey


class TwoXpathAddition(_OperationKey):
    def __init__(self, xpath_1: str, xpath_2: str):
        super(TwoXpathAddition, self).__init__(xpath_1, xpath_2)

    def add_two_xpath_together(self):
        """
        Add two Xpath obj together
        :return:
        """
        if self.operation_key == '00':
            return self.xpath_1 + self.xpath_2
        elif self.operation_key == '10':
            return self.add_to_xpath_with_or_operator()
        elif self.operation_key == '01':
            return self.add_xpath_with_or_operator()
        else:
            return self.add_together_xpath_with_or_operator()

    def add_to_xpath_with_or_operator(self):
        """
        Add to Xpath obj with .xpath attr containing OR operator another Xpath obj with .xpath attr without OR operator.
        :return:
        """
        split_xpath_1 = self._split_xpath_1()
        joined_xpath = '|'.join([part_of_xpath + self.xpath_2 for part_of_xpath in split_xpath_1])
        full_xpath = copy.deepcopy(joined_xpath)
        for content in self.xpath_1_square_brackets_inside:
            full_xpath = re.sub('CLEARED_1', '{}'.format(content), full_xpath, 1)
        return full_xpath

    def add_xpath_with_or_operator(self):
        """
        Add to Xpath obj without .xpath attr containing OR operator another Xpath with .xpath attr with OR operator.
        :return:
        """
        split_xpath_2 = self._split_xpath_2()
        joined_xpath = '|'.join([self.xpath_1 + part_of_xpath for part_of_xpath in split_xpath_2])
        full_xpath = copy.deepcopy(joined_xpath)
        for content in self.xpath_2_square_brackets_inside:
            full_xpath = re.sub('CLEARED_2', '{}'.format(content), full_xpath, 1)
        return full_xpath

    def add_together_xpath_with_or_operator(self):
        """
        Add together two Xpath objects with .xpath attr which contain OR operator.
        :return:
        """
        split_xpath_1 = copy.deepcopy(self._split_xpath_1())
        split_xpath_2 = copy.deepcopy(self._split_xpath_2())
        for content in self.xpath_1_square_brackets_inside:
            split_xpath_1 = re.sub('CLEARED_1', '{}'.format(content), ';!;'.join(split_xpath_1), 1).split(
                ';!;')
        for content in self.xpath_2_square_brackets_inside:
            split_xpath_2 = re.sub('CLEARED_2', '{}'.format(content), ';!;'.join(split_xpath_2), 1).split(
                ';!;')
        split_xpath_product = [''.join(element) for element in itertools.product(split_xpath_1, split_xpath_2)]
        full_xpath = '|'.join(split_xpath_product)
        return full_xpath

    def _split_xpath_1(self):
        self.xpath_1_square_brackets_inside = [find[0] for find in re.findall(
            self._or_operator_in_square_brackets_part_regex, self.xpath_1)]
        xpath_1_without_square_brackets = re.sub(
            self._or_operator_in_square_brackets_part_regex, 'CLEARED_1', self.xpath_1)
        split_xpath = xpath_1_without_square_brackets.split('|')
        return split_xpath

    def _split_xpath_2(self):
        self.xpath_2_square_brackets_inside = [find[0] for find in re.findall(
            self._or_operator_in_square_brackets_part_regex, self.xpath_2)]
        xpath_2_without_square_brackets = re.sub(
            self._or_operator_in_square_brackets_part_regex, 'CLEARED_2', self.xpath_2)
        split_xpath = xpath_2_without_square_brackets.split('|')
        return split_xpath
