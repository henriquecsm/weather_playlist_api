# weather_playlist_api
RestFul API to get a playlist according to current weather from a specific city.

Foi utilizado o microframework FlaskRestful para o processamento das requisições http, possibilitando o uso de microserviço, uma vez que utiliza end points para cada recurso.

Para a geração da documentação para API: foi utilizado o Flasgger que é uma extensão do Flask e utiliza a base do framework  Swagger, tornando a documenção fácil de ser gerada.
Para acessar documentação utilizar o link: http://localhost:5000/apidocs depois que o Flask iniciar o WSGIServer.

Abaixo segue diagrama de organização do código:

weather_playlist_api/
 |
 ├──config/
 |    |
 |    └──config.py
 |
 ├──resources/
 |     |
 |     └──get_weather_playlist.py
 |
 ├──app.py
 |
 └──run.py




Arquitetura utilizada:

                     |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺| 
                     |                                    FlaskRestFul process                                  |
                     |                                                                                          |
                     |                                                                                          |
                     |                                                                                          |
                     |                                                                                          |
 |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|     |      |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|            |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|            |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|       |
 |             |     |      |                 |            |             |            |                 |       |
 | API request |-----|----->| OpenWeather API |----------->| Spotify API |----------->| Return playlist |       |
 |             |     |      |                 |            |             |            |                 |       |
 |             |     |      |                 |            |             |            |                 |       |
  ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺      |       ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺              ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺              ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺        |
                     |                                                                                          | 
                     |                                                                                          |
                     |                                                                                          |
                     |                                                                                          |
                      ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
                      
 
 
 Weather Playlist API RESTful:
 
Implementation Notes:
It uses flaskRestful as microservise and flasgger for swagger Rest API documentation.

Response Class (Status 200)
RestFul API to get a playlist according to current weather from a specific city.

Example Value:
{
  "city": "Campinas"
}

Curl:
curl -X GET --header 'Accept: application/json' 'http://localhost:5000/playlist/Campinas'

Request URL:
http://localhost:5000/playlist/Campinas

Response Body:
{
  "status": "success",
  "Cidade": "Campinas",
  "Temperatura": 25,
  "Playlist sugerida": [
    "Rock Classics",
    "Rock Party",
    "Soft Rock",
    "Yacht Rock",
    "Rock This",
    "Acoustic Rock",
    "Rock Forever",
    "Soft Pop Hits",
    "Rock Covers",
    "Rock Solid",
    "90s Rock Anthems",
    "Rock Español",
    "Swagger",
    "Rock en Español",
    "Iconos del Rock Argentino",
    "Rock Drive",
    "Rock Hard",
    "Légendes du Rock",
    "Rock Ballads",
    "00s Rock Anthems"
  ]
}
Response Code:
200
Response Headers:
{
  "date": "Mon, 22 Jul 2019 16:02:02 GMT",
  "server": "Werkzeug/0.15.5 Python/3.6.5",
  "content-length": "613",
  "content-type": "application/json"
}
