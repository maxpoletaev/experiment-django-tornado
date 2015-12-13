from tornado.web import Application


def make_app(**kwargs):
    from .urls import urlpatterns
    return Application(urlpatterns, **kwargs)
