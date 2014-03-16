__author__ = 'iury'

from  google.appengine.ext import ndb

class Post(ndb.Model):
    title = ndb.stringProperty(required=True)
    content = ndb.stringProperty(required=True)





