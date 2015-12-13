from tornado.web import RequestHandler
from .models import Vote


class CounterHandler(RequestHandler):
    def get(self):
        Vote.objects.create()
        counter_value = len(Vote.objects.all())
        self.write(str(counter_value))
