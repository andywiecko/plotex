import src.Profile as Profile
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

        profile = Profile.Profile(terminalSettings, plotSettings)
        return profile
