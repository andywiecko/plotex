import os
import src.PlotexSettings as Settings

class LatexRunner:
    def __init__(self):
        self.latexCompiler = Settings.latexCompiler
        self.latexFlags = Settings.latexFlags
        outputFlag = '--output-dir '+Settings.plotexPath+'/'+Settings.output+'/'
        PATH = Settings.plotexPath+'/'+Settings.output+'/'+Settings.tmpfile+'.tex'
        cmd = ' '.join([self.latexCompiler,self.latexFlags,outputFlag,PATH])
        os.system(cmd)
