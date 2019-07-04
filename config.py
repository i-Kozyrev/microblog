# coding=UTF-8

"""
What module do?

Created by ikozyrev at 04.07.2019.
"""

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or "postgresql://mb-user:449722@localhost:5432/microblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
