from dao.favorite import Favorite
from database.db import db

# LIST ALL FAVORITES
def repo_get():
    favorites = Favorite.query.all()
    return favorites

# FIND FAVORITE BY ID
def repo_get_favorite(id):
    return Favorite.query.get(id)

# SAVE FAVORITE
def repo_save(favorite):
    db.session.add(favorite)
    db.session.commit()
    return favorite

# UPDATE FAVORITE
def repo_put(id, favorite):
    favorite_by_id = Favorite.query.get(id)
    
    favorite_by_id.id = id
    favorite_by_id.name = favorite.name

    db.session.commit()
    return favorite

# DELETE FAVORITE
def repo_delete(id):
    favorite_by_id = Favorite.query.get(id)
    db.session.delete(favorite_by_id)
    db.session.commit()