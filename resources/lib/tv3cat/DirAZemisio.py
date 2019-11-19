from resources.lib.video.FolderVideo import FolderVideo


class DirAZemisio:

    def __init__(self):
        self.progsAC = FolderVideo("A-C", "#A-C", "progsAZemisio", "", "")
        self.progsDE = FolderVideo("D-E", "D-E", "progsAZemisio", "", "")
        self.progsFI = FolderVideo("F-I", "F-I", "progsAZemisio", "", "")
        self.progsJL = FolderVideo("J-L", "J-L", "progsAZemisio", "", "")
        self.progsMP = FolderVideo("M-P", "M-P", "progsAZemisio", "", "")
        self.progsQS = FolderVideo("Q-S", "Q-S", "progsAZemisio", "", "")
        self.progsTV = FolderVideo("T-V", "T-V", "progsAZemisio", "", "")
        self.progsXZ = FolderVideo("X-Z", "X-Z", "progsAZemisio", "", "")

        self.list = [self.progsAC, self.progsDE, self.progsFI, self.progsJL, self.progsMP, self.progsQS, self.progsTV,
                     self.progsXZ]
