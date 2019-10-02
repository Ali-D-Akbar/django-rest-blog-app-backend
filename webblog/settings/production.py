from .base import *

DEBUG = False
INSTALLED_APPS += (
    # other apps for production site
)
<<<<<<< HEAD

AWS_LOCATION = 'static'
AWS_ACCESS_KEY_ID = '<youraccessid>'
AWS_SECRET_ACCESS_KEY = '<yoursecretkey>'
AWS_STORAGE_BUCKET_NAME = '<yourbucketname>'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'app.storage_backends.MediaStorage'
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
AWS_DEFAULT_ACL = None
=======
>>>>>>> master
