
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from plotex.bcolors import bcolors

class Info:

    __verbose = False

    @staticmethod
    def Info():
        Info.Line()
        print(bcolors.BOLD+"This is ploTeX, Version",__version__,'(beta)'+bcolors.ENDC)
        Info.Line()

    def Line():
        print(bcolors.OKBLUE+40*"="+bcolors.ENDC)

    @staticmethod
    def SetVerbose():
        Info.__verbose = True

    @staticmethod
    def Verbose(message):
        if Info.__verbose:
            print(bcolors.WARNING+' *',message+bcolors.ENDC)


    @staticmethod
    def Finish():
        print(bcolors.BOLD+"ploTeX finished succesfully!"+bcolors.ENDC)
