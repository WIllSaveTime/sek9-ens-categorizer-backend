"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import datetime
from datetime import timedelta
from django.utils import timezone
import psycopg2
import json
from six.moves.urllib import request
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from corsheaders.defaults import default_headers
import functools


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = 'v@n@2tqy-nx6#xu)3(+=ii2m__s=7e1&akzakm)oz*tupo^3mu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  '*',
  'www.sek9.com',
  'sek9.com',
  'localhost',
  'localhost:3000',
  '172.17.0.3',
  '172.17.0.3:8000',
  '170.187.153.78',
  '192.168.0.123',
  '192.168.0.121',
  '192.168.0.121:3000',
]


# Application definition

DJANGO_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
]

THIRD_PARTY_APPS = [
  'rest_framework',
  'rest_framework.authtoken',
#   'rest_framework_jwt',
  'rest_framework_swagger',
  'rest_auth',
  'rest_auth.registration',
  'allauth',
  'allauth.account',
  'corsheaders',
  'coreapi',
  'drf_yasg',
  'nested_admin',
  'import_export',
  's3direct',
  'django_extensions',
  'django_apscheduler',
]

LOCAL_APPS = [
  'authentication',
  'member',
  'category',
  'ethereum',
  'tag',
  'domain',
  'category_tag',
  'favorit',
  'newsletter',
  'feedback',
  'feedback_answer',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
  {
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [os.path.join(BASE_DIR, 'templates')],
  'APP_DIRS': True,
  'OPTIONS': {
    'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    ],
  },
  },
]

WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'sek9'),
        'USER': os.environ.get('DATABASE_USER_NAME', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    },
    'OPTIONS': {
        'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = os.environ.get('SITE_URL', 'http://127.0.0.1:8000')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/statics/'
STATIC_ROOT = 'statics'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = default_headers + ('cache-control',)
CORS_ALLOWED_ORIGINS = [
    'http://www.sek9.com',
    'https://www.sek9.com',
    'http://sek9.com',
    'https://sek9.com',
]
CSRF_TRUSTED_ORIGINS = [
    'http://www.sek9.com',
    'https://www.sek9.com',
    'http://sek9.com',
    'https://sek9.com',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
    'DEFAULT_PERMISSION_CLASSES': (
        # 'authentication.custom_permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
        'authentication.custom_permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'authentication.custom_jwt.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'EXCEPTION_HANDLER': 'utils.error_utils.custom_exception_handler',
}

REST_AUTH_SERIALIZERS = {
    'REST_AUTH_REGISTER_SERIALIZERS': 'user.email_user_serializers.CustomEmailRegisterSerializer',
}

AUTH_USER_MODEL = 'auth.User'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'request_token': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        # 'rest_framework_jwt.utils.jwt_encode_handler',
        'authentication.custom_jwt.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
        # 'rest_framework_jwt.utils.jwt_decode_handler',
        'authentication.custom_jwt.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
        # 'rest_framework_jwt.utils.jwt_payload_handler',
        'authentication.custom_jwt.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        # 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
        'authentication.custom_jwt.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
        # 'rest_framework_jwt.utils.jwt_response_payload_handler',
        'authentication.custom_jwt.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=259200), # 3 days
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_PUBLIC_KEY': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=10),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}

SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
    'BASE_PATH': os.environ.get('SWAGGER_BASE_URL', 'http://app.sek9.com/'),
    'BASE_URL': os.environ.get('SWAGGER_BASE_URL', 'http://app.sek9.com/'),
}

ADMIN_JWT_AUTH = {
    # 'JWT_ENCODE_HANDLER':
    #     'rest_framework_jwt.utils.jwt_encode_handler',

    # 'JWT_DECODE_HANDLER':
    #     'rest_framework_jwt.utils.jwt_decode_handler',

    # 'JWT_PAYLOAD_HANDLER':
    #     'rest_framework_jwt.utils.jwt_payload_handler',

    # 'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    #     'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    # 'JWT_RESPONSE_PAYLOAD_HANDLER':
    #     'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_PUBLIC_KEY': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}

IMPORT_EXPORT_CSV_DELIMITER = ','

REST_USE_JWT = True
REST_SESSION_LOGIN = False
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True   
ACCOUNT_USERNAME_REQUIRED = False

# If these are set to None, the EC2 instance profile and IAM role are used.
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'AKIA3NKBM4FPAW5PJ6PU')
AWS_SECRET_ACCESS_KEY = os.environ.get('nqS6yp8DFftzR/k96mPq7gnihUREvOvSPgE8WPeU')

# Bucket name
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'sek9')


# The region of your bucket, more info:
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'eu-west-3')

# The endpoint of your bucket, more info:
AWS_S3_ENDPOINT_URL = os.environ.get(
    'AWS_S3_ENDPOINT_URL', 
    'https://s3-eu-west-3.amazonaws.com'
)

def generate_filename_by_now(filename, prefix=''):  
    new_filename = ''
    name, extension = os.path.splitext(filename)    
    n = timezone.now()
    new_filename = prefix + '-' + n.strftime('%Y%m%d-%H%M%S-%Z').lower() + extension
    return new_filename

S3DIRECT_DESTINATIONS = {
    'member_images': {
        'key': lambda filename, args: args + '/' + generate_filename_by_now(filename, 'member'),
    	'key_args': 'members/images',
        'auth': lambda u: u.is_staff,
        'allowed': ['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'],
        'cache_control': 'max-age=2592000',
        'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),
        'content_length_range': (100, 20000000),
        'server_side_encryption': 'AES256',
        'allow_existence_optimization': False,
    },
    'admin': {
        'key': lambda filename, args: args + '/' + generate_filename_by_now(filename, 'admin'),
        'key_args': 'admin/uploads',
        'auth': lambda u: u.is_staff,
        'allowed': ['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'],
        'cache_control': 'max-age=2592000',
        'content_disposition': lambda x: 'attachment; filename="{}_A4"'.format(x),
        'content_length_range': (100, 20000000),
        'server_side_encryption': 'AES256',
        'allow_existence_optimization': False,
    },
}

AWS_S3_BASE_IMAGE_URL = 'https://{bucket_name}.s3-{region_name}.amazonaws.com'.format(
    bucket_name=AWS_STORAGE_BUCKET_NAME,
    region_name=AWS_S3_REGION_NAME
)
#'https://sek9.s3-eu-west-3.amazonaws.com'

# Email config info
def verified_callback(member):
    member.confirmed = True
    member.save()

# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_SSL = True # 465
EMAIL_USE_TLS = False # 587
EMAIL_PORT = 465
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'admin@sek9.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '123qweasd')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = EMAIL_HOST_USER
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'confirm_mail_body.html'
EMAIL_MAIL_PLAIN = 'confirm_mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = os.environ.get('EMAIL_PAGE_DOMAIN', 'http://192.168.0.121:8000/')

EMAIL_RESET_MAIL_SUBJECT = 'Reset your email'
EMAIL_PASSWORD_RESET_MAIL_SUBJECT = 'Reset your password'
EMAIL_PASSWORD_RESET_MAIL_HTML = 'passsword_reset_mail_body.html'
MAILADDRESS_RESET_MAIL_HTML = 'email_reset_mail_body.html'
EMAIL_PASSWORD_RESET_MAIL_PLAIN = 'passsword_reset_mail_body.txt'
PASSWORD_RESET_CONFIRM_TEMPLATE = 'password_reset_confirm.html'
EMAIL_RESET_CONFIRM_TEMPLATE = 'email_reset_confirm.html'
PASSWORD_RESET_COMPLETE_TEMPLATE = 'password_reset_complete.html'
MAILADDRESS_RESET_COMPLETE_TEMPLATE = 'email_reset_complete.html'

EMAIL_COMMON_SUBJECT = 'SEK9'
EMAIL_PASSWORD_GENERATE_MAIL_SUBJECT = 'Generated your password'
EMAIL_PASSWORD_GENERATE_MAIL_HTML = 'passsword_generate_mail_body.html'
EMAIL_PASSWORD_GENERATE_MAIL_PLAIN = 'passsword_generate_mail_body.txt'

EMAIL_ACTIVITY_MAIL_HTML = 'activity_mail_body.html'
EMAIL_ACTIVITY_MAIL_PLAIN = 'activity_mail_body.txt'
EMAIL_ACTIVITY_MAIL_HTML_1 = 'activity_mail_body1.html'
EMAIL_ACTIVITY_MAIL_PLAIN_1 = 'activity_mail_body1.txt'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379/4')]
        }
    },
}

# Format string for displaying run time timestamps in the Django admin site. The default
# just adds seconds to the standard Django format, which is useful for displaying the timestamps
# for jobs that are scheduled to run on intervals of less than one minute.
# 
# See https://docs.djangoproject.com/en/dev/ref/settings/#datetime-format for format string
# syntax details.
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# Maximum run time allowed for jobs that are triggered manually via the Django admin site, which
# prevents admin site HTTP requests from timing out.
# 
# Longer running jobs should probably be handed over to a background task processing library
# that supports multiple background worker processes instead (e.g. Dramatiq, Celery, Django-RQ,
# etc. See: https://djangopackages.org/grids/g/workers-queues-tasks/ for popular options).
APSCHEDULER_RUN_NOW_TIMEOUT = 30  # Seconds

ETHER_SCAN_API_KEY_TOKEN = 'I9C5SCAAYXB41F9ITE4ZSEFEMP1VVCPR6A'
OPENSEA_API_KEY = 'eed91a052d8a49aca391c484fa13b9f8'