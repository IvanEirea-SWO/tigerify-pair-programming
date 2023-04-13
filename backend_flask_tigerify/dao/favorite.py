from database.db import db

# stores many to many relationships between users and songs
class Favorite(db.Model):
    
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    
    def __init__(self, id, user_id, song_id):
        self.id = id
        self.user_id = user_id
        self.song_id = song_id