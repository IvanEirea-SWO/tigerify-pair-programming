from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class SongSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'length', 'artist')