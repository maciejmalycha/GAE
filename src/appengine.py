import os.path
import webapp2
import jinja2
import logging

from google.appengine.ext.webapp.util import run_wsgi_app


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("MainPage.get called")
        template = JINJA_ENVIRONMENT.get_template("index.html")
        context = { 'who' : 'Bydgoszcz'}
        self.response.write(template.render(context))

    def post(self):
        logging.debug("MainPage.post called")
        template = JINJA_ENVIRONMENT.get_template("index.html")
        context = { 'who' : self.request.get('imie') }
        self.response.write(template.render(context))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    # Call dev_appserver.py with option --log_level debug to see log below INFO
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
