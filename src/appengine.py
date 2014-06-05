import os.path
import webapp2
import jinja2
import logging
import datetime

from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class SignRecord(db.Model):
    imie = db.StringProperty()
    date = db.DateTimeProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("MainPage.get called")
        parent = db.Key.from_path("SignRecord", "id")
        query = db.Query(SignRecord).ancestor(parent).order('date')
        signatures = query.run()
        template = JINJA_ENVIRONMENT.get_template("index.html")
        context = { 'signatures' : signatures }
        self.response.write(template.render(context))

    def post(self):
        logging.debug("MainPage.post called")
        parent = db.Key.from_path("SignRecord", "id")
        record = SignRecord(imie = self.request.get('imie'),
                            date = datetime.datetime.now(),
                            parent = parent)
        record.put()
        self.redirect("/")


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    # Call dev_appserver.py with option --log_level debug to see log below INFO
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
