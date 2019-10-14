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
