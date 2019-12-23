
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
from src.NameResolver import NameResolver
from src.Info import Info

class LatexRunner:
    def __init__(self):
        self.latexCompiler = Settings.latexCompiler
        self.latexFlags = Settings.latexFlags
        self.outputFlag = '--output-dir '
        self.outputFlag += NameResolver.GetOutput()
        self.filename = NameResolver.GetTmpfileTex()
        self.__CMD = ' '.join([
            self.latexCompiler,
            self.latexFlags,
            self.outputFlag,
            self.filename])

        Info.Verbose("Latex Runner initialization")

    def Run(self):
        return os.system(self.__CMD)

