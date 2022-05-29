import re


class MobileValidation(object):
    """docstring for MobileValidation"""

    def __init__(self, mobile,minl,maxl):
        super(MobileValidation, self).__init__()
        self.__mobile = mobile
        self.__min=minl
        self.__max=maxl


    def validation(self):
        if re.match("\\d{10}", self.__mobile):
            return True
        elif re.match("\\d{3}[-\\.\\s]\\d{3}[-\\.\\s]\\d{4}", self.__mobile):
            return True;
        elif re.match("\\d{3}-\\d{3}-\\d{4}\\s(x|(ext))\\d{3,5}", self.__mobile):
            return True;
        elif re.match("\\(\\d{3}\\)-\\d{3}-\\d{4}", self.__mobile):
            return True;
        return False;


    def max_validation(self):
        if (len(str(self.__mobile))<self.__max):
            return True
        return False


    def min_validation(self):
        if (len(str(self.__mobile))>self.__min):
            return True
        return False


    def left_trim_validation(self):
        if self.__mobile[0]!=' ':
            return True
        return False
        

    def req_validation(self):
        if (len(str(self.__mobile)))>1:
            return True
        return False



