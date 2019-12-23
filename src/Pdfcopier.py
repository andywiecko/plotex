
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
import src.NameResolver as NameResolver

class Pdfcopier:
    def __init__(self,args):
       
        outputfile = NameResolver.NameResolver.GetTmpfilePdf()
        filename = NameResolver.NameResolver.GetLocalScript(args.filename)
        filename = NameResolver.NameResolver.ReplaceWithPdf(filename)

        copyCMD = 'cp {outfile} {localfile}'
        copyCMD = copyCMD.format(
                outfile=outputfile,
                localfile=filename)
        os.system(copyCMD)
