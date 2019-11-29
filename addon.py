# -*- coding: utf-8 -*-

'''
 TV3cat Kodi addon
 @author: jqandreu
 @contact: jqsandreu@gmail.com
'''
import sys
import urlparse
import xbmcplugin
import xbmc
from resources.lib.ui.UI import UI
xbmc.log("plugin.video.tv3.cat - addon.py")
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmc.log("plugin.video.tv3.cat - addon.py - args: ")
xbmc.log(str(args))

xbmcplugin.setContent(addon_handle, 'movies')

mode = args.get('mode', None)
url = args.get('url', [''])

'''
name = args.get('name', None)
if (name != None) and (len(name) > 0):
    name = name[0].replace("\n", "")
program = args.get('program', None)
'''

ui = UI(base_url, addon_handle, args)


ui.run(mode, url)
  
