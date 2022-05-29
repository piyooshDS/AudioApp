


import re


class AlphaCheckValidation(object):
    """docstring for AlphaCheckValidation"""

    def __init__(self, number):
        super(AlphaCheckValidation, self).__init__()
        self.__number = number

    def validation(self):
        if str.isalpha(self.__number):
            return True
        return False



