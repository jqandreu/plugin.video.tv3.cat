from resources.lib.utils.Utils import  getHtml, buildUrl
from resources.lib.tv3cat.TV3cat import TV3cat
import json
import xbmcaddon
import xbmcplugin
import xbmcgui
import xbmc
from resources.lib.video.Urls import url_datavideos


class UI:

    def __init__(self, base_url, addon_handle, args):
        addon = xbmcaddon.Addon()
        addon_path = xbmc.translatePath(addon.getAddonInfo('path'))
        self.tv3 = TV3cat(addon_path, addon)
        self.base_url = base_url
        self.addon_handle = addon_handle
        self.args = args
        self.mode = args.get('mode', None)
        self.url = args.get('url', [''])
        self.name = args.get('name', None)

    def run(self, mode, url):

        if mode == None:

            lFolder = self.tv3.listHome()
            self.listFolder(lFolder)

        elif mode == 'destaquem':

            lFolder = self.tv3.listDestaquem()
            self.listFolder(lFolder)


        elif mode == 'noperdis':

            lFolder = self.tv3.listNoPerdis()
            self.listFolder(lFolder)

        elif mode == 'mesvist':

            lFolder = self.tv3.listMesVist()
            self.listFolder(lFolder)

        elif mode == 'dirseccions':

            lFolder = self.tv3.dirSections()
            self.listFolder(lFolder)

        elif mode == 'progseccions':

            lFolder = self.tv3.programsSections(url)
            self.listVideos(lFolder)

        elif mode == 'dirAZemisio':

            lFolder = self.tv3.dirAZemisio()
            self.listFolder(lFolder)

        elif mode == 'dirAZtots':

            lFolder = self.tv3.dirAZtots()
            self.listFolder(lFolder)

        elif mode == 'progAZ':
            letters = self.name
            lFolder = self.tv3.programesAZ(url, letters)
            self.listFolder(lFolder)

        elif mode == 'directe':

            lFolder = self.tv3.lilistDirecte()
            self.listFolder(lFolder)

        elif mode == 'cercar':

            self.tv3.search()

        elif mode == 'listvideos':

            self.tv3.listVideos(url, None)

        elif mode == 'coleccions':

            lFolder = self.tv3.lislistColeccions()
            self.listFolder(lFolder)

        elif mode == 'playVideo':

            self.tv3.playVideo(url)

    def listFolder(self, lFolderVideos):

        for folder in lFolderVideos:

            mode = folder.mode
            name = folder.name
            url = folder.url
            iconImage = folder.iconImage
            thumbImage = folder.thumbnailImage

            urlPlugin = buildUrl({'mode': mode, 'name': name, 'url': url}, self.base_url)
            liz = xbmcgui.ListItem(name, iconImage=iconImage, thumbnailImage=thumbImage)
            liz.setInfo(type="Video", infoLabels={"title": name})
            liz.setArt({'fanart': iconImage})

            xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=urlPlugin, listitem=liz, isFolder=True)


    def listVideos(self, lVideos):

        for video in lVideos:

            urlVideo = video.url
            iconImage = video.iconImage
            thumbImage = video.thumbnailImage
            durada = video.duration
            titol = video.name

            urlPlugin = buildUrl({'mode':'playVideo','name':"",'url':urlVideo}, self.base_url)

            liz = xbmcgui.ListItem(titol, iconImage="DefaultVideo.png", thumbnailImage=thumbImage)

            infolabels = video.information

            liz.setInfo('video', infolabels)
            liz.addStreamInfo('video', {'duration': durada})
            liz.setProperty('isPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=urlPlugin, listitem=liz)


    def playVideo(self,url):
        code = url[-8:-1]

        html_data = getHtml(url_datavideos + code + '&profile=pc')

        if html_data:

            html_data = html_data.decode("ISO-8859-1")
            data = json.loads(html_data)

            urlvideo = None

            if len(data) > 0:

                media = data.get('media', {})

                if type(media) is list and len(media) > 0:
                    media_dict = media[0]
                    urlvideo = media_dict.get('url', None)
                else:
                    urlvideo = media.get('url', None)

                if urlvideo:
                    if type(urlvideo) is list and len(urlvideo) > 0:
                        urlvideo_item = urlvideo[0]
                        video = urlvideo_item.get('file', None)

                    else:
                        video = url

                    xbmc.log("Play video - url:  " + video)

                    item = xbmcgui.ListItem(path=video)
                    xbmcplugin.setResolvedUrl(self.addon_handle, True, item)