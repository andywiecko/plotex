
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.Profile import Profile
import importlib
import sys

class ProfileLoader():
    def __init__(self,profileName):
        self.__profileName = profileName

    def __Info(self):
        info=\
"""\
Profile not found!
Check for the typos!\
"""
        return info

    def Load(self,args):
        try:
            settings = importlib.import_module('profiles.'+self.__profileName, package=None)
        except ImportError:
            print(self.__Info())
            sys.exit(1)
        
        terminalSettings = settings.terminalSettings
        plotSettings = settings.plotSettings
        if args.terminal:
            terminalSettings['terminal'] = args.terminal

        if args.append:
            terminalSettings['header'] += args.append

        if args.replace:
            terminalSettings['header'] = args.replace

        profile = Profile(terminalSettings, plotSettings)
        return profile
