#coding: utf-8
#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world')

class QueryStringHandler(webapp2.RequestHandler):
    def get(self):
        nome = self.request.get("nome")
        self.response.write("Ola %s" %nome)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/query", QueryStringHandler)
], debug=True)
