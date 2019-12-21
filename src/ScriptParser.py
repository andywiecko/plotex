import src.PlotexSettings as Settings
import src.ScriptLoader as ScriptLoader
import src.ProfileLoader as ProfileLoader
import src.ScriptSaver as ScriptSaver

class ScriptParser:
    def __init__(self,args):
        
        self.__args = args

        self.__header = r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} standalone {terminalOptions} header {header}
set output '{tmpfile}.tex' 
"""
        self.__settings = "# gnuplot script settings loaded from profile\n{settings}"
        self.__body = "# gnuplot script loaded by plotex"
        self.Parse()

    def __Header(self,terminalSettings):
        self.__header = \
                self.__header.format(
                shebang = Settings.shebang,
                tmpfile = Settings.tmpfile,
                terminal = terminalSettings['terminal'],
                terminalOptions = terminalSettings['terminalOptions'],
                header = terminalSettings['header'])

    def __Settings(self,plotSettings):
        self.__settings = self.__settings.format(settings="\n".join(plotSettings)) + "\n"

    def __Body(self,script):
        self.__body +=  script

    def __LoadScript(self,filename):
        scriptLoader = ScriptLoader.ScriptLoader(filename)
        return scriptLoader.GetScript()
   
    def __LoadProfile(self,profileName):
        profileLoader = ProfileLoader.ProfileLoader(profileName)
        return profileLoader.Load() 

    def __Glue(self):
        return "\n".join(
                [self.__header,
                self.__settings,
                self.__body])

    def Parse(self):
        script = self.__LoadScript(self.__args.filename)
        profile = self.__LoadProfile(self.__args.profile)
               
        terminalSettings = profile.GetTerminalSettings()
        plotSettings = profile.GetPlotSettings()
  
        self.__Header(terminalSettings)
        self.__Settings(plotSettings)    
        self.__Body(script) 
       
        scriptSaver = ScriptSaver.ScriptSaver()
        scriptSaver.Save(self.__Glue())


