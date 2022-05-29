


class  ConfirmPasswordValidaton(object):
    """ ConfirmPasswordValidator"""

    def __init__(self,password,confirm_password,minl,maxl):
        super(ConfirmPasswordValidaton, self).__init__()
        self.__password = password
        self.__confirm_password=confirm_password
        self.__min=minl
        self.__max=maxl

    def validation(self):
        if (self.__password==self.__confirm_password):
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


class AddressValidation(object):

	def __init__(self,Address,minl,maxl):
		super(AddressValidation, self).__init__()
		self.__Address = Address

	def req_validation(self):
		if (len(str(self.__Address)))>1:
			return True
		return False

	def notempty_validation(self):
		if (len(str(self.__Address)))>1:
			return True
		return False

