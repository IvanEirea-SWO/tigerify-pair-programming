from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class GenreSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name')