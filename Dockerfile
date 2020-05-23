FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install --upgrade pip
COPY . /iq-trello
WORKDIR /iq-trello
RUN pip install -r requirements.txt
EXPOSE 5000