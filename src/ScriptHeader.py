import src.PlotexSettings as Settings

class ScriptHeader:
    def __init__(self,terminalSettings):

        self.__header = r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} {terminalOptions} header "{header}"
set output '{tmpfile}.tex' 
"""
        self.__Header(terminalSettings)

    def __Header(self,terminalSettings):
        self.__header = \
                self.__header.format(
                shebang = Settings.shebang,
                tmpfile = Settings.tmpfile,
                terminal = terminalSettings['terminal'],
                terminalOptions = ' '.join(terminalSettings['terminalOptions']),
                header = "\\n".join(terminalSettings['header']))

    def GetHeader(self,args):
        if args.ignore:
            return ''
        else:
            return self.__header
