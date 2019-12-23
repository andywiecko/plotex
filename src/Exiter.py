
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import sys
import os
from src.NameResolver import NameResolver
from src.bcolors import bcolors

class Exiter:
    @staticmethod
    def Exit(message=''):
        if message!='': print(bcolors.FAIL+"Error:",message+bcolors.ENDC)
        print(bcolors.FAIL+bcolors.BOLD+"ploTeX has encountered some problems"+bcolors.ENDC+bcolors.ENDC)
        print("Cleaning...")
        Exiter.Clean()
        print("Exiting...")
        sys.exit(1)

    @staticmethod
    def Clean():
        os.system('rm -f '+NameResolver.GetOutput()+'*')
        os.system('rmdir '+NameResolver.GetOutput())

