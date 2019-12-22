#!/usr/bin/python3

#import src.Plotex as Plotex

import os
import src.Plotex as Plotex
import src.PlotexSettings as Settings

def main():
    plotexPath = os.path.realpath(__file__)
    plotexPath = plotexPath.split('/')
    plotexPath = '/'.join(plotexPath[:-1])
    localPath = os.getcwd()

    Settings.localPath = localPath
    Settings.plotexPath = plotexPath

    Plotex.Plotex()


if __name__=="__main__":
    main()
