from flask import Blueprint
from flask_jwt_extended import jwt_required
from logic.controllers.genre_controller import *

# url comun para todos los metodos con url_prefix
genres_routes = Blueprint('genre_routes', __name__, url_prefix='/genre')

# LIST ALL GENRES: genres()
@genres_routes.get('/list')
@jwt_required()
def route_genres_list():
    return genres()

# FIND GENRE BY ID: genre(id)
@genres_routes.get('/find/<int:id>')
@jwt_required()
def route_genres_by_id(id):
    return genre(id)

# FIND GENRE BY NAME: genre_by_name(name)
@genres_routes.get('/find/<string:name>')
@jwt_required()
def route_genres_by_name(name):
    return genre_by_name(name)

# SAVE GENRE: save()
@genres_routes.post('/save')
@jwt_required()
def route_save():
    return save()

# UPDATE GENRE: put(id)
@genres_routes.put('/update/<int:id>')
@jwt_required()
def route_update(id):
    return put(id)

# DELETE GENRE: delete(id)
@genres_routes.delete('/delete/<int:id>')
@jwt_required()
def route_delete(id):
    delete(id)
    return jsonify({'message': 'Genre deleted'})