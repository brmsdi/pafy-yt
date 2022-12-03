from flask import Flask, request
from flask_cors import CORS
from model.error import Error
from service.videoService import get_video_service
from os import environ

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v2/video": {"origins": environ['ORIGINV1']}})


@app.route("/api/v2/video", methods=["GET"])
def get_video():
    link = request.args.get('link')
    if link:
        print("var : " + environ['ORIGINV1'])
        return get_video_service(link)
    error = Error()
    error.error = "404"
    error.message = "Não foi possível processar a requisição. Tente novamente!"
    return error.__dict__


if __name__ == '__main__':
    app.run()
