# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from google.appengine.api import users


def index(_write_tmpl):
    user = users.get_current_user()
    if user:
        logout_url = users.create_logout_url('/')
        dic = {"user": user, "logout_url": logout_url}
    else:
        login_url = users.create_login_url('/')
        dic = {'login_url': login_url}
    _write_tmpl('/templates/home.html', dic)
