import random
import string
import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 15031})

#class HelloWorld(object):
#    @cherrypy.expose
#    def index(self):
#        return "Hello world!"

#if __name__ == '__main__':
#    cherrypy.quickstart(HelloWorld())

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
  <head></head>
  <body>
    <form method="get" action="generate">
      <input type="text" value="8" name="length"/>
      <button type="submit">Give it now!</button>
    </form>
  </body>
</html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, \
                       int(length)))

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())

