
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import plotex.PlotexSettings as Settings
from plotex.NameResolver import NameResolver
from plotex.Info import Info

class Pdfcopier:
    def __init__(self,args):
       
        self.outputfile = NameResolver.GetTmpfilePdf()
        filename = NameResolver.GetLocalScript(args.filename)
        self.filename = NameResolver.ReplaceWithPdf(filename)

        self.__CMD = 'cp {outfile} {localfile}'
        self.__CMD = self.__CMD.format(
                outfile=self.outputfile,
                localfile=self.filename)

        Info.Verbose("Pdfcopier initialization")

    def Copy(self):
        return os.system(self.__CMD)
