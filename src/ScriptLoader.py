
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings

class ScriptLoader:

    def Load(self):
        scriptFile = open(self.__filename,'r')
        self.__script = scriptFile.read()
        scriptFile.close()

    def __init__(self,filename):
        self.__filename = Settings.localPath+'/'+ filename
        self.__script = ''
        self.Load()

    def GetScript(self):
        return self.__script


