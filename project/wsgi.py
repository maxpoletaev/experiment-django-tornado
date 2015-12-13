import os
from project import get_app
from tornado.wsgi import WSGIAdapter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = WSGIAdapter(get_app())
