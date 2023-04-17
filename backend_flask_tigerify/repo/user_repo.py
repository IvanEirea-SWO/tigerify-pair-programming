from dao.user import User
from database.db import db

# LIST ALL USERS
def repo_get():
    users = User.query.all()
    return users

# FIND USER BY ID
def repo_get_user(id):
    return User.query.get(id)

# FIND USER BY USERNAME
def repo_get_user_by_name(username):
    data = User.query.filter(User.name.like(f'%{username}%')).all()
    results = []
    for i in data:
        info = {
            'id': i.id,
            'username': i.username,
            'email': i.email,
            'password': i.password
        }
        results.append(info)
    return results

# REGISTER USER
def repo_register(user):
    db.session.add(user)
    db.session.commit()
    return user

# LOGIN USER

# UPDATE USER
def repo_put(id, user):
    user_by_id = User.query.get(id)
    
    user_by_id.id = id
    user_by_id.username = user.username
    user_by_id.email = user.email
    user_by_id.password = user.password

    db.session.commit()
    return user

# DELETE USER
def repo_delete(id):
    user_by_id = User.query.get(id)
    db.session.delete(user_by_id)
    db.session.commit()