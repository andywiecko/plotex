
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import sys
import os
from src.NameResolver import NameResolver

class Exiter:
    @staticmethod
    def Exit():
        print("ploTeX has encountered some problems")
        print("Cleaning...")
        Exiter.Clean()
        print("Exiting...")
        sys.exit(1)

    @staticmethod
    def Clean():
        os.system('rm -f '+NameResolver.GetOutput()+'*')
        os.system('rmdir '+NameResolver.GetOutput())

