import bottle
import pywapi
from bottle import route, run, send_file, static_file
from beaker.middleware import SessionMiddleware

# session set up
app = bottle.default_app()
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './session',
    'session.auto': True
}
app = SessionMiddleware(app, session_opts)

# static files (js,css,partials) set up
@route('/js/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/js/')

@route('/css/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/css/')

@route('/lib/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/lib/')

@route('/partials/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/partials/')

# route set up
@bottle.route('/test')
def test():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = s.get('test',0) + 1
    s.save()
    return 'Test counter: %d' % s['test']

@route('/weather')
def get_weather():
    result = pywapi.get_weather_from_google('Singapore','en')
    return result

@route('/countries')
def get_countries():
    result = pywapi.get_countries_from_google('en')
    return { 'countries' : result }

@route('/')
@route('/index.html')
def index():
    raise static_file('app/index.html', root='.')

# start application
bottle.run(app=app,host='localhost', port=8080)
