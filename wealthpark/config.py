# -*- coding: utf8 -*-
import os

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/runtime/database.db' % os.environ.get('GITROOT')

class Producation(Config):
    DEBUG = False

class Development(Config):
    ENV = 'development'

class Testing(Config):
    ENV = 'development'
    TEST = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/runtime/test_database.db' % os.environ.get('GITROOT')
