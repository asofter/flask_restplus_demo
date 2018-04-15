import logging

from flask import request, g
from flask_restplus import Resource
from rest_demo.api.user.serializers import user_auth
from rest_demo.api.restplus import api
from rest_demo.database.models import User, user_loader
from rest_demo import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

log = logging.getLogger(__name__)

ns = api.namespace('user_auth', path='/user/auth', description='Operations related to user auth process')


@ns.route('/login')
@api.response(404, 'User does not exist.')
class LoginItem(Resource):

    @api.response(201, 'Successfully logged in.')
    @api.expect(user_auth)
    def post(self):
        # get the post data
        data = request.json

        # fetch the user data
        user = User.query.filter_by(
            email=data.get('email')
        ).first()
        if not user or not bcrypt.check_password_hash(
                user.password, data.get('password')
        ):
            return api.abort(404, "User does not exist.")

        auth_token = create_access_token(identity=user)
        return {"auth_token": auth_token}, 200