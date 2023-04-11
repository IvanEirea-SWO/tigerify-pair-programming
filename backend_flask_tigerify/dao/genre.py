from database.db import db

# strong table
class Genre(db.Model):
    
    __tablename__ = 'genres'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    # song list?
    
    def __init__(self, id, name):
        self.id = id
        self.name = name