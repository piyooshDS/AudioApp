import re


class ZipCodeValidation(object):
    """docstring for ZipCodeValidation"""

    def __init__(self, zipCode):
        super(ZipCodeValidation, self).__init__()
        self.__pattern = "\\d{5,10}"
        self.__zipCode = zipCode

    def validation(self):
        if re.match(self.__pattern, self.__zipCode):
            return True
        return False
