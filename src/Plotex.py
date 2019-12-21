__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019, The Cogent Project"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings
import src.Argv as Argv
import src.ScriptLoader as ScriptLoader
import src.ProfileLoader as ProfileLoader

class Plotex:

    def __init__(self):
        self.__header = r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} standalone {terminalOptions} header {header}
set output 'test.tex' 
"""
        self.__settings = "# gnuplot script settings loaded from profile\n{settings}"
        self.__body = "# gnuplot script loaded by plotex"

    def PlotexParser(self):
        argv = Argv.Argv()
        args = argv.GetArgs()
    
        scriptLoader = ScriptLoader.ScriptLoader(args.filename)
        script = scriptLoader.GetScript()
    
        profileLoader = ProfileLoader.ProfileLoader('default')
        profile = profileLoader.Load() 
        terminalSettings = profile.GetTerminalSettings()
        plotSettings = profile.GetPlotSettings()
    
        self.__header = self.__header.format(
                shebang=Settings.shebang,
                terminal=terminalSettings['terminal'],
                terminalOptions=terminalSettings['terminalOptions'],
                header=terminalSettings['header'])
     
        self.__settings = self.__settings.format(settings="\n".join(plotSettings)) + "\n"
    
        self.__body +=  script
        
       
    
        print(self.Glue())
    

    def Glue(self):
        return "\n".join(
                [self.__header,
                self.__settings,
                self.__body])
