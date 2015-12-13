DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'project.server',
    'project.counter',
]

SECRET_KEY = 'qwerty'

ROOT_URLCONF = []

DEBUG = True
