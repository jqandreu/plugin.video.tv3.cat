from resources.lib.video.FolderVideo import FolderVideo
from resources.lib.tv3cat.TV3Strings import TV3Strings


class Sections:

    def __init__(self, addon):
        self.strs = TV3Strings(addon)

        self.series = FolderVideo(self.strs.get('series'), "/series/", "sections", "", "")
        self.information = FolderVideo(self.strs.get('informatius'), "/informatius/", "sections", "", "")
        self.entreteniment = FolderVideo(self.strs.get('entreteniment'), "/entreteniment/", "sections", "",
                                         "")
        self.sports = FolderVideo(self.strs.get('esports'), "/esports/", "sections", "", "")
        self.documentals = FolderVideo(self.strs.get('documentals'), "/documentals/", "sections", "", "")
        self.divulgacio = FolderVideo(self.strs.get('divulgacio'), "/divulgacio/", "sections", "", "")
        self.cultura = FolderVideo(self.strs.get('cultura'), "/cultura/", "sections", "", "")
        self.musica = FolderVideo(self.strs.get('musica'), "/musica/", "sections", "", "")
        self.emissio = FolderVideo(self.strs.get('emissio'), "/programes/", "sections", "", "")
        self.tots = FolderVideo(self.strs.get('tots'), "/programes-tots/", "sections", "", "")

        self.list = [self.series, self.information, self.entreteniment, self.sports, self.documentals, self.divulgacio,
                     self.cultura, self.musica, self.emissio, self.tots]
