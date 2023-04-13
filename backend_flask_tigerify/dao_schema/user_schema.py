from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password')