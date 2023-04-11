from dao.genre import Genre
from database.db import db

# LIST ALL GENRE
def repo_get():
    genres = Genre.query.all()
    return genres

# FIND GENRE BY ID
def repo_get_genre(id):
    return Genre.query.get(id)

# FIND GENRE BY NAME
def repo_get_genre_by_name(name):
    data = Genre.query.filter(Genre.name == name).all()
    results = [] 
    for i in data:
        info = {
            'id': i.id,
            'name': i.name,
        }
        results.append(info)
    return results

# SAVE GENRE
def repo_save(genre):
    db.session.add(genre)
    db.session.commit()
    return genre

# UPDATE GENRE
def repo_put(id, genre):
    genre_by_id = Genre.query.get(id)
    
    genre_by_id.id = id
    genre_by_id.name = genre.name

    db.session.commit()
    return genre

# DELETE GENRE
def repo_delete(id):
    genre_by_id = Genre.query.get(id)
    db.session.delete(genre_by_id)
    db.session.commit()