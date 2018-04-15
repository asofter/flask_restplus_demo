import logging

from flask import request, g
from flask_restplus import Resource
from rest_demo.api.user.serializers import user_auth, user_update
from rest_demo.api.restplus import api
from rest_demo.database.models import User, user_loader
from rest_demo.api.user.business import update_user
from rest_demo import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

log = logging.getLogger(__name__)

ns = api.namespace('user_me', path='/user/me', description='Operations related to user data')


@ns.route('/')
@api.response(404, 'User not found.')
@api.header('Authorization', 'JWT Token', required=True, defaultValue='Bearer ')
class MeItem(Resource):

    @api.response(200, 'User data')
    @jwt_required
    @user_loader
    def get(self):
        user = g.user
        if user:
            return {
                'user_id': user.id,
                'email': user.email,
                'admin': user.admin,
                'registered_on': user.registered_on.strftime("%d.%m.%Y %H:%m")
            }

    @jwt_required
    @user_loader
    @api.expect(user_update)
    @api.response(204, 'User successfully updated.')
    def put(self):
        user = g.user
        data = request.json
        update_user(user, data)
        return None, 204