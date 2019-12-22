
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import src.PlotexSettings as Settings

class ScriptHeader:
    def __init__(self,terminalSettings):

        self.__header = r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} {terminalOptions} header "{header}"
set output '{plotexPath}/{output}/{tmpfile}.tex' 
"""
        self.__Header(terminalSettings)

    def __Header(self,terminalSettings):
        self.__header = \
                self.__header.format(
                shebang = Settings.shebang,
                tmpfile = Settings.tmpfile,
                terminal = terminalSettings['terminal'],
                terminalOptions = ' '.join(terminalSettings['terminalOptions']),
                header = "\\n".join(terminalSettings['header']),
                output = Settings.output,
                plotexPath = Settings.plotexPath)

    def GetHeader(self,args):
        if args.ignore:
            return ''
        else:
            return self.__header
