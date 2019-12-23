
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
from src.Exiter import Exiter
from src.Info import Info

import sys
import os
from src.NameResolver import NameResolver

class Plotex:

    def __init__(self):
        self.__argv = Argv()
        self.__args = self.__argv.GetArgs()
        if self.__args.verbose:
            Info.SetVerbose()

    def Run(self):
        
        Info.Info() 
        
        # generating script -> .plt
        ScriptParser(self.__args)
        Info.Verbose("Exiting Script Parser")

        # .plt -> .tex
        gnuplotRunner = GnuplotRunner()
        if gnuplotRunner.Run():
            Exiter.Exit("gnuplot does not exit successfully!")
        Info.Verbose("Exiting Gnuplot Runner")

        # .tex post-processing

        # .tex -> .pdf
        if not self.__args.ignore:
            latexRunner = LatexRunner()
            if latexRunner.Run():
                Exiter.Exit("LaTeX does not exit successfully!")
            Info.Verbose("Exiting LaTeX Runner")

            pdfcopier = Pdfcopier(self.__args)
            if pdfcopier.Copy():
                Exiter.Exit("copying does not finished successfully!")
            Info.Verbose("Exiting Pdfcopier")

        Exiter.Clean()
        return 0
