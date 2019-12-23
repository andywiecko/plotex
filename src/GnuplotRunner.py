
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
import src.NameResolver as NameResolver

class GnuplotRunner:
    def __init__(self):
        self.gnuplotCMD = 'gnuplot'
        self.filename = NameResolver.NameResolver.GetTmpfilePlt()
        CMD = ' '.join([self.gnuplotCMD,self.filename])
        os.system(CMD)
