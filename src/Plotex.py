
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.Argv import Argv
from src.ScriptParser import ScriptParser
from src.GnuplotRunner import GnuplotRunner
from src.LatexRunner import LatexRunner
from src.Pdfcopier import Pdfcopier

class Plotex:

    def __init__(self):
        self.__argv = Argv()
        self.__args = self.__argv.GetArgs()
        
    def Run(self):
        # generating script -> .plt
        ScriptParser(self.__args)
        
        # .plt -> .tex
        gnuplotRunner = GnuplotRunner()
        gnuplotRunner.Run()

        # .tex -> .pdf
        if not self.__args.ignore:
            latexRunner = LatexRunner()
            latexRunner.Run()

            pdfcopier = Pdfcopier(self.__args)
            pdfcopier.Copy()

