from repo.song_repo import *
from dao_schema.song_schema import *
from flask import request, jsonify

song_schema = SongSchema()
songs_schema = SongSchema(many=True)

# LIST ALL SONGS: repo_get()
def songs():
    data = repo_get()
    return songs_schema.dump(data)

# FIND SONG BY ID: repo_get_song(id)
def song(id):
    return song_schema.jsonify(repo_get_song(id))

# FIND SONG BY NAME: repo_get_song_by_name(name)
def song_by_name(name):
    return songs_schema.jsonify(repo_get_song_by_name(name))

# SAVE SONG: repo_save(song)
def save():
    name = request.json['name']
    length = request.json['length']
    artist = request.json['artist']
    
    song_by_request = Song(None, name, length, artist)
    data = repo_save(song_by_request)
    return song_schema.jsonify(data)

# UPDATE SONG: repo_put(id, song)
def put(id):
    name = request.json['name']
    length = request.json['length']
    artist = request.json['artist']
    
    song_by_request = Song(None, name, length, artist)
    repo_put(id, song_by_request)
    data = repo_get_song(id) # find one element by id repo method
    return song_schema.jsonify(data)

# DELETE SONG: repo_delete(id)
def delete(id):
    repo_delete(id)
    return jsonify({'message': 'Song deleted'})