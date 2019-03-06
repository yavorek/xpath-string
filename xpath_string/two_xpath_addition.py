import copy
import re

from xpath_string._operation_key import _OperationKey


class TwoXpathAddition(_OperationKey):
    def __init__(self, xpath_1: str, xpath_2: str):
        super(TwoXpathAddition, self).__init__(xpath_1, xpath_2)

    def add_two_xpath_together(self):
        if self.operation_key == '00':
            return self.xpath_1 + self.xpath_2
        elif self.operation_key == '10':
            return self.add_to_xpath_with_or_operator()
        elif self.operation_key == '01':
            return self.add_xpath_with_or_operator()
        else:
            raise Exception('TO IMPLEMENT')

    def add_to_xpath_with_or_operator(self):
        split_xpath_1 = self._split_xpath_1()
        joined_xpath = '|'.join([part_of_xpath + self.xpath_2 for part_of_xpath in split_xpath_1])
        full_xpath = copy.deepcopy(joined_xpath)
        for contains in self.xpath_1_contains_with_or_operator:
            full_xpath = re.sub('CLEARED', 'contains({})'.format(contains), full_xpath, 1)
        return full_xpath

    def add_xpath_with_or_operator(self):
        split_xpath_2 = self._split_xpath_2()
        joined_xpath = '|'.join([self.xpath_1 + part_of_xpath for part_of_xpath in split_xpath_2])
        full_xpath = copy.deepcopy(joined_xpath)
        for contains in self.xpath_2_contains_with_or_operator:
            full_xpath = re.sub('CLEARED', 'contains({})'.format(contains), full_xpath, 1)
        return full_xpath

    def _split_xpath_1(self):
        self.xpath_1_contains_with_or_operator = [find[0] for find in
                                                  re.findall(self._or_operator_in_contains_part_regex, self.xpath_1)]
        xpath_1_without_contains_with_or_operator = re.sub(self._or_operator_in_contains_part_regex, 'CLEARED',
                                                           self.xpath_1)
        split_xpath = xpath_1_without_contains_with_or_operator.split('|')
        return split_xpath

    def _split_xpath_2(self):
        self.xpath_2_contains_with_or_operator = [find[0] for find in
                                                  re.findall(self._or_operator_in_contains_part_regex, self.xpath_2)]
        xpath_2_without_contains_with_or_operator = re.sub(self._or_operator_in_contains_part_regex, 'CLEARED',
                                                           self.xpath_2)
        split_xpath = xpath_2_without_contains_with_or_operator.split('|')
        return split_xpath
