# -*- coding: utf-8 -*-
from flask_bootstrap import Bootstrap

from .wrappers import Flask
from .ext import login_manager


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = 'demo.config.Config'
    app.config.from_object(config)

    login_manager.init_app(app)
    Bootstrap(app)

    return app
