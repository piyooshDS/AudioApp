import re


class NumberValidation(object):
    """docstring for NumberValidation"""

    def __init__(self, number):
        super(NumberValidation, self).__init__()
        self.__number = number

    def validation(self):
        if str.isnumeric(self.__number):
            return True
        return False
