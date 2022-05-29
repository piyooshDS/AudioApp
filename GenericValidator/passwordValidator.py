import re


class PasswordValidation(object):
    """docstring for PasswordValidation"""

    def __init__(self, password,minl,maxl):
        super(PasswordValidation, self).__init__()
        self.__pattern = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\\S+$).{8,}$"
        self.__password = password
        self.__min=minl
        self.__max=maxl


    def validation(self):
        if re.match(self.__pattern, self.__password):
            return True
        return False

    def max_validation(self):
    	if (len(str(self.__password))<self.__max):
    		return True
    	return False


    def min_validation(self):
    	if (len(str(self.__password))>self.__min):
    		return True
    	return False


    def req_validation(self):
    	if (len(str(self.__password)))>1:
    		return True
    	return False


    def alpha_numeric(self):
        if str.isalnum(self.__password):
            return True
        return False

    def alpha_validation(self):
        if str.isalpha(self.__password):
            return True
        return False

    def left_trim_validation(self):
        if self.__password[0]!=' ':
            return True
        return False
