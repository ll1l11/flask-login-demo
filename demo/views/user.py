# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user

from demo.models import User
from demo.forms import LoginForm


bp = Blueprint('user', __name__)


@bp.route('/')
@login_required
def index():
    return 'this is index'


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        user.id = 1
        login_user(user)
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))
