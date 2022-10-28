import dj_database_url
from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bz_0^cd%v+=rmaknhg!!&!5aqur_x*u*qk$-t8qcrl8c&61#0!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.sqlite3", conn_max_age=600,
)