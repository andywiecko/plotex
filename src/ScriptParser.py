import src.ScriptLoader as ScriptLoader
import src.ProfileLoader as ProfileLoader
import src.ScriptGlue as ScriptGlue
import src.ScriptSaver as ScriptSaver

class ScriptParser:
    def __init__(self,args):
        self.__args = args
        self.__Parse()

    def __LoadScript(self,filename):
        scriptLoader = ScriptLoader.ScriptLoader(filename)
        return scriptLoader.GetScript()
   
    def __LoadProfile(self,profileName):
        profileLoader = ProfileLoader.ProfileLoader(profileName)
        return profileLoader.Load(self.__args) 

    def __SaveScript(self,glued):
        scriptSaver = ScriptSaver.ScriptSaver()
        scriptSaver.Save(glued)

    def __Parse(self):
        profile = self.__LoadProfile(self.__args.profile)
        if self.__args.display:
            print(profile)

        terminalSettings = profile.GetTerminalSettings()
        plotSettings = profile.GetPlotSettings()
        script = self.__LoadScript(self.__args.filename)
 
        scriptGlue = ScriptGlue.ScriptGlue(terminalSettings,plotSettings,script,self.__args)
        glued = scriptGlue.GetGlue()
        self.__SaveScript(glued)

