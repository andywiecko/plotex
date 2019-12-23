
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings

class PathSetter:
    def __init__(self,path):

        __plotexPath = path.split('/')
        self.__plotexPath = '/'.join(__plotexPath[:-1])

    def SetPath(self):
        Settings.plotexPath = self.__plotexPath
        localPath = os.getcwd()
        Settings.localPath = localPath

