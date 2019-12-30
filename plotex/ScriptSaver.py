
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import plotex.PlotexSettings as Settings
from plotex.NameResolver import NameResolver
from plotex.Exiter import Exiter

class ScriptSaver:
    
    def __init__(self,ext='plt'):
        if ext=='plt':
            self.__filename = NameResolver.GetTmpfilePlt()
        if ext=='tex':
            self.__filename = NameResolver.GetTmpfileTex()

    def Save(self,script):
        try: 
            scriptFile = open(self.__filename, "w")
            scriptFile.write(script)
            scriptFile.close()
            return 0
        except IOError:
            print("Error: {filename} cannot be accessed!".format(filename=self.__filename))
            Exiter.Exit()
            return 1
