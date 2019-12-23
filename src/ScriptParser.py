
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.ScriptLoader import ScriptLoader
from src.ProfileLoader import ProfileLoader
from src.ScriptGlue import ScriptGlue
from src.ScriptSaver import ScriptSaver

class ScriptParser:
    def __init__(self,args):
        self.__args = args
        self.__Parse()

    def __LoadScript(self,filename):
        scriptLoader = ScriptLoader(filename)
        scriptLoader.Load()
        return scriptLoader.GetScript()
   
    def __LoadProfile(self,profileName):
        profileLoader = ProfileLoader(profileName)
        return profileLoader.Load(self.__args) 

    def __SaveScript(self,glued):
        scriptSaver = ScriptSaver()
        scriptSaver.Save(glued)

    def __Parse(self):
        profile = self.__LoadProfile(self.__args.profile)
        if self.__args.display:
            print(profile)

        terminalSettings = profile.GetTerminalSettings()
        plotSettings = profile.GetPlotSettings()
        script = self.__LoadScript(self.__args.filename)
 
        scriptGlue = ScriptGlue(terminalSettings,plotSettings,script,self.__args)
        glued = scriptGlue.GetGlue()
        self.__SaveScript(glued)

