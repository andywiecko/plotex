
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

class ScriptSettingsSection:
    def __init__(self,plotSettings):

        self.__settings = "# gnuplot script settings loaded from profile\n{settings}"
        self.__Settings(plotSettings)    

    def __Settings(self,plotSettings):
        self.__settings = self.__settings.format(settings="\n".join(plotSettings)) + "\n"

    def GetSettings(self):
        return self.__settings
