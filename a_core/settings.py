import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-rj#-z^kx3j+1ay397otg6j8m_8#v^$^$jys6&41vy^&6le)ezc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','.vercel.app', '127.0.0.1', '*']

CSRF_TRUSTED_ORIGINS = [ 'https://*' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'django_htmx',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'a_messageboard',
    "whitenoise.runserver_nostatic",

    # My apps
    'a_home',
    'a_users',
    'django_celery_beat'
]

SITE_ID = 1

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add this line
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'a_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'a_core.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",#corr
        "NAME":  "thedb",
        "USER":"postgres", 
        "PASSWORD": "1910_Lionelmasia",
        "HOST":  "database-2.cdqeqesumfb0.us-east-1.rds.amazonaws.com", #urdatabase1-4
        "PORT": "5432",
    }
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='fleektyre@gmail.com'
EMAIL_HOST_PASSWORD='wirtbvakhwphsauf'
EMAIL_PORT=587
EMAIL_USE_TLS=True #transport layer security
DEFAULT_FROM_EMAIL=f'Chidiiiii'
ACCOUNT_EMAIL_SUBJECT_PREFIX=''

CELERY_BROKER_URL='redis://localhost:6379/0'
#CELERY_CONFIG
CELERY_BROKER_CONNECTION_RESTART_ON_STARTUP=True