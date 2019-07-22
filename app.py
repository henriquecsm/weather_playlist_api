
from flask import Blueprint
from flask_restful import Api
from resources.get_weather_playlist import GetPlaylist


api_play = Blueprint('api', __name__)
api = Api(api_play)


# Defining Route
api.add_resource(GetPlaylist, '/playlist/<string:city>')