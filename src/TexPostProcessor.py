
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.NameResolver import NameResolver
from src.Exiter import Exiter
from src.Info import Info
from src.ScriptSaver import ScriptSaver

class TexPostProcessor:
    def __init__(self):
        self.__filename = NameResolver.GetTmpfileTex()
        self.__tex = ''
        Info.Verbose("TeX Post-processor initialization")

    
    def __Load(self):
        try:  
            texFile = open(self.__filename,'r')
            self.__tex = texFile.readlines()
            texFile.close()
            return 0
        except IOError:
            Exiter.Exit("File {filename} does not exist or there is no access avaliable!".format(filename=self.__filename))
            return 1

    def PostProcess(self,append):
        try:
            Info.Verbose("TeX loading...")
            self.__Load()
            Info.Verbose("TeX loading completed!")
   
            Info.Verbose("TeX post-processing...")
            beginDoc = '\\begin{document}\n'
            if beginDoc in self.__tex:
                indexBegin = self.__tex.index(beginDoc)
                self.__tex.insert(indexBegin+1,append+'\n')
                self.__tex =''.join(self.__tex)
            Info.Verbose("TeX post-processing completed!")

            Info.Verbose("TeX saving...")
            self.__Save()
            Info.Verbose("TeX saving completed!")

            return 0
        except:
            return 1


    def __Save(self):
        scriptSaver = ScriptSaver('tex')
        scriptSaver.Save(self.__tex)
