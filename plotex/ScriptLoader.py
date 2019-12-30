
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import plotex.PlotexSettings as Settings
from plotex.NameResolver import NameResolver
from plotex.Exiter import Exiter

class ScriptLoader:

    def Load(self):
        try:
            scriptFile = open(self.__filename,'r')
            self.__script = scriptFile.read()
            scriptFile.close()
            return 0
        except IOError:
            Exiter.Exit("File {filename} does not exist or there is no access avaliable!".format(filename=self.__filename))
            return 1

    def __init__(self,filename):
        self.__filename =  NameResolver.GetLocalScript(filename)
        self.__script = ''

    def GetScript(self):
        return self.__script


