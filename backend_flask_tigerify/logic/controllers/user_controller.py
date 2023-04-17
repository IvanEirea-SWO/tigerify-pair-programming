from repo.user_repo import *
from dao_schema.user_schema import *
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# LIST ALL USERS: repo_get()
def users():
    data = repo_get()
    return users_schema.dump(data)

# FIND USER BY ID: repo_get_user(id)
def user(id):
    return user_schema.jsonify(repo_get_user(id))

# FIND USER BY USERNAME: repo_get_user_by_name(username)
def user_by_name(username):
    return users_schema.jsonify(repo_get_user_by_name(username))

# REGISTER USER: repo_register(user)
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    # hashing the password
    password_hash = generate_password_hash(password)
    
    user_by_request = User(None, username, email, password_hash)
    data = repo_register(user_by_request)
    return user_schema.jsonify(data)

# LOGIN USER
def login():
    username = request.json['username']
    #email = request.json['email']
    password = request.json['password']
    
    user = User.query.filter_by(username = username).one_or_none() # ??
    
    if user is not None and check_password_hash(user.password, password):
        return jsonify({"success": "AUTH"})
    else:
        return jsonify({"error": "UNAUTH"})

# UPDATE USER: repo_put(id, user)
def put(id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    # hashing the password
    password_hash = generate_password_hash(password)
    
    user_by_request = User(None, username, email, password_hash)
    repo_put(id, user_by_request)
    data = repo_get_user(id) # find one element by id repo method
    return user_schema.jsonify(data)

# DELETE USER: repo_delete(id)
def delete(id):
    repo_delete(id)
    return jsonify({'message': 'User deleted'})