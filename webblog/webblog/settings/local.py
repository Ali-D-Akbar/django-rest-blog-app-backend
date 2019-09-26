from .base import *

DEBUG = True
INSTALLED_APPS += (
    'rest_framework',
    'blog.apps.BlogConfig',
    'corsheaders',
    'knox',
    'accounts',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
}

MIDDLEWARE += (
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
