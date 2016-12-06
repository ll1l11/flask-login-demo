# -*- coding: utf-8 -*-


class JSONException(Exception):
    code = 500
    message = 'Server Error'
    errors = None

    def __init__(self, message=None, code=None):
        super(JSONException, self).__init__()

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code


class NotJSONRequest(JSONException):
    code = 400
    message = 'Body should be a JSON object'


class JSONParseError(JSONException):
    code = 400
    message = 'Problems parsing JSON'


class ValidationFailed(JSONException):
    code = 422
    message = 'Validation Failed'

    def __init__(self, errors):
        self.errors = errors
