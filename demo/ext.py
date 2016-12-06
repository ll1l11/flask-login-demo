# -*- coding: utf-8 -*-

from flask import current_app
from werkzeug.local import LocalProxy
from flask_login import LoginManager

__all__ = (
    'logger',
    'login_manager',
)


logger = LocalProxy(lambda: current_app.logger)
login_manager = LoginManager()
