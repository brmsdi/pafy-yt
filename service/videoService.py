def extract_dict(file, video, item):
    items = list()
    result = video(file.author, file.title, file.duration)
    for fileVideo in file.allstreams:
        if (fileVideo.extension == 'mp4' and fileVideo.mediatype == 'normal') \
                or (fileVideo.extension == 'm4a' and fileVideo.mediatype == 'audio'):
            extracted_item = item(fileVideo.extension, fileVideo.resolution, fileVideo.url)
            items.append(extracted_item.__dict__)
    result.items = items.copy()
    return result.__dict__


def convert_to_json(video, json):
    return json.dumps(video, ensure_ascii=False).encode('utf8')
