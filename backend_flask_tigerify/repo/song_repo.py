from dao.song import Song
from database.db import db

# LIST ALL SONGS
def repo_get():
    songs = Song.query.all()
    return songs

# FIND SONG BY ID
def repo_get_song(id):
    return Song.query.get(id)

# FIND SONG BY NAME
def repo_get_song_by_name(name):
    data = Song.query.filter(Song.name.like(f'%{name}%')).all()
    results = [] 
    for i in data:
        info = {
            'id': i.id,
            'name': i.name,
            'length': i.length,
            'artist': i.artist
        }
        results.append(info)
    return results

# SAVE SONG
def repo_save(song):
    db.session.add(song)
    db.session.commit()
    return song

# UPDATE SONG
def repo_put(id, song):
    song_by_id = Song.query.get(id)
    
    song_by_id.id = id
    song_by_id.name = song.name
    song_by_id.length = song.length
    song_by_id.artist = song.artist

    db.session.commit()
    return song

# DELETE SONG
def repo_delete(id):
    song_by_id = Song.query.get(id)
    db.session.delete(song_by_id)
    db.session.commit()