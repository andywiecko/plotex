
__author__ = "Andrzej Więckowski"
__copyright__ = "Copyright 2019"
__license__ = "GNU"
__version__ = "2.0.0"
__email__ = "andrzej.wieckowski@pwr.edu.pl"

from src.Exiter import Exiter
from src.Profile import Profile
import importlib
import sys
import glob
from src.Info import Info
from src.NameResolver import NameResolver
import src.PlotexSettings as Settings

def ReplaceSlash(listOfArgs):
    return '\\\\'.join('\n'.join(listOfArgs).split('\\')).split('\n')


class ProfileLoader():
    def __init__(self,profileName):
        self.__profileName = profileName

    def GetProfileList(self):
        profiles = glob.glob(NameResolver.GetProfilePath()+"*.py")
        profiles = [profile.split('/')[-1][:-3] for profile in profiles] 
        init = '__init__'
        if init in profiles: profiles.remove(init)
        return '\n * '.join(profiles)

    def Load(self,args):
        try:
            settings = importlib.import_module('profiles.'+self.__profileName, package=None)
            Info.Verbose("Profile `{profile}` loaded".format(profile=self.__profileName))
        except ImportError:
            profileList = self.GetProfileList()
            Exiter.Exit("Profile `{profile}` not found! Check for the typos! \nProfiles avaliable:\n * {list}".format(profile=self.__profileName,list=profileList))
        
        terminalSettings = settings.terminalSettings
        plotSettings = settings.plotSettings
        if args.terminal:
            terminalSettings['terminal'] = args.terminal

        if args.append:
            terminalSettings['header'] += ReplaceSlash(args.append)

        if args.replace:
            terminalSettings['header'] = ReplaceSlash(args.replace)

        profile = Profile(terminalSettings, plotSettings)
        return profile
