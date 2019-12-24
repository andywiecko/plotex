
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

class ScriptBody:
    def __init__(self,script):

        self.__body = "# gnuplot script loaded by plotex\n"
        self.__Body(script)
        
    def __Body(self,script):
        self.__body +=  script

    def GetBody(self):
        return self.__body


