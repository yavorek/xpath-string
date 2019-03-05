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
