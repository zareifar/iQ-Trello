# Mail Service

from threading import Thread
from flask_mail import Message
from wsgi import flask_app, mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
            print('Mail sent')
        except ConnectionRefusedError:
            return 'MAIL SERVER] not working', 500


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    Thread(target=send_async_email, args=(flask_app, msg)).start()
