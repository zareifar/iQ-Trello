# Database Models

from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

from database import db


class Comment(db.EmbeddedDocument):
    content = db.StringField(required=True)
    sender = db.ReferenceField('User')
    created_date = db.DateTimeField(required=True, default=datetime.now)

    class Meta:
        collection_name = "comment"


class Card(db.Document):
    title = db.StringField(required=True)
    content = db.StringField()
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()
    status = db.StringField(required=True, default='received', choices={'received', 'started', 'checked', 'completed'})
    assigned_to = db.ListField(db.ReferenceField('User'))
    created_by = db.ReferenceField('User')
    project = db.ReferenceField('Project')
    created_date = db.DateTimeField(required=True, default=datetime.now)
    completion_date = db.DateTimeField()
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    class Meta:
        collection_name = "card"


class Project(db.Document):
    title = db.StringField(required=True, unique=True)
    status = db.StringField(required=True, default='active', choices={'active', 'archived'})
    created_by = db.ReferenceField('User')
    created_date = db.DateTimeField(required=True, default=datetime.now)
    cards = db.ListField(db.ReferenceField('Card'), reverse_delete_rule=db.PULL)

    class Meta:
        collection_name = "project"
        strict = False

    def find_all(self):
        items = self._repo.find_all()
        return items


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    projects = db.ListField(db.ReferenceField('Project'), reverse_delete_rule=db.PULL)
    cards = db.ListField(db.ReferenceField('Card'), reverse_delete_rule=db.PULL)
    assignments = db.ListField(db.ReferenceField('Card'), reverse_delete_rule=db.PULL)

    class Meta:
        collection_name = "user"

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Project, 'created_by', db.CASCADE)
User.register_delete_rule(Card, 'created_by', db.CASCADE)

Project.register_delete_rule(Card, 'project', db.CASCADE)


