


class  TwoDigitAfterDecimalvalidation(object):
    """docstring for  TwoDigitAfterDecimalvalidation"""

    def __init__(self,price):
        super(TwoDigitAfterDecimalvalidation, self).__init__()
        self.__price = price
        if not '.' in str(self.__price):
        	self.__y=0
        self.__y= len(str(self.__price)) - str(self.__price).index('.') - 1

    def validation(self):
        if self.__y == 2:
        	return True
        return False
