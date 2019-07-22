from flask import Flask
from app import api_play
from flasgger import Swagger, swag_from

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_play)

    app.config['SWAGGER'] = {
        'title': 'Weather Playlist API RESTful',
        'uiversion': 2
    }

    swagger = Swagger(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)