import dj_database_url
from  .base_settings import *
from task1.utils.env_variables import get_env_variable

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DEBUG')

ALLOWED_HOSTS = []

DATABASES["default"] = dj_database_url.parse(
    get_env_variable("PROD_DATABASE_URL"), conn_max_age=600
)

MIDDLEWARE += [    
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DATABASES["default"]["NAME"] = get_env_variable("DATABASE_NAME")
DATABASES["default"]["ENGINE"] = get_env_variable("DATABASE_ENGINE")
DATABASES["default"]["POOL_OPTIONS"] = {
    "POOL_SIZE": 20,
    "MAX_OVERFLOW": 30,
    "RECYCLE": 24 * 60 * 60,
}

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIR = [
    BASE_DIR / 'static'
]