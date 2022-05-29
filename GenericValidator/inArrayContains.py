import re


class InArrayContainsValidation(object):
    """docstring for InArrayContainsValidation"""

    def __init__(self, array, value):
        super(InArrayContainsValidation, self).__init__()
        self.__array = array
        self.__value = value

    def validation(self):
        if self.__value in self.__array:
            return True
        return False
