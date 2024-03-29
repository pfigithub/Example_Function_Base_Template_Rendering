from mysite2.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tb)-wz+(h84ogs3^zgaw%lgvhp+6c#284@9pbfp0cjrs0kur81'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

COMPRESS_ENABLED = not DEBUG

ALLOWED_HOSTS = []

# sites framework

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

#CSRF_COOKIE_SECURE = True
