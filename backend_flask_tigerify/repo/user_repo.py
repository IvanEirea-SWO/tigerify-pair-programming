from dao.user import User
from database.db import db

# LIST ALL USERS
def repo_get():
    users = User.query.all()
    return users

# FIND USER BY ID
def repo_get_user(id):
    return User.query.get(id)

# FIND USER BY NAME
def repo_get_user_by_name(name):
    data = User.query.filter(User.name.like(f'%{name}%')).all()
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

# SAVE USER
def repo_save(user):
    db.session.add(user)
    db.session.commit()
    return user

# UPDATE USER
def repo_put(id, user):
    user_by_id = User.query.get(id)
    
    user_by_id.id = id
    user_by_id.name = user.name

    db.session.commit()
    return user

# DELETE USER
def repo_delete(id):
    user_by_id = User.query.get(id)
    db.session.delete(user_by_id)
    db.session.commit()