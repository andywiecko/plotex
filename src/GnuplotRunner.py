
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings

class GnuplotRunner:
    def __init__(self):
        self.gnuplotCMD = 'gnuplot'
        os.system(self.gnuplotCMD+' '+Settings.plotexPath + '/' + Settings.output+'/'+Settings.tmpfile+'.plt')
