from flask import Blueprint
from logic.controllers.song_controller import *

# url comun para todos los metodos con url_prefix
songs_routes = Blueprint('song_routes', __name__, url_prefix='/song')

# LIST ALL SONGS: songs()
@songs_routes.get('/list')
def route_songs_list():
    return songs()

# FIND SONG BY ID: song(id)
@songs_routes.get('/find/<int:id>')
def route_songs_by_id(id):
    return song(id)

# FIND SONG BY NAME: song_by_name(name)
@songs_routes.get('/find/<string:name>')
def route_songs_by_name(name):
    return song_by_name(name)

# SAVE SONG: save()
@songs_routes.post('/save')
def route_save():
    return save()

# UPDATE SONG: put(id)
@songs_routes.put('/update/<int:id>')
def route_update(id):
    return put(id)

# DELETE SONG: delete(id)
@songs_routes.delete('/delete/<int:id>')
def route_delete(id):
    delete(id)
    return 'Song deleted'