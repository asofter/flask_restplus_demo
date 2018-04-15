# -*- coding: utf-8 -*- --
import os
import logging.config

from rest_demo import app
from flask import Flask, Blueprint
from rest_demo.api.blog.endpoints.posts import ns as blog_posts_namespace
from rest_demo.api.blog.endpoints.categories import ns as blog_categories_namespace
from rest_demo.api.user.endpoints.signup import ns as user_signup_namespace
from rest_demo.api.user.endpoints.auth import ns as user_auth_namespace
from rest_demo.api.user.endpoints.me import ns as user_me_namespace
from rest_demo.api.restplus import api

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(blog_posts_namespace)
api.add_namespace(blog_categories_namespace)
api.add_namespace(user_signup_namespace)
api.add_namespace(user_auth_namespace)
api.add_namespace(user_me_namespace)
app.register_blueprint(blueprint)


def main():
    log.info('* Starting development server at http://{}/api/ *'.format(app.config['SERVER_NAME']))
    app.run()


if __name__ == "__main__":
    main()