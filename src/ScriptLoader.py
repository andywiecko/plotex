import src.PlotexSettings as Settings

class ScriptLoader:

    def Load(self):
        scriptFile = open(self.__filename,'r')
        self.__script = scriptFile.read()
        scriptFile.close()

    def __init__(self,filename):
        self.__filename = Settings.localPath+'/'+ filename
        self.__script = ''
        self.Load()

    def GetScript(self):
        return self.__script


