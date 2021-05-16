from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

# Create new Flask application
app = Flask(__name__)

# Set up SQLalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

# Define a class for user model
class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   userName = db.Column(db.String)
   name = db.Column(db.String)
   password = db.Column(db.String)

db.create_all()

# Create data abstraction layer
class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_view = 'user_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'user_many'

    id = fields.Integer()
    userName = fields.Str(required=True)
    name = fields.Str()
    password = fields.Str(required=True)

class UserMany(ResourceList):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}

class UserOne(ResourceDetail):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}

api = Api(app)
api.route(UserMany, 'user_many', '/users')
api.route(UserOne, 'user_one', '/user/<int:id>')

# main loop to run in debug mode
if __name__ == '__main__':
   app.run(debug=True)
