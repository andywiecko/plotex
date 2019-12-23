
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
from src.NameResolver import NameResolver
from src.Info import Info

class GnuplotRunner:
    def __init__(self):
        self.gnuplotCMD = 'gnuplot'
        self.filename = NameResolver.GetTmpfilePlt()
        self.__CMD = ' '.join([self.gnuplotCMD,self.filename])
        Info.Verbose("Gnuplot Runner initialization")

    def Run(self):
        return os.system(self.__CMD)

