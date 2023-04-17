from flask import Blueprint
from flask_jwt_extended import jwt_required
from logic.controllers.user_controller import *

# url comun para todos los metodos con url_prefix
users_routes = Blueprint('user_routes', __name__, url_prefix='/user')

# LIST ALL USERS: users()
@users_routes.get('/list')
@jwt_required()
def route_users_list():
    return users()

# FIND USER BY ID: user(id)
@users_routes.get('/find/<int:id>')
@jwt_required()
def route_users_by_id(id):
    return user(id)

# FIND USER BY USERNAME: user_by_name(username)
@users_routes.get('/find/<string:username>')
@jwt_required()
def route_users_by_name(username):
    return user_by_name(username)

# REGISTER USER: register()
@users_routes.post('/register')
@jwt_required()
def route_register():
    return register()

# LOGIN USER: login()
@users_routes.post('/login')
@jwt_required()
def route_login():
    return login()

# UPDATE USER: put(id)
@users_routes.put('/update/<int:id>')
@jwt_required()
def route_update(id):
    return put(id)

# DELETE USER: delete(id)
@users_routes.delete('/delete/<int:id>')
@jwt_required()
def route_delete(id):
    delete(id)
    return jsonify({'message': 'User deleted'})