# -*- coding: utf-8 -*- --

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Flask settings
    SERVER_NAME = 'localhost:8888'
    DEBUG = True

    BCRYPT_LOG_ROUNDS = 4
    SECRET_KEY = 'my_precious'

    JWT_AUTH_URL_RULE='/user/auth/login'
    JWT_AUTH_USERNAME_KEY='email'
    JWT_AUTH_HEADER_PREFIX='Bearer'
    JWT_VERIFY_EXPIRATION=False
    JWT_SECRET_KEY='Secret'


    # Flask-Restplus settings
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/rest_demo?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True