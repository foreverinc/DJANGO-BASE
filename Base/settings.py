from pathlib import Path
import os
from django.contrib import messages
from .variables import *


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^0$vx$f1+mi78#z!tb-f@j@+%pa+8uk4z3y$23muakmn9cpqi%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'main',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "debug_toolbar",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "phonenumber_field",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    
]

ROOT_URLCONF = 'Base.urls'

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

WSGI_APPLICATION = 'Base.wsgi.application'

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


if DEBUG:
    STATIC_URL = 'static/'
    MEDIA_URL='media/'
    STATICFILES_DIRS =[
        os.path.join(BASE_DIR, 'static'),
        os.path.join(BASE_DIR,'media'),
    ]
    STATIC_ROOT=os.path.join(BASE_DIR,'assets')
    MEDIA_ROOT=os.path.join(BASE_DIR,'media_cdn')
else:
    STATIC_URL=GITHUB_LINK
    CLOUDINARY_STORAGE={
        'CLOUD_NAME': CLOUD_NAME,
        'API_KEY': CLOUD_APIKEY,
        'API_SECRET': CLOUD_SECRET,
    }
    DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#site configuration for allauth
if DEBUG:
    SITE_ID=DEV_SITE
    ACCOUNT_DEFAULT_HTTP_PROTOCOL='http'
else:
    SITE_ID=PROD_SITE
    ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
    
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
SOCIALACCOUNT_PROVIDERS = {
    'globus': {
        'SCOPE': [
            'openid',
            'profile',
            'email',
            'urn:globus:auth:scope:transfer.api.globus.org:all'
        ]
    }
}

ACCOUNT_MAX_EMAIL_ADDRESSES= 2
ACCOUNT_EMAIL_VERIFICATION ='optional' #none #mandatory #optional
ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_LOGOUT_REDIRECT_URL ='account_login'
LOGIN_REDIRECT_URL='home'
ACCOUNT_AUTHENTICATION_METHOD='username_email'
ACCOUNT_USERNAME_MIN_LENGTH =4
ACCOUNT_EMAIL_SUBJECT_PREFIX=PROJECT_NAME
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=True


#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_USER
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

#error handling
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
