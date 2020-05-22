from flask import Flask
from flask_restful import Api
from api.errors import errors
from flask_mail import Mail


flask_app = Flask(__name__)

api = Api(flask_app, errors=errors)


@flask_app.route('/')
def welcome():
    return 'Welcome'
