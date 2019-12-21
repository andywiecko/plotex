
class Profile:
    def __init__(self,terminalSettings,plotSettings):
        self.__terminalSettings = terminalSettings
        self.__plotSettings = plotSettings
       
    def GetTerminalSettings(self):
        return self.__terminalSettings

    def GetPlotSettings(self):
        return self.__plotSettings
