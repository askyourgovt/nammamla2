from main.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*!(s08*iw-n(%(a2!w!+xl@!lm7xyuan(ovejmv+y8k9%bizb'

DEBUG=True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
)

#INTERNAL_IPS = ('127.0.0.1','192.168.126.1')
STATICFILES_DIRS += (
    os.path.join(PROJECT_ROOT, "static_local"),
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    #'HIDE_DJANGO_SQL': False,
    #'TAG': 'div',
    'ENABLE_STACKTRACES': True,
    #'HIDDEN_STACKTRACE_MODULES': ('gunicorn', 'newrelic'),
    'SHOW_TEMPLATE_CONTEXT': True,
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s.%(msecs)d] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
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
            'filename': 'nammamla.log',
            'formatter': 'verbose'
        },
        'console':{
            'level':'ERROR',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'nammamla': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },

    }

}


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# Celery settings
# For prod change ip with jobs.lakshyaresearch.com
#BROKER_URL = 'redis://127.0.0.1:6379/0'
#CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_ACCEPT_CONTENT = ['application/x-python-serialize']



#redis DND database
#REDIS_HOST = '127.0.0.1'
#REDIS_PORT = '6379'
#REDIS_DND_DATABASE_NO = 1
