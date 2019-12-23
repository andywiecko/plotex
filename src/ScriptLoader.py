
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings
from src.NameResolver import NameResolver
from src.Exiter import Exiter

class ScriptLoader:

    def Load(self):
        try:
            scriptFile = open(self.__filename,'r')
            self.__script = scriptFile.read()
            scriptFile.close()
            return 0
        except IOError:
            print("Error: File {filename} does not exist or there is no access avaliable!".format(filename=self.__filename))
            Exiter.Exit()
            return 1

    def __init__(self,filename):
        self.__filename =  NameResolver.GetLocalScript(filename)
        self.__script = ''

    def GetScript(self):
        return self.__script


