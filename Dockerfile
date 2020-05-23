FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install --upgrade pip
ENV FLASK_ENV development
COPY . /iq-trello
WORKDIR /iq-trello
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python run.py