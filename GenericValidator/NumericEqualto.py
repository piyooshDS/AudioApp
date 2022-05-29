

class NumericEqualValidation(object):
    """docstring for NumericLesserThanEqualtoValidation"""

    def __init__(self, minVal, maxVal):
        super(NumericEqualValidation, self).__init__()
        self.__minVal = minVal
        self.__maxVal = maxVal

    def validation(self):
        if self.__maxVal==self.__minVal:
            return True
        return False
