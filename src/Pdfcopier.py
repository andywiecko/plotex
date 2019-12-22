
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings

class Pdfcopier:
    def __init__(self,args):
       
        outputPath = Settings.plotexPath + '/' + Settings.output + '/' + Settings.tmpfile + '.pdf'
        localPath = Settings.localPath

        localfile = args.filename.split('.')
        if len(localfile)>1:
            localfile = localfile[:-1]
    
        localfile = ''.join(localfile)

        filename = localPath + '/' + localfile + '.pdf'

        copyCMD = 'cp {outfile} {localfile}'
        copyCMD = copyCMD.format(outfile=outputPath,localfile=filename)
        os.system(copyCMD)
