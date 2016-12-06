# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import ValidationError

class LoginForm(FlaskForm):
    password = PasswordField('passowrd')
    submit = SubmitField('submit')

    def validate_password(self, field):
        if field.data != '123123':
            raise ValidationError('密码错误')
