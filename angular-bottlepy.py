import os
from os import environ as env
from sys import argv
import bottle
import pywapi
from bottle import route, run, static_file, redirect, request, error
from beaker.middleware import SessionMiddleware

bottle.debug(True)

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

@route('/scenarios.js')
def scenario():
    return static_file('scenarios.js',root='./test/e2e/')

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./app/')

@route('/js/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/js/')

@route('/css/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/css/')

@route('/img/:path#.+#')
def server_static(path):
    return static_file(path, root='./app/img/')

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
    raise static_file('index.html', root='./app')

@route('/slides')
def slides():
    raise static_file('slides.html', root='./app')

@route('/tests')
def tests():
    raise static_file('runner.html', root='./test/e2e/')

@error(404)
def mistake404(code):
    return static_file('404.html', root='./app')

# start application
bottle.run(app=app,host='0.0.0.0', port=argv[1])
