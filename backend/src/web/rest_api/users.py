# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from user.model import Usuario

__author__ = 'iury'


def get_all_users(_write):
        users = Usuario.query().fetch()
        users = [user.to_dict() for user in users]
        _write(json.dumps(users))


def remove_user(email):
    user = Usuario.query(Usuario.email == email).get()
    user.key.delete()


def add_user(nome, email, id):
    Usuario(nome=nome, email=email, google_id=id).put()
