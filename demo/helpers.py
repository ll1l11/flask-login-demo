# -*- coding: utf-8 -*-
import pkgutil
import importlib

from flask import Blueprint


def register_blueprints(app, module_prefix, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.
    :param app: the Flask application
    :param module_prefix: a string on the front of every module name
    :param package_path: a path to look for modules in
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules([package_path], module_prefix):
        m = importlib.import_module(name)
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv
