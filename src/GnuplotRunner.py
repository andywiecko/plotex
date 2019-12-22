import os
import src.PlotexSettings as Settings

class GnuplotRunner:
    def __init__(self):
        self.gnuplotCMD = 'gnuplot'
        os.system(self.gnuplotCMD+' '+Settings.plotexPath + '/' + Settings.output+'/'+Settings.tmpfile+'.plt')
