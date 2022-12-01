class Video:
    def __init__(self, videoid='', author='', title='', duration='', thumb='', items=[]):
        self.videoid = videoid
        self.author = author
        self.title = title
        self.duration = duration
        self.thumb = thumb
        self.items = items


class Item:
    def __init__(self, key, extension='', resolution='', url='', bitrate='', rawbitrate='', filesize='', mediatype=''):
        self.key = key
        self.extension = extension
        self.resolution = resolution
        self.url = url
        self.bitrate = bitrate
        self.rawbitrate = rawbitrate
        self.filesize = filesize
        self.mediatype = mediatype
