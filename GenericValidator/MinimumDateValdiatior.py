import time


class MinimumDateValdiation(object):
    """docstring for MaximumDateValdiation"""

    def __init__(self,date1,date2):
        super(MinimumDateValdiation, self).__init__()
        self.__date1 = time.strptime(date1, "%d/%m/%Y")
        self.__date2 = time.strptime(date2, "%d/%m/%Y")

    def validation(self):
        if (self.__date1<self.__date2):
        	return True
        return False
