
class Profile:
    def __init__(self,terminalSettings,plotSettings):
        self.__terminalSettings = terminalSettings
        self.__plotSettings = plotSettings
       
    def GetTerminalSettings(self):
        return self.__terminalSettings

    def GetPlotSettings(self):
        return self.__plotSettings

    def __str__(self):
        ret = ''
        for key, value in self.GetTerminalSettings().items():
            ret += str(key) + ' : ' + str(value) + '\n'
        ret += 'plotSettings : '+str(self.GetPlotSettings())
        return ret

