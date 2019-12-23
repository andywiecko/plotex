#!/usr/bin/python3

__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
from src.PathSetter import PathSetter
from src.Plotex import Plotex
import src.PlotexSettings as Settings
def main():

    # setting path
    plotexPath = os.path.realpath(__file__)
    pathSetter = PathSetter(plotexPath)
    pathSetter.SetPath()

    plotex = Plotex()
    plotex.Run()

if __name__=="__main__":
    main()
