
class ScriptBody:
    def __init__(self,script):

        self.__body = "# gnuplot script loaded by plotex"
        self.__Body(script)
        
    def __Body(self,script):
        self.__body +=  script

    def GetBody(self):
        return self.__body


