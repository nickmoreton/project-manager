from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lzhtqp@p411acq23l%!c(c!m5@3mr^4tj!59v!()g!yhoto@_q"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *  # noqa
except ImportError:
    pass
