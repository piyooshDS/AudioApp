import re


class PhonenumberformatforIndia(object):
    """docstring for LastNameValidation"""

    def __init__(self,number):
        super(PhonenumberformatforIndia, self).__init__()
        self.__pattern = '((\+*)((0[ -]+)*|(91 )*)(\d{12}+|\d{10}+)|\d{5}([- ]*)\d{6})'
        self.__name = number
 
    def validation(self):
        if re.match(str(self.__pattern), self.__name):
            return True
        return False