def extract_dict(file, video, item):
    items = list()
    result = video(videoid=file.videoid, author=file.author, title=file.title, duration=file.duration,
                   thumb=file.getbestthumb())
    count = 1
    for fileVideo in file.allstreams:
        extracted_item = item(count, fileVideo.extension, fileVideo.resolution, fileVideo.url, fileVideo.bitrate,
                              fileVideo.rawbitrate, fileVideo.get_filesize())
        items.append(extracted_item.__dict__)
        count += 1
    result.items = items.copy()
    return result.__dict__


def convert_to_json(video, json):
    return json.dumps(video, ensure_ascii=False).encode('utf8')
