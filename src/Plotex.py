__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019, The Cogent Project"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings
import src.Argv as Argv
import src.ScriptLoader as ScriptLoader
import src.ProfileLoader as ProfileLoader
class Plotex():
    pass


def Glue():
    pass

def PlotexParser():
    argv = Argv.Argv()
    args = argv.GetArgs()

    scriptLoader = ScriptLoader.ScriptLoader(args.filename)
    script = scriptLoader.GetScript()

    profileLoader = ProfileLoader.ProfileLoader('default')
    profile = profileLoader.Load() 
    terminalSettings = profile.GetTerminalSettings()
    plotSettings = profile.GetPlotSettings()

    gnuplotHeaderSettings=\
r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} standalone {terminalOptions} header {header}
set output 'test.tex' 
"""

    gnuplotScriptSettings="{settings}"
    gnuplotScriptSettings="# gnuplot script settings loaded from profile\n" + gnuplotScriptSettings.format(settings="set grid") + "\n"

    gnuplotScript="# gnuplot script loaded by plotex"+script
    
    gnuplotHeaderSettings = gnuplotHeaderSettings.format(
            shebang=Settings.shebang,
            terminal=terminalSettings['terminal'],
            terminalOptions=terminalSettings['terminalOptions'],
            header=terminalSettings['header'])
    

    print(gnuplotHeaderSettings)
    print(gnuplotScriptSettings)
    print(gnuplotScript)


