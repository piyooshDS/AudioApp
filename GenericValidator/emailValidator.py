import re


class EmailValidation(object):
    """docstring for EmailValidation"""

    def __init__(self, email,minl,maxl):
        super(EmailValidation, self).__init__()
        self.__pattern = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
        self.__email = email
        self.__min=minl
        self.__max=maxl

    def validation(self):
        if re.match(self.__pattern, self.__email):
            return True
        return False


    def max_validation(self):
    	if (len(str(self.__email))<self.__max):
    		return True
    	return False


    def min_validation(self):
    	if (len(str(self.__email))>self.__min):
    		return True
    	return False


    def req_validation(self):
    	if (len(str(self.__email)))>1:
    		return True
    	return False

    # def not_empty(self):
    #     if (len(str(self.__email)))>1:
    #         return True
    #     return False


    def alpha_numeric(self):
        if not self.__email.isalnum():
            return True
        return False

    def alpha_validation(self):
        if not str.isalpha(self.__email):
            return True
        return False

    def left_trim_validation(self):
        if self.__email[0]!=' ':
            return True
        return False


