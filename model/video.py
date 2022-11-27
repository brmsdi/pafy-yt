class Video:
    def __init__(self, author='', title='', duration='', items=[]):
        self.author = author
        self.title = title
        self.duration = duration
        self.items = items


class Item:
    def __init__(self, extension='', resolution='', url=''):
        self.extension = extension
        self.resolution = resolution
        self.url = url
