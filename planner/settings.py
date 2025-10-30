import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-key-troque-em-producao'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'pages',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'pages.middleware.StaticFilesMiddleware',
]

ROOT_URLCONF = 'planner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Telas')],
    },
]

DATABASES = {}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Recursos de Estilo'),
    os.path.join(BASE_DIR, 'Telas'),
]
