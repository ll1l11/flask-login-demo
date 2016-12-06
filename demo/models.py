# -*- coding: utf-8 -*-
from datetime import datetime

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin


class User(UserMixin):
    pass
