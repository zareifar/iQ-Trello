# Application Configuration Settings

import os


class BaseConfig(object):
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = True

    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_HOSTNAME', 'mongodb://localhost/iqvizyondb')
    }

    # JWT Configurations
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'ROoJ63UWtL7SCg2lzc54ey3jpieXhCOqhb5d0wMpQSkZk3apB4Az3YVUjw6Yscx')

    # Celery Mongo configuration
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost/iqvizyondb')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'mongodb://localhost/iqvizyondb')
    CELERY_MONGODB_BACKEND_SETTINGS = {
        "host": os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost/iqvizyondb'),
        "port": int(os.getenv('MONGODB_PORT', 27017)),
        "database": os.getenv('MONGODB_DATABASE', "iqvizyondb"),
        "taskmeta_collection": "celery_collection",
    }

    # Mail Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER_URL', 'localhost')
    MAIL_PORT = os.getenv('MAIL_PORT', "1025")
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', "")
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', "")
    MAIL_SENDER = os.getenv('MAIL_SENDER', 'custom_sender@iqtrello.com')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'scheduler@iqtrello.com')

    # Card Check Cron Configuration
    CARD_CHECK_CRON_MINUTE = '*'
    CARD_CHECK_CRON_HOUR = '*'
    CARD_CHECK_CRON_DAY_OF_WEEK = '*'
    CARD_CHECK_CRON_MONTH_OF_YEAR = '*'


class ProductionConfig(BaseConfig):
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')

    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_HOSTNAME', 'mongodb://localhost/iqvizyondb')
    }

    # JWT Configurations
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'ROoJ63UWtL7SCg2lzc54ey3jpieXhCOqhb5d0wMpQSkZk3apB4Az3YVUjw6Yscx')

    # Celery Mongo configuration
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost/iqvizyondb')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'mongodb://localhost/iqvizyondb')
    CELERY_MONGODB_BACKEND_SETTINGS = {
        "host": os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost/iqvizyondb'),
        "port": int(os.getenv('MONGODB_PORT', 27017)),
        "database": os.getenv('MONGODB_DATABASE', "iqvizyondb"),
        "taskmeta_collection": "celery_collection",
    }

    # Mail Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER_URL', 'localhost')
    MAIL_PORT = os.getenv('MAIL_PORT', "1025")
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', "")
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', "")
    MAIL_SENDER = os.getenv('MAIL_SENDER', 'custom_sender@iqtrello.com')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'scheduler@iqtrello.com')

    # Card Check Cron Configuration
    CARD_CHECK_CRON_MINUTE = '*'
    CARD_CHECK_CRON_HOUR = '*'
    CARD_CHECK_CRON_DAY_OF_WEEK = '*'
    CARD_CHECK_CRON_MONTH_OF_YEAR = '*'


LOGGING_CONF = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(name)s %(threadName)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'fileHandler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': 'iq_trello.log',
            'maxBytes': 500000,
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    },
    'disable_existing_loggers': False
}
