from database.db import db
from sqlalchemy.orm import relationship

# user table, the relationship of user and song is stored in favorites
class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    
    # this is necessary to delete users bc the foreign key in favorites
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete")
    
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password