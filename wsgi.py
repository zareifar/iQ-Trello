from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from celery import Celery
from celery.schedules import crontab
from database import initialize_db
from api.routes import initialize_routes
from iq_trello import flask_app, api
from config import DevelopmentConfig, ProductionConfig, LOGGING_CONF


if flask_app.config["ENV"] == "production":
    flask_app.config.from_object(ProductionConfig)
else:
    flask_app.config.from_object(DevelopmentConfig)

# Initialize extensions
initialize_db(flask_app)
initialize_routes(api)
bcrypt = Bcrypt(flask_app)
jwt = JWTManager(flask_app)
mail = Mail(flask_app)


def make_celery(app):
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery


celery = make_celery(flask_app)

celery.conf['CELERY_IMPORTS'] = ("tasks.celery_worker",)
celery.conf['CELERYBEAT_SCHEDULE'] = {
    'check-cards-task': {
        'task': 'check_cards',
        'schedule': crontab(
            flask_app.config['CARD_CHECK_CRON_MINUTE'],
            flask_app.config['CARD_CHECK_CRON_HOUR'],
            flask_app.config['CARD_CHECK_CRON_DAY_OF_WEEK'],
            flask_app.config['CARD_CHECK_CRON_MONTH_OF_YEAR']
        ),
    },
}

if __name__ == "__main__":

    if flask_app.debug is not True:
        from logging.config import dictConfig

        dictConfig(LOGGING_CONF)

    flask_app.run(host="0.0.0.0", port=5000, use_reloader=True)

