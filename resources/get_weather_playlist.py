from urllib.parse import quote
from flask_restful import Resource
import requests
from flask import jsonify
from config import config


class GetPlaylist(Resource):

    def get(self, city):

        """
               It returns a playlist according to current weather from a specific city.
               It uses flaskRestful as microservise and flasgger for swagger Rest API documentation.
               ---
               parameters:
                 - in: path
                   name: city
                   type: string
                   required: true
               responses:
                 200:
                   description: RestFul API to get a playlist according to current weather from a specific city.
                   schema:
                     id: city
                     properties:
                       city:
                         type: string
                         description: City name
                         example: Campinas
                """

        #Trata o token spotify
        def request(qstring, spo_token):

            bearer = 'Bearer {}'.format(spo_token)

            if spo_token is None:
                return requests.request('GET', qstring)
            else:
                # If is a Spotify call
                return requests.request(
                    'GET', qstring, headers={
                        'Authorization': bearer})


        '''Obtém playlist do spotify de acordo com o gênero definido pela 
           temperatura atual de uma cidade específica'''
        def get_playlists(temperatura, spo_token):

            playlist = []

            if temperatura > 25:
                genero = 'pop'
            elif temperatura >= 10 and temperatura <= 25:
                genero = 'rock'
            elif temperatura < 10:
                genero = 'classical'

            qstring = '{}search?q={}&type=playlist'.format(
                config.spotify_url, quote(genero))

            resp = request(qstring, spo_token).json()


            if 'error' in resp:
               resp = {'cod':'0','cont':resp}
               return resp
            else:
                items = resp['playlists']['items']

                for playlist_name in items:
                    playlist.append(playlist_name['name'])

                result = {'cod':'1','cont':playlist}

                return result

        '''Obtém a temperatura para uma cidade específica'''
        def get_weather(city, appid):

            r_str = '{}?units=metric&q={}&appid={}'.format(config.openweather_url, quote(city), appid)

            # Requesting the API
            resp = request(r_str, None)

            return resp.json()


        weather = get_weather(city, config.openweather_API_KEY)

        if weather['cod'] != 200:
            return jsonify(weather)

        main = weather['main']

        temperatura = int(main['temp'])

        if not temperatura:
            return {"cod": 404, "message": "temperatura not found"}, 404


        playlist = get_playlists(temperatura, config.spotify_API_KEY)

        if playlist['cod'] == '1':
            playlist = playlist['cont']
        else:
            error = playlist['cont']
            return jsonify(error)

        return {"status":'success', "Cidade":city, "Temperatura":temperatura, "Playlist sugerida":playlist}, 200











