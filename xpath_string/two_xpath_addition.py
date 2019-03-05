from xpath_string._operation_key import _OperationKey


class TwoXpathAddition(_OperationKey):
    def __init__(self, xpath_1: str, xpath_2: str):
        super(TwoXpathAddition, self).__init__(xpath_1, xpath_2)

    def add_two_xpath_together(self):
        if self.operation_key == '00':
            return self.xpath_1 + self.xpath_2
        elif self.operation_key == '10':
            raise Exception('TO IMPLEMENT')
        elif self.operation_key == '01':
            raise Exception('TO IMPLEMENT')
        else:
            raise Exception('TO IMPLEMENT')

    def add_to_xpath_with_or_operator(self, xpath_with_or_operator: str, regular_xpath: str):
        split_xpath = self.__split_xpath(xpath_with_or_operator)
        return '|'.join([part_of_xpath + regular_xpath for part_of_xpath in split_xpath])

    def __split_xpath(self, xpath_with_or_operator: str):
        # add checking if contains with or operator is present; if it is then save it content to some list
        # self._or_operator_in_contains_part_regex
        return
