from tornado.concurrent import run_on_executor, futures
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado import gen
from time import sleep

from .models import Vote


class TaskRunner:
    def __init__(self, loop=None):
        self.io_loop = loop or IOLoop.instance()
        self.executor = futures.ThreadPoolExecutor(2)

    @run_on_executor
    def increment(self):
        sleep(0.1)
        return 'hello'


tasks = TaskRunner()

class CounterHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        message = yield tasks.increment()
        self.write(message)
