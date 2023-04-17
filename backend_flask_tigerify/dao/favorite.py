from database.db import db
from sqlalchemy.orm import relationship

# stores many to many relationships between users and songs
class Favorite(db.Model):
    
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    # this ondelet and the user and song relationship are necessary to delete favorites bc the foreign key of users and songs
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id', ondelete="CASCADE"))
    user = relationship("User", back_populates="favorites")
    song = relationship("Song", back_populates="favorites")
    
    def __init__(self, id, user_id, song_id):
        self.id = id
        self.user_id = user_id
        self.song_id = song_id