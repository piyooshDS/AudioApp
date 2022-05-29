import re


class  CheckForOddNumbervalidation(object):
    """docstring for CheckForEvenNumber"""

    def __init__(self, number):
        super( CheckForOddNumbervalidation, self).__init__()
        self.__number = number

    def validation(self):
        if (self.__number)%2!=0:
        	return True
        return False