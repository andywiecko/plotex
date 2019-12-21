import src.Profile as Profile

class ProfileLoader():
    def __init__(self,profileName):
        __profileName = profileName

    def Load(self):
        import profiles.default as settings
        profile = Profile.Profile(settings.terminalSettings,settings.plotSettings)
        return profile
