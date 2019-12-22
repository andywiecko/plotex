__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.Argv as Argv
import src.ScriptParser as ScriptParser
import src.GnuplotRunner as GnuplotRunner
import src.LatexRunner as LatexRunner
import src.Pdfcopier as Pdfcopier

class Plotex:

    def __init__(self):
        argv = Argv.Argv()
        args = argv.GetArgs()
    
        # generating script -> .plt
        ScriptParser.ScriptParser(args)
        
        # .plt -> .tex
        GnuplotRunner.GnuplotRunner()

        # .tex -> .pdf
        if not args.ignore:
            LatexRunner.LatexRunner()
            Pdfcopier.Pdfcopier(args)

