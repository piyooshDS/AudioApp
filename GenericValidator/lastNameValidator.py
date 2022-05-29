import re


class LastNameValidation(object):
    """docstring for LastNameValidation"""

    def __init__(self, name,minl,maxl):
        super(LastNameValidation, self).__init__()
        self.__pattern = '[a-zA-Z]+'
        self.__name = name
        self.__min=minl
        self.__max=maxl

    def validation(self):
        if re.match(self.__pattern, self.__name):
            return True
        return False


    def alpha_numeric(self):
        if str.isalnum(self.__name):
            return True
        return False

    def alpha_validation(self):
        if str.isalpha(self.__name):
            return True
        return False

    def left_trim_validation(self):
        if self.__name[0]!=' ':
            return True
        return False


    def max_validation(self):
    	if (len(str(self.__name))<self.__max):
    		return True
    	return False


    def min_validation(self):
    	if (len(str(self.__name))>self.__min):
    		return True
    	return False


    def req_validation(self):
    	if (len(str(self.__name)))>1:
    		return True
    	return False
