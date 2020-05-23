# Celery tasks

from _datetime import datetime
from run import celery

from database.models import Card
from services.mail_services import send_email


@celery.task(name='check_cards')
def check_cards():
    """
        Celery task to check cards.
    """
    print('checking cards...')
    sender_email = celery._preconf['MAIL_DEFAULT_SENDER']
    if celery._preconf['MAIL_SENDER']:
        sender_email = celery._preconf['MAIL_SENDER']

    late_start = Card.objects(status='received', start_date__lt=datetime.now)
    for card in late_start:
        send_email("{} Hasn't started yet".format(card.title), sender_email, [card.created_by.email],
                   "{} with id {} Should have started on {}".format(card.title, card.id, card.start_date))

    late_finish = Card.objects(status__ne='completed', end_date__lt=datetime.now)
    for card in late_finish:
        send_email("{} Hasn't finished yet".format(card.title), sender_email, [card.created_by.email],
                   "{} with id {} Should have finished on {}".format(card.title, card.id, card.end_date))

