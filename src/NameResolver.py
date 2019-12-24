
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings

class NameResolver:
   
    @staticmethod
    def GetTmpfile():
        ret = NameResolver.GetOutput()
        ret += Settings.tmpfile
        return ret

    @staticmethod
    def GetOutputWithoutPID():
        ret = Settings.plotexPath + '/'
        ret += Settings.output + '/'
        return ret

    @staticmethod
    def GetOutput():
        ret = NameResolver.GetOutputWithoutPID()
        ret += Settings.PID + '/'
        return ret

    @staticmethod
    def GetTmpfileTex():
        return NameResolver.GetTmpfile() + '.tex'

    @staticmethod
    def GetTmpfilePlt():
        return NameResolver.GetTmpfile() + '.plt'

    @staticmethod
    def GetTmpfilePdf():
        return NameResolver.GetTmpfile() + '.pdf'

    @staticmethod
    def GetLocalPath():
        return Settings.localPath + '/'

    @staticmethod
    def GetLocalScript(filename):
        return NameResolver.GetLocalPath() + filename

    @staticmethod
    def GetProfilePath():
        return Settings.plotexPath + '/profiles/'

    @staticmethod
    def ReplaceWithPdf(filename):
        ret = filename.split('.')
        ret = ret[:-1] if len(ret)>1 else ret
        ret = ''.join(ret)
        return ret + '.pdf'


