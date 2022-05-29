

class  ExactLengthValidaton(object):
    """docstring for AlphaCheckValidation"""

    def __init__(self, number,length):
        super(ExactLengthValidaton, self).__init__()
        self.__number = number
        self.__length=length


    def validation(self):
        if (len(str(self.__number))==self.__length):
            return True
        return False
