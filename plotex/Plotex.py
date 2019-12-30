
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from plotex.Argv import Argv
from plotex.ScriptParser import ScriptParser
from plotex.GnuplotRunner import GnuplotRunner
from plotex.TexPostProcessor import TexPostProcessor
from plotex.LatexRunner import LatexRunner
from plotex.Pdfcopier import Pdfcopier
from plotex.Exiter import Exiter
from plotex.Info import Info

class Plotex:

    def __init__(self):
        self.__argv = Argv()
        self.__args = self.__argv.GetArgs()
        if self.__args.verbose:
            Info.SetVerbose()

    def Run(self):
        
        Info.Info() 
        args = self.__args
        
        # generating script -> .plt
        ScriptParser(args)
        Info.Verbose("Exiting Script Parser")

        # .plt -> .tex
        gnuplotRunner = GnuplotRunner()
        if gnuplotRunner.Run():
            Exiter.Exit("gnuplot does not exit successfully!")
        Info.Verbose("Exiting Gnuplot Runner")


        if not args.ignore:
            # .tex post-processing
            if args.postprocess:
                texPostProcessor = TexPostProcessor()
                if texPostProcessor.PostProcess(args.postprocess):
                    Exiter.Exit("TeX Post-Processor does not exit successfully!")
                Info.Verbose("Exiting Tex Post-Processor") 

            # .tex -> .pdf
            latexRunner = LatexRunner()
            if latexRunner.Run():
                Exiter.Exit("LaTeX does not exit successfully!")
            Info.Verbose("Exiting LaTeX Runner")
            
            # .pdf -> local path
            pdfcopier = Pdfcopier(args)
            if pdfcopier.Copy():
                Exiter.Exit("copying does not finished successfully!")
            Info.Verbose("Exiting Pdfcopier")

        Exiter.Clean()
        return 0
