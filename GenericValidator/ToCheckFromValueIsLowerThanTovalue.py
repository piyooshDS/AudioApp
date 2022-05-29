import re


class  ToCheckFromValueIsLowervalidation(object):
    """ ToCheckFromValueIsLowerThanTovalue"""

    def __init__(self, number1,number2):
        super( ToCheckFromValueIsLowervalidation, self).__init__()
        self.__number1 =number1
        self.__number2 = number2

    def validation(self):
        if (self.__number1< self.__number2):
        	return True
        return False