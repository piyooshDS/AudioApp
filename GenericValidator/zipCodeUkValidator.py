import re


class ZipCodeUkValidation(object):
    """docstring for ZipCodeUkValidation"""

    def __init__(self, zipCodeUk):
        super(ZipCodeUkValidation, self).__init__()
        self.__pattern = "\\b[A-Z0-9]+\\b"
        self.__zipCodeUk = zipCodeUk

    def validation(self):
        if re.match(self.__pattern, self.__zipCodeUk):
            return True
        return False
