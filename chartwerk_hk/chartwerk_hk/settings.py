"""
Django settings for chartwerk_hk project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k@i2yungc3$k%-_=gdrwo#-d8x#*60s)*4iq+d%%=qj29+2xhb"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'chartwerk',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chartwerk_hk.urls'

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
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'chartwerk_hk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ieee_spectrum_chartwerk',
        'USER': 'josh',
        'PASSWORD': os.environ.get('CHARTWERK_DB_PW'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

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

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CHARTWERK_DOMAIN = 'https://ieee-spectrum-chartwerk.herokuapp.com'
CHARTWERK_AWS_BUCKET = 'chartwerk.ieeespectrum.joshuarrr'
CHARTWERK_AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
CHARTWERK_AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

CHARTWERK_GITHUB_ORG = 'IEEESpectrum'
CHARTWERK_GITHUB_REPO = 'chartwerk_chart-templates'
CHARTWERK_GITHUB_TOKEN = os.environ.get('GH_CHARTWERK_TOKEN')

CHARTWERK_EMBED_TEMPLATE_CONTEXT = lambda chart: {
    'chart_path': 'https://s3.amazonaws.com/chartwerk.ieeespectrum.joshuarrr/charts/',
    'embed_script': 'https://s3.amazonaws.com/chartwerk.ieeespectrum.joshuarrr/main-embed.bundle.js',
}

CHARTWERK_COLOR_SCHEMES = {
    'categorical': {
        'default': [
            '#03A6E3',
            '#D40A06',
            '#F75F08',
            '#F5CD09',
            '#48B44C',
            '#682590',
            '#3FBEB6',
            '#C9C9C9',
        ],
        'highlight': [
            '#03A6E3',
            '#7A7A7A',
            '#898989',
            '#989898',
            '#A7A7A7',
            '#B8B8B8',
            '#C9C9C9',
            '#DADADA',
        ],
    },
    'sequential': {
        'red': [
            '#f5c8c1',
            '#eea89e',
            '#e8887a',
            '#e26856',
            '#dc4730',
            '#c13621',
            '#9d2c1b',
            '#700f00',
        ],
        'blue': [
            '#cfebff',
            '#a5dbff',
            '#7bc2f2',
            '#5cb5f2',
            '#359fe6',
            '#2487c9',
            '#0267ab',
            '#004a7a',
        ],
        'green': [
            '#d9ebc3',
            '#bde388',
            '#a2cf63',
            '#7bc049',
            '#65a835',
            '#4e941b',
            '#327303',
            '#245400',
        ],
        'warm': [
            '#ffe261',
            '#ffc226',
            '#ffa310',
            '#f57f00',
            '#e35000',
            '#cc3300',
            '#a31600',
            '#700f00',
        ],
        'cool': [
            '#d4f2cb',
            '#ace6b1',
            '#8bd9b9',
            '#5ac9c1',
            '#2cb9c7',
            '#0c94c2',
            '#0275c2',
            '#004a7a',
        ],
    },
    'diverging': {
        'redBlue': [
            '#0078d1',
            '#299aee',
            '#5ab5fa',
            '#99d3ff',
            '#f7a699',
            '#f57864',
            '#e34e36',
            '#c42c14',
        ],
        'redBlueMix': [
            '#0064c2',
            '#2985f2',
            '#7e94f7',
            '#aea4fc',
            '#d99ee8',
            '#de7cbf',
            '#ce5269',
            '#ba230b',
        ],
        'redGreen': [
            '#c12e17',
            '#ea652b',
            '#fc9943',
            '#fcc857',
            '#bee16d',
            '#99cf51',
            '#6ebe34',
            '#539f1e',
        ],
        'orangePurple': [
            '#b35806',
            '#e08214',
            '#fdb863',
            '#fee0b6',
            '#d8daeb',
            '#b2abd2',
            '#8073ac',
            '#542788',
        ],
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
