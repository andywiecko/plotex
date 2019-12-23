
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
import src.NameResolver as NameResolver

class LatexRunner:
    def __init__(self):
        self.latexCompiler = Settings.latexCompiler
        self.latexFlags = Settings.latexFlags
        self.outputFlag = '--output-dir '
        self.outputFlag += NameResolver.NameResolver.GetOutput()
        self.filename = NameResolver.NameResolver.GetTmpfileTex()
        cmd = ' '.join([
            self.latexCompiler,
            self.latexFlags,
            self.outputFlag,
            self.filename])
        os.system(cmd)
