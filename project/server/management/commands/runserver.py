from django.core.management import BaseCommand
from django.core.management.commands.runserver \
    import Command as BaseRunserverCommand
from tornado.ioloop import IOLoop
from project import make_app


class Command(BaseCommand):
    help = BaseRunserverCommand.help

    def add_arguments(self, parser):
        parser.add_argument('--port', '-p', dest='port', type=int, default=8000)

    def handle(self, *args, **options):
        self.check_migrations()
        app = make_app(debug=True)

        app.listen(options['port'])
        self.stdout.write('Listen on http://127.0.0.1:' + str(options['port']))

        try:
            IOLoop.current().start()
        except KeyboardInterrupt:
            pass

    check_migrations = BaseRunserverCommand.check_migrations
