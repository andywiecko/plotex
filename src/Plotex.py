__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019, The Cogent Project"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings
import src.Argv as Argv
import src.ScriptLoader as Loader

class Plotex():
    pass


def Glue():
    pass

def PlotexParser():
    argv = Argv.Argv()
    args = argv.GetArgs()

    loader = Loader.ScriptLoader(args.filename)
    script = loader.GetScript()

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
            terminal="cairolatex",
            terminalOptions="",
            header=r"'\usepackage{mathptmx}'")
    

    print(gnuplotHeaderSettings)
    print(gnuplotScriptSettings)
    print(gnuplotScript)


