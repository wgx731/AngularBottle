import bottle
import pywapi
from bottle import route, run, static_file, redirect, request, error
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

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./app/')

@route('/img/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/img/')

@route('/lib/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/lib/')

@route('/partials/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/partials/')

# route set up
@bottle.route('/settings',method='POST')
def save_settings():
    s = bottle.request.environ.get('beaker.session')
    s['location'] = request.POST.get('location', 'Singapore').strip()
    s.save()
    redirect ('/')

@route('/weather')
def get_weather():
    s = bottle.request.environ.get('beaker.session')
    result = pywapi.get_weather_from_google(s.get('location','Singapore'),'en')
    return result

@route('/countries')
def get_countries():
    result = pywapi.get_countries_from_google('en')
    return { 'countries' : result }

@route('/')
@route('/index.html')
def index():
    raise static_file('app/index.html', root='.')

@route('/slides')
def slides():
    raise static_file('app/slides.html', root='.')

@error(404)
def mistake404(code):
    return static_file('app/404.html', root='.')

# start application
bottle.run(app=app,host='localhost', port=8080)
