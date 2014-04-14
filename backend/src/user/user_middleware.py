# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from .model import Usuario

def execute(next_process, handler, dependencies, **kwargs):
    user = users.get_current_user()
    if user:
        google_id = user.user_id()
        query = Usuario.query_by_google(google_id)
        logged_user = query.get()
        if not logged_user:
            logged_user = Usuario(nome=user.nickname(), email=user.email(), google_id=google_id)
            logged_user.put()

        dependencies["logged_user"] = logged_user
        dependencies['logout_url'] = users.create_logout_url('/')

    else:
        dependencies["logged_user"] = False
        dependencies['login_url'] = users.create_login_url('/')

    next_process(dependencies, **kwargs)
