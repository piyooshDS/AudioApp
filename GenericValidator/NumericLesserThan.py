class NumericLesserThanValidation(object):
    """docstring for NumericLesserThanEqualtoValidation"""

    def __init__(self, minVal, maxVal):
        super(NumericLesserThanValidation, self).__init__()
        self.__minVal = minVal
        self.__maxVal = maxVal

    def validation(self):
        if self.__minVal <self.__maxVal:
            return True
        return False
