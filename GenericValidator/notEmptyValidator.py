import re


class NotEmptyValidation(object):
    """docstring for NotEmptyValidation"""

    def __init__(self, value):
        super(NotEmptyValidation, self).__init__()
        self.__value = value

    def validation(self):
        if self.__value:
            return True
        return False
