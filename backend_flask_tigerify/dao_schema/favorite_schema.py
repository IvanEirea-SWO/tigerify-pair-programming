from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class FavoriteSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'user_id', 'song_id')