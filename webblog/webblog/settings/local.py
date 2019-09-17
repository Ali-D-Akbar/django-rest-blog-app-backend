from webblog.settings.base import *

DEBUG = True
INSTALLED_APPS += (
    'rest_framework',
    'blog.apps.BlogConfig',
    'frontend',
    'corsheaders',
    'knox',
    'accounts',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
