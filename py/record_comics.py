import json
import webapp2
import logging
from models import Comic
from google.appengine.ext import ndb

class PostComicList(webapp2.RequestHandler):
	def post(self):
	    comics = self.request.body
	    logging.warning(comics)
	    comics = json.loads(comics)

	    for comic in comics:
	    	newComic = Comic(
	    				publisher=comic.get('publisher'),
	    				title=comic.get('title'),
	    				booknum=comic.get('booknum'),
	    				writer=comic.get('writer'),
	    				artist=comic.get('artist'),
	    				misc=comic.get('misc')
	    				)
	    	newComic.put()
	    	self.response.out.write(newComic.key.urlsafe())

app = webapp2.WSGIApplication([
    ('/py/record_comics', PostComicList)
], debug=True)