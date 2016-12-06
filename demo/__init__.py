# -*- coding: utf-8 -*-
from flask_login import user_logged_in

from . import factory
from .ext import login_manager
from .models import User
from .helpers import register_blueprints


def create_app(config=None):
    app = factory.create_app(config)

    register_auth()

    # register blueprints
    module_prefix = __name__ + '.views.'
    package_path = app.root_path + '/views'
    register_blueprints(app, module_prefix, package_path)

    # subscirbe to user login signals
    subscribe_user_login(app)

    return app


def register_auth():

    @login_manager.user_loader
    def load_user(user_id):
        print('*' * 20, user_id)
        return User()

    login_manager.login_view = 'user.login'


# 订阅登录的signals
def subscribe_user_login(app):
    @user_logged_in.connect_via(app)
    def when_user_login(sender, user):
        # print('#' * 30, sender, args, kwargs)
        print('#' * 30, sender, user)
