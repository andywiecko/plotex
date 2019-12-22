
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.ScriptHeader as ScriptHeader
import src.ScriptSettingsSection as ScriptSettingsSection
import src.ScriptBody as ScriptBody
class ScriptGlue:
    def __init__(self,terminalSettings,plotSettings,script,args):

        scriptHeader = ScriptHeader.ScriptHeader(terminalSettings)
        self.__header = scriptHeader.GetHeader(args)

        scriptSettingsSection = ScriptSettingsSection.ScriptSettingsSection(plotSettings)
        self.__settings = scriptSettingsSection.GetSettings()
    
        scriptBody = ScriptBody.ScriptBody(script)
        self.__body = scriptBody.GetBody() 
       
        
    def GetGlue(self):
        return "\n".join(
                [self.__header,
                self.__settings,
                self.__body])

