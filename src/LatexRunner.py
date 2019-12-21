import os
import src.PlotexSettings as Settings

class LatexRunner:
    def __init__(self):
        self.latexCompiler = Settings.latexCompiler
        self.latexFlags = Settings.latexFlags
        cmd = ' '.join([self.latexCompiler,self.latexFlags,Settings.tmpfile+'.tex'])
        os.system(cmd)
