
import src.ScriptHeader as ScriptHeader
import src.ScriptSettingsSection as ScriptSettingsSection
import src.ScriptBody as ScriptBody
class ScriptGlue:
    def __init__(self,terminalSettings,plotSettings,script):

        scriptHeader = ScriptHeader.ScriptHeader(terminalSettings)
        self.__header = scriptHeader.GetHeader()

        scriptSettingsSection = ScriptSettingsSection.ScriptSettingsSection(plotSettings)
        self.__settings = scriptSettingsSection.GetSettings()
    
        scriptBody = ScriptBody.ScriptBody(script)
        self.__body = scriptBody.GetBody() 
       
        
    def GetGlue(self):
        return "\n".join(
                [self.__header,
                self.__settings,
                self.__body])

