import src.PlotexSettings as Settings

class ScriptSaver:
    __filename = Settings.tmpfile+'.plt'

    def Save(self,script):
        scriptFile = open(self.__filename, "w")
        scriptFile.write(script)
        scriptFile.close()
