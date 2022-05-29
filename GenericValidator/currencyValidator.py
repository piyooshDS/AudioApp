import re


class CurrenyValidation(object):
    """docstring for CurrenyValidation"""

    def __init__(self, currency):
        super(CurrenyValidation, self).__init__()
        self.__pattern = "(?:[A-Z]{3})(?:\d+(?:[.,]?\d*)*)"
        self.__currency = currency

    def validation(self):
        if re.match(self.__pattern, self.__currency):
            return True
        return False
