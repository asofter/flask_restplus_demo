from flask_restplus import fields
from rest_demo.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='E-mail'),
    'password': fields.String(required=True, description='Password'),
    'registered_on': fields.DateTime(readonly=True, description='Registered date and time')
})

user_auth = api.model('User Auth', {
    'email': fields.String(required=True, description='E-mail'),
    'password': fields.String(required=True, description='Password')
})

user_update = api.model('User Auth', {
    'email': fields.String(description='E-mail'),
    'password': fields.String(description='Password')
})