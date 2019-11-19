from resources.lib.video.FolderVideo import FolderVideo
from resources.lib.tv3cat.TV3Strings import TV3Strings
from resources.lib.video.Urls import url_coleccions, url_mesvist


class Home:

    def __init__(self,addon):
        self.strs = TV3Strings(addon)

        self.avuidestaquem = FolderVideo(self.strs.get('avuidestaquem'), "", "destaquem", "", "")
        self.noperdis = FolderVideo(self.strs.get('noperdis'), url_coleccions, "noperdis", "", "")
        self.mesvist = FolderVideo(self.strs.get('mesvist'), url_mesvist, "mesvist", "", "")
        self.coleccions = FolderVideo(self.strs.get('coleccions'), "", "coleccions", "", "")
        self.programes = FolderVideo(self.strs.get('programes'), "", "programes", "", "")
        self.directe = FolderVideo(self.strs.get('directe'), "", "directe", "", "")
        self.cercar = FolderVideo(self.strs.get('cercar'), "", "cercar", "", "")

        self.list = [self.avuidestaquem, self.noperdis, self.mesvist, self.coleccions, self.programes, self.directe, self.cercar]