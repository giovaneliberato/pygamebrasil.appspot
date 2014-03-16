__author__ = 'iury'

import src.database.Database as db


def doPost(title, content):
    post = db.Post(title, content)
    post.put()


