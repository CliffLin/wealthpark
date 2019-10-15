# -*- coding: utf8 -*-
import os

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % os.environ.get('GITROOT') + \
                              '/runtime/database.db'
    SERVER_NAME = '127.0.0.1:9999'

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % os.environ.get('GITROOT') + \
                              '/runtime/prod_database.db'
    DEBUG = False
    SERVER_NAME = '0.0.0.0:8080'

class Development(Config):
    ENV = 'development'

class Testing(Config):
    ENV = 'development'
    TEST = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % os.environ.get('GITROOT') + \
                              '/runtime/test_database.db'
