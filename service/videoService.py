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


def convert_to_json(video, json):
    return json.dumps(video, ensure_ascii=False).encode('utf8')
