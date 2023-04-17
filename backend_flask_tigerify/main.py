# general
from flask import Flask, jsonify, make_response, request
from envs.dev.dev_env import config, get_database_config 
from database.db import init_app
from logic.routes.genre_route import * 
from logic.routes.song_route import *
from logic.routes.user_route import * 
from logic.routes.favorite_route import *
from flask_cors import CORS
# token
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
import os
from dotenv import load_dotenv
import datetime

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
# Los blueprints son necesarios para crear automaticamente las tablas en la database
app.register_blueprint(genres_routes)
app.register_blueprint(songs_routes)
app.register_blueprint(users_routes)
app.register_blueprint(favorites_routes)

# JWT CONFIG
# Those endpoint are test ones, should remove them when they are well implemented
# create_my_token() method creates the JWT token used in our endpoints
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

@app.post('/token')
def create_my_token():
    token_config = {
        'payload':'example',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = create_access_token(token_config)
    return jsonify({'token': token})

@app.post('/token-login')
def login():
    username = request.json['username']
    password = request.json['password']
    
    if username == 'example' and password == 'aaa':
        return create_my_token()
    else:
        response = make_response({'error-401': 'Authentication error'})
        response.status_code = 401
        return response
    
@app.get('/admin')
# This is used to protect routes with JWT tokens (bearer token of the authorization header)
# Uses the token created by create_my_token?
@jwt_required()
def dashboard():
    return 'DASHBOARD'

# MAIN
if __name__ == '__main__':
    # Así cargamos lo que está en dev_env.py y su .env
    app.config.from_object(config['dev'])
    app.run(debug=True)