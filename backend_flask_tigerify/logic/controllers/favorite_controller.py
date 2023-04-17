from repo.favorite_repo import *
from dao_schema.favorite_schema import *
from flask import request, jsonify

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)

# LIST ALL FAVORITES: repo_get()
def favorites():
    data = repo_get()
    return favorites_schema.dump(data)

# FIND FAVORITE BY ID: repo_get_favorite(id)
def favorite(id):
    return favorite_schema.jsonify(repo_get_favorite(id))

# SAVE FAVORITE: repo_save(favorite)
def save():
    user_id = request.json['user_id']
    song_id = request.json['song_id']
    
    favorite_by_request = Favorite(None, user_id, song_id)
    data = repo_save(favorite_by_request)
    return favorite_schema.jsonify(data)

# UPDATE FAVORITE: repo_put(id, favorite)
def put(id):
    user_id = request.json['user_id']
    song_id = request.json['song_id']
    
    favorite_by_request = Favorite(None, user_id, song_id)
    repo_put(id, favorite_by_request)
    data = repo_get_favorite(id) # find one element by id repo method
    return favorite_schema.jsonify(data)

# DELETE FAVORITE: repo_delete(id)
def delete(id):
    repo_delete(id)
    return jsonify({'message': 'Favorite deleted'})