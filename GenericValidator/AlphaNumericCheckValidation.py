import re


class AlphaNumericCheckValidation(object):
    """docstring for AlphaNumericCheckValidation"""

    def __init__(self, number):
        super(AlphaNumericCheckValidation, self).__init__()
        self.__number = number

    def validation(self):
        if str.isalnum(self.__number):
            return True
        return False