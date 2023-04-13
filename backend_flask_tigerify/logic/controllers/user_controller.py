from repo.genre_repo import *
from dao_schema.genre_schema import *
from flask import request, jsonify

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# LIST ALL GENRES: repo_get()
def genres():
    data = repo_get()
    return genres_schema.dump(data)

# FIND GENRE BY ID: repo_get_genre(id)
def genre(id):
    return genre_schema.jsonify(repo_get_genre(id))

# FIND GENRE BY NAME: repo_get_genre_by_name(name)
def genre_by_name(name):
    return genres_schema.jsonify(repo_get_genre_by_name(name))

# SAVE GENRE: repo_save(genre)
def save():
    name = request.json['name']
    
    genre_by_request = Genre(None, name)
    data = repo_save(genre_by_request)
    return genre_schema.jsonify(data)

# UPDATE GENRE: repo_put(id, genre)
def put(id):
    name = request.json['name']
    
    genre_by_request = Genre(None, name)
    repo_put(id, genre_by_request)
    data = repo_get_genre(id) # find one element by id repo method
    return genre_schema.jsonify(data)

# DELETE GENRE: repo_delete(id)
def delete(id):
    repo_delete(id)
    return jsonify({'message': 'Genre deleted'})