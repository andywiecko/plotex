
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.Exiter import Exiter
from src.Profile import Profile
import importlib
import sys
from src.Info import Info

class ProfileLoader():
    def __init__(self,profileName):
        self.__profileName = profileName

    def Load(self,args):
        try:
            settings = importlib.import_module('profiles.'+self.__profileName, package=None)
            Info.Verbose("Profile `{profile}` loaded".format(profile=self.__profileName))
        except ImportError:
            Exiter.Exit("Error: Profile `{profile}` not found! Check for the typos!".format(profile=self.__profileName))
        
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
