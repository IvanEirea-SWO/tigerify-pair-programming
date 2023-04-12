from flask import Flask
from envs.dev.dev_env import config, get_database_config 
from database.db import init_app
from logic.routes.genre_route import * 
from logic.routes.song_route import *
from flask_cors import CORS

app = Flask(__name__)

# CORS CONFIG
app.config['JSON_AS_ASCII'] = False
CORS(app)

# DATABASE CONFIG
host = get_database_config().get('MYSQL_HOST')
user = get_database_config().get('MYSQL_USER')
password = get_database_config().get('MYSQL_PASSWORD')
database = get_database_config().get('DATABASE_NAME')
sql_track_modifications = get_database_config().get('SQLALCHEMY_TRACK_MODIFICATIONS')
# Creamos el connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+'@'+host+'/'+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Así iniciamos SQLAlchemy, nuestro ORM
init_app(app)

# BLUEPRINTS (aquí habría que usar el controller pero solo routes ahora para testear)
app.register_blueprint(genres_routes)
app.register_blueprint(songs_routes)

# MAIN
if __name__ == '__main__':
    # Así cargamos lo que está en dev_env.py y su .env
    app.config.from_object(config['dev'])
    app.run(debug=True)