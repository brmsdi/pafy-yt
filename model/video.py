class Video:
    def __init__(self, videoid='', author='', title='', duration='', items=[]):
        self.videoid = videoid
        self.author = author
        self.title = title
        self.duration = duration
        self.items = items


class Item:
    def __init__(self, key, extension='', resolution='', url='', bitrate='', rawbitrate='', filesize=''):
        self.key = key
        self.extension = extension
        self.resolution = resolution
        self.url = url
        self.bitrate = bitrate
        self.rawbitrate = rawbitrate
        self.filesize = filesize

