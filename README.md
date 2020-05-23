[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://opensource.org/licenses/MIT)   [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://documenter.getpostman.com/view/3771340/Szt5gBNM)    [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# iQ-Trello
 
a simple project management application

Click here to read the [REST API Document](https://documenter.getpostman.com/view/3771340/Szt5gBNM) 

This project provides a Restful  API for a simple project management application requested by iQvizyon

Basic Requirements:
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [Flask 1.1](https://flask.palletsprojects.com/en/1.1.x/)
* [MongoEngine 0.20](http://mongoengine.org/)
* [Marshmallow 3.6](https://marshmallow.readthedocs.io/en/stable/)
* [Celery 4.4](http://www.celeryproject.org/)

### Installing

#### 1. Using docker-compose

Set you desired environment variables in docker-compose.yml and run:

```
docker-conpose build
docker-compose up
```

#### 2. Manually

##### Configure the settings

Create a new MongoDB database and set the environment variable to specify your environment configuration settings

```
export FLASK_ENV=development
```

or

```
export FLASK_ENV=production
```

Or you can configure the settings, such as Secret Key, MongoDB, Mail, etc. in your preferred config object.

```
sudo nano config.py
```

##### Run the server

Once you are done, run the server:

```
python run.py
```

##### Running the task scheduler

There is a task scheduler using Celery to check on all the cards and notify the card owner if a card has passed it's start date or finish date.
You need to have a mail server ready to use this feature. You can also use a Public mail server such as Gmail or you can use Python's SMTP Server.
If you want to start the SMTP Server, go ahead with the following command:

```
python -m smtpd -n -c DebuggingServer localhost:1025
```

Once you have the mail server running, you can start the scheduler:

```
cd iq-trello
celery -A run worker -B -Q celery -l INFO
```

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
