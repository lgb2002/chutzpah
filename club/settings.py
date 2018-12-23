"""
Django settings for studybee_completed project.
This is a qna blog.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#ERROR OCCUR
APPEND_SLASH=False

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'templates'),
#)

# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xz1snho&0ie=ukhkx69pt(nubm=cpo32vna_uk$@p3w1ehvs8o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.puhungclub.kr']
# SECURITY WARNING: don't run with debug turned on in production!

#TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'chutzpah',
)

INSTALLED_APPS += ('django_summernote', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
'''
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)
'''
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#TEST = 'home/gibaek/club/main/templates/main'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), 
            'main/templates/main',
            'chutzpah/templates/chutzpah',
            #TEST,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ]#,
            #
            #loaders' : [
            #    'django_jinja.loaders.AppLoader',
            #    'django_jinja.loaders.FileSystemLoader',
            #]
            #
        },
    },
]

ROOT_URLCONF = 'club.urls'

WSGI_APPLICATION = 'club.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https:
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, '')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Login url
#LOGIN_REDIRECT_URL = '/chutzpah/index.html'


# MEDIA
# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
# MEDIA_URL = '/upoad_files/'

# to use in login_required decorator
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

# to use in django.contrib.auth.views.login function
LOGIN_REDIRECT_URL = '/'

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    'height': '380',

    # Use proper language setting automatically (default)
    'lang': None,

    # Or, set editor language/locale forcely
    # 'lang': 'ko-KR',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        # ['fontname', ['fontname']],
        ['color', ['color']],
        ['style', ['bold', 'italic', 'underline']],
        # ['style', ['clear']],
        ['para', ['ul', 'ol', 'paragraph']],
        # ['height', ['height']],
        # ['table', ['table']],
        ['insert', ['link', 'hr']],
        # ['insert', ['picture']],
        ['view', ['fullscreen', 'codeview']],
    ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    # 'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    # 'attachment_storage_class': 'my.custom.storage.class.name',

    # Set external media files for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'inplacewidget_external_css': (
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css',
        '//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css',
    ),
    'inplacewidget_external_js': (
        '//code.jquery.com/jquery-1.9.1.min.js',
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',
    ),
}