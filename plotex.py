#!/usr/bin/python3

__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

import os
import src.PlotexSettings as Settings
from src.Plotex import Plotex

def main():

    # setting path
    plotexPath = os.path.realpath(__file__)
    plotexPath = plotexPath.split('/')
    plotexPath = '/'.join(plotexPath[:-1])
    localPath = os.getcwd()

    Settings.localPath = localPath
    Settings.plotexPath = plotexPath

    plotex = Plotex()
    plotex.Run()

if __name__=="__main__":
    main()
