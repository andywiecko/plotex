
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings

class ScriptSaver:
    __filename = Settings.tmpfile+'.plt'

    def Save(self,script):
        scriptFile = open(Settings.plotexPath +'/'+ Settings.output+'/'+self.__filename, "w")
        scriptFile.write(script)
        scriptFile.close()
