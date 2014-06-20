from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

class Comic(ndb.Model):
    publisher = ndb.StringProperty()
    title = ndb.StringProperty()
    booknum = ndb.IntegerProperty()