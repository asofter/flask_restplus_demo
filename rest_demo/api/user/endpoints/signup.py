import logging

from flask import request
from flask_restplus import Resource
from rest_demo.api.user.business import create_user
from rest_demo.api.user.serializers import user_auth
from rest_demo.api.restplus import api
from rest_demo.database.models import User
from flask_jwt_extended import create_access_token

log = logging.getLogger(__name__)

ns = api.namespace('user_signup', path='/user/signup', description='Operations related to user signup process')


@ns.route('/')
@api.response(403, 'User already exists. Please Log in.')
@api.response(401, 'User can not be created.')
class SignupItem(Resource):

    @api.response(201, 'User successfully registered.')
    @api.expect(user_auth, validate=True)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            return api.abort(403, "User already exists. Please Log in.")
        else:
            new_user = create_user(data)
            if new_user:
                auth_token = create_access_token(identity=new_user)
                return {"auth_token": auth_token}, 201

        return None, 401
