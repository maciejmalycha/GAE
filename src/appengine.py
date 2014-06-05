import os.path
import webapp2
import jinja2

from google.appengine.ext.webapp.util import run_wsgi_app


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("index.html")
        context = { 'who' : 'Bydgoszcz'}
        self.response.write(template.render(context))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
