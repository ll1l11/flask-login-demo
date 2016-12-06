# -*- coding: utf-8 -*-
from flask import Flask as BaseFlask
from flask import Request as BaseRequest

from demo.exceptions import JSONParseError


class Request(BaseRequest):

    def on_json_loading_failed(self, e):
        """Called if decoding of the JSON data failed.  The return value of
        this method is used by :meth:`get_json` when an error occurred.  The
        default implementation just raises a :class:`BadRequest` exception.
        .. versionchanged:: 0.10
           Removed buggy previous behavior of generating a random JSON
           response.  If you want that behavior back you can trivially
           add it by subclassing.
        .. versionadded:: 0.8
        """
        raise JSONParseError()


class Flask(BaseFlask):
    request_class = Request
