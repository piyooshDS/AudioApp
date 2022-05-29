import re


class RangeValidation(object):
    """docstring for RangeValidation"""

    def __init__(self, minVal, maxVal, value):
        super(RangeValidation, self).__init__()
        self.__minVal = minVal
        self.__maxVal = maxVal
        self.__value = value

    def validation(self):
        if self.__minVal <= self.__value <= self.__maxVal:
            return True
        return False
