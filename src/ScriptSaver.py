
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings
import src.NameResolver as NameResolver

class ScriptSaver:
    
    def __init__(self):
        self.__filename = NameResolver.NameResolver.GetTmpfilePlt()

    def Save(self,script):
        scriptFile = open(self.__filename, "w")
        scriptFile.write(script)
        scriptFile.close()
