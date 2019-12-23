
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

import sys
import os
from src.NameResolver import NameResolver

class Plotex:

    def __init__(self):
        self.__argv = Argv()
        self.__args = self.__argv.GetArgs()
       
    @staticmethod
    def Info():
        print("This is ploTeX, Version",__version__,'(beta)')
        print(40*"=")

    def Run(self):
        
        Plotex.Info() 
        
        # generating script -> .plt
        ScriptParser(self.__args)
        
        # .plt -> .tex
        gnuplotRunner = GnuplotRunner()
        if gnuplotRunner.Run():
            Exiter.Exit()

        # .tex post-processing

        # .tex -> .pdf
        if not self.__args.ignore:
            latexRunner = LatexRunner()
            if latexRunner.Run():
                Exiter.Exit()

            pdfcopier = Pdfcopier(self.__args)
            if pdfcopier.Copy():
                Exiter.Exit()

        Exiter.Clean()
        return 0
