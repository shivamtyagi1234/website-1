"""
Django settings for pclubWebsite project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$4p#tsin((&rnm!%696^2xutz_-n5k)o&mnwg3z*^f7&--99h&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'home',
    'social_django',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'pclubWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = '1bb44747fe47d4452460'
SOCIAL_AUTH_GITHUB_SECRET = '888dbf7469fa2496f4508d99c17ff178d6bade67'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '974649954440-oqe59nmr4k7ac9mh3ghl5ufgrnck2052.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'bEDkAPEPZP_r-SRIy9BXvZtf'

WSGI_APPLICATION = 'pclubWebsite.wsgi.application'

LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/home'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3.db',
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

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [ os.path.join(BASE_DIR,'staticFiles') ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    # 'cleanup_on_startup': True,
    # 'custom_undo_redo_levels': 20,
    # 'selector': 'textarea',
    # 'theme': 'modern',
    # 'plugins': '''
    #         textcolor save link image media preview codesample contextmenu
    #         table code lists fullscreen  insertdatetime  nonbreaking
    #         contextmenu directionality searchreplace wordcount visualblocks
    #         visualchars code fullscreen autolink lists  charmap print  hr
    #         anchor pagebreak
    #         ''',
    # 'toolbar1': '''
    #         fullscreen preview bold italic underline | fontselect,
    #         fontsizeselect  | forecolor backcolor | alignleft alignright |
    #         aligncenter alignjustify | indent outdent | bullist numlist table |
    #         | link image media | codesample |
    #         ''',
    # 'toolbar2': '''
    #         visualblocks visualchars |
    #         charmap hr pagebreak nonbreaking anchor |  code |
    #         ''',
    # 'contextmenu': 'formats | link image',
    # 'menubar': True,
    # 'statusbar': True,
}
