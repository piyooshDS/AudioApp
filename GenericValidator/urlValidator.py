import re, validators


class URLValidation(object):
    """docstring for URLValidation"""

    def __init__(self, url):
        super(URLValidation, self).__init__()
        self.__url = url

    def validation(self):
        if validators.url(self.__url):
            return True
        return False
