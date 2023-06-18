"""
Django settings for piracy_prevention project.

Generated by 'django-admin startproject' using Django 1.11.23.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fa-*k)mfpm1as)-la0l-#$@-e*1*6z489&36awx*&qj+1--gr!'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = bool(int(os.environ.get('DEBUG',1)))

DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['<copied-public-dns-of-machine>', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    # Core of the authentication framework
    'django.contrib.auth',
    # Allows permissions to be associated with models you create.
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'piracy_prevention_api',
    'website',
    'widget_tweaks',
]

    # 'sslserver',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'piracy_prevention.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'website/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'website.context_processor.add_my_login_form',
            ],
        },

    },
]

WSGI_APPLICATION = 'piracy_prevention.wsgi.application'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'piracy_prevention_api.UserProfile'

# MEDIA_ROOT = '/media'

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "assets")


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ),
    # 'DEFAULT_PERMISSION_CLASSES' : (
    #     'piracy_prevention_api.permissions.DisableOptionsPermission',
    # ),
    # 'DEFAULT_PERMISSION_CLASSES' : (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_RENDERER_CLASSESS':(
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES':(
    #     'rest_framework.parsers.JSONParser'
    # ),
}

# To redirect user after successfull login
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/home'

AUTHENTICATION_BACKENDS = (
    'piracy_prevention_api.backends.MyAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 100
# SECURE_HSTS_PRELOAD = True
