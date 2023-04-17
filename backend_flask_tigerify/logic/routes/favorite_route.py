from flask import Blueprint
from flask_jwt_extended import jwt_required
from logic.controllers.favorite_controller import *

# url comun para todos los metodos con url_prefix
favorites_routes = Blueprint('favorite_routes', __name__, url_prefix='/favorite')

# LIST ALL FAVORTES: favorites()
@favorites_routes.get('/list')
@jwt_required()
def route_favorites_list():
    return favorites()

# FIND FAVORTE BY ID: favorite(id)
@favorites_routes.get('/find/<int:id>')
@jwt_required()
def route_favorites_by_id(id):
    return favorite(id)

# SAVE FAVORTE: save()
@favorites_routes.post('/save')
@jwt_required()
def route_save():
    return save()

# UPDATE FAVORTE: put(id)
@favorites_routes.put('/update/<int:id>')
@jwt_required()
def route_update(id):
    return put(id)

# DELETE FAVORTE: delete(id)
@favorites_routes.delete('/delete/<int:id>')
@jwt_required()
def route_delete(id):
    delete(id)
    return jsonify({'message': 'Favorite deleted'})