import json
import webapp2
import logging
import models

class GetComicList(webapp2.RequestHandler):
	def get(self):
	    comics = models.Comic.query().order(models.Comic.publisher).fetch(1000)  # list of Comic models
	    logging.warning(comics)
	    comics = [  # list of comic dictionaries
	    	{'publisher': c.publisher,
	    	 'title': c.title,
	    	 'booknum': c.booknum}
	    	 for c in comics
	    ]
	    comics = json.dumps(comics)  # json string
	    self.response.write(comics)
		# self.response.headers['Content-Type'] = 'application/json'


app = webapp2.WSGIApplication([
    ('/retrieve_comics', GetComicList)
], debug=True)