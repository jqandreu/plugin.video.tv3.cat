from resources.lib.video.FolderVideo import FolderVideo


class DirAZtots:

    def __init__(self):
        self.progsAC = FolderVideo("A-C", "#A-C", "progsAZtots", "", "")
        self.progsDE = FolderVideo("D-E", "D-E", "progsAZtots", "", "")
        self.progsFI = FolderVideo("F-I", "F-I", "progsAZtots", "", "")
        self.progsJL = FolderVideo("J-L", "J-L", "progsAZtots", "", "")
        self.progsMP = FolderVideo("M-P", "M-P", "progsAZtots", "", "")
        self.progsQS = FolderVideo("Q-S", "Q-S", "progsAZtots", "", "")
        self.progsTV = FolderVideo("T-V", "T-V", "progsAZtots", "", "")
        self.progsXZ = FolderVideo("X-Z", "X-Z", "progsAZtots", "", "")

        self.list = [self.progsAC, self.progsDE, self.progsFI, self.progsJL, self.progsMP, self.progsQS, self.progsTV,
                     self.progsXZ]