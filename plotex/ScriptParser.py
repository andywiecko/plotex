
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from plotex.Info import Info
from plotex.ScriptLoader import ScriptLoader
from plotex.ProfileLoader import ProfileLoader
from plotex.ScriptGlue import ScriptGlue
from plotex.ScriptSaver import ScriptSaver
from plotex import profiles
import yaml


class ScriptParser:
    def __init__(self,args):
        self.__args = args
        Info.Verbose("Script Parser initialization")
        self.__Parse()

    def __LoadScript(self,filename):
        scriptLoader = ScriptLoader(filename)
        Info.Verbose("Local script `{}` loading...".format(filename))
        if not scriptLoader.Load():
            Info.Verbose("Local script `{}` loading completed!".format(filename))
        return scriptLoader.GetScript()
   
    def __LoadProfile(self,profileName):
        profileLoader = ProfileLoader(profileName)
        return profileLoader.Load(self.__args) 

    def __SaveScript(self,glued):
        scriptSaver = ScriptSaver()
        Info.Verbose("Parsed script saving...")
        if not scriptSaver.Save(glued):
            Info.Verbose("Parsed script saving completed")

    def __Parse(self):
        profile = profiles.load_profile(self.__args.profile, self.__args)
        if self.__args.display:
            print(yaml.dumps(profile))

        terminalSettings = profile["terminalSettings"]
        plotSettings = profile["plotSettings"]
        script = self.__LoadScript(self.__args.filename)
        
        scriptGlue = ScriptGlue(terminalSettings,plotSettings,script,self.__args)
        Info.Verbose("Glueing...")
        glued = scriptGlue.GetGlue()
        Info.Verbose("Glueing completed!")
        self.__SaveScript(glued)

