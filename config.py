# Application Configuration Settings


class BaseConfig(object):
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True

    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/iqvizyondb'
    }

    # JWT Configurations
    JWT_SECRET_KEY = 'ROoJ63UWtL7SCg2lzc54ey3jpieXhCOqhb5d0wMpQSkZk3apB4Az3YVUjw6Yscx'

    # Celery Mongo configuration
    CELERY_RESULT_BACKEND = "mongodb://localhost/iqvizyondb"
    CELERY_BROKER_URL = 'mongodb://localhost/iqvizyondb'
    CELERY_MONGODB_BACKEND_SETTINGS = {
        "host": "localhost",
        "port": 27017,
        "database": "iqvizyondb",
        "taskmeta_collection": "celery_collection",
    }

    # Mail Configuration
    MAIL_SERVER = "localhost"
    MAIL_PORT = "1025"
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_SENDER = 'custom_sender@iqtrello.com'
    MAIL_DEFAULT_SENDER = 'scheduler@iqtrello.com'

    # Card Check Cron Configuration
    CARD_CHECK_CRON_MINUTE = '*'
    CARD_CHECK_CRON_HOUR = '*'
    CARD_CHECK_CRON_DAY_OF_WEEK = '*'
    CARD_CHECK_CRON_MONTH_OF_YEAR = '*'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'

    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/iqvizyondb'
    }

    # JWT Configurations
    JWT_SECRET_KEY = 'ROoJ63UWtL7SCg2lzc54ey3jpieXhCOqhb5d0wMpQSkZk3apB4Az3YVUjw6Yscx'

    # Celery Mongo configuration
    CELERY_RESULT_BACKEND = "mongodb://localhost/iqvizyondb"
    CELERY_BROKER_URL = 'mongodb://localhost/iqvizyondb'
    CELERY_MONGODB_BACKEND_SETTINGS = {
        "host": "localhost",
        "port": 27017,
        "database": "iqvizyondb",
        "taskmeta_collection": "celery_collection",
    }

    # Mail Configuration
    MAIL_SERVER = "localhost"
    MAIL_PORT = "1025"
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_SENDER = 'custom_sender@iqtrello.com'
    MAIL_DEFAULT_SENDER = 'scheduler@iqtrello.com'

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
