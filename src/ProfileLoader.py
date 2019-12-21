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

    def Load(self):
        try:
            settings = importlib.import_module('profiles.'+self.__profileName, package=None)
            profile = Profile.Profile(settings.terminalSettings,settings.plotSettings)
            return profile
        except ImportError:
            print(self.__Info())
            sys.exit(1)
