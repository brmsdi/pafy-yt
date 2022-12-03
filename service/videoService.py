import pafy

from model.video import Video, Item


def extract_dict(file, video, item):
    items = list()
    result = video(videoid=file.videoid, author=file.author, title=file.title,
                   duration=file.duration, thumb=file.getbestthumb())
    count = 1
    for stream in file.allstreams:
        extracted_item = item(count, stream.extension, stream.resolution, stream.url_https,
                              stream.bitrate, stream.rawbitrate,
                              stream.get_filesize(), stream.mediatype)
        items.append(extracted_item.__dict__)
        count += 1
    result.items = items.copy()
    return result.__dict__


def get_video_service(link=''):
    file_video = pafy.new(link)
    if file_video.videoid:
        return extract_dict(file=file_video, video=Video, item=Item)
