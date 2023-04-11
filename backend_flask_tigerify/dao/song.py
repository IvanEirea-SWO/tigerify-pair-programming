from database.db import db

# weak table
class Song(db.Model):
    
    __tablename__ = 'songs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    length = db.Column(db.Integer)
    artist = db.Column(db.String(200))
    
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genres = db.relationship('Genre', backref='songs')
    
    def __init__(self, id, name, length, artist):
        self.id = id
        self.name = name
        self.length = length
        self.artist = artist