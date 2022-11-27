from os import makedirs, path
import pafy
from model.video import Video, Item
from service.videoService import extract_dict, convert_to_json
import json
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description='Programa para criar json com metadados do YouTube.')
    parser.add_argument(dest='link',
                        metavar='link',
                        nargs=1,
                        type=str,
                        help='Informe o link do vídeo do YouTbe.')

    parser.add_argument(dest='fileName',
                        metavar="fileName",
                        nargs=1,
                        type=str,
                        help='Nome do arquivo que será gerado')

    """https://www.youtube.com/watch?v=gQxQ9K4gnn0&ab_channel=VitorRamosVideos"""

    args = parser.parse_args()
    fileVideo = pafy.new(args.link[0])
    video = extract_dict(file=fileVideo, video=Video, item=Item)

    if not path.isdir("./files"):
        makedirs("./files")

    with open(f"./files/{args.fileName[0]}.json", "w+") as outfile:
        outfile.write(convert_to_json(video, json).decode())
        outfile.close()
