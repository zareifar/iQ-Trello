# REST API Model Serializers

import bson
from marshmallow import Schema, fields, ValidationError


class ObjectId(fields.Field):
    """
    Marshmallow field for :class:`bson.ObjectId`
    """

    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value, attr, data):
        try:
            return bson.ObjectId(value)
        except (TypeError, bson.errors.InvalidId):
            raise ValidationError('Invalid ObjectId.')


class UserSchema(Schema):
    email = fields.String()


class CommentSchema(Schema):
    content = fields.String()
    sender = fields.Nested(UserSchema(only=("email",)))
    created_date = fields.DateTime(format='%Y-%m-%d %H:%M')

    class Meta:
        ordered = True
        dateformat = '%Y-%m-%d %H:%M'


class CardSchema(Schema):
    id = ObjectId()
    title = fields.String()
    content = fields.String()
    status = fields.String()
    start_date = fields.DateTime(format='%Y-%m-%d %H:%M')
    end_date = fields.DateTime(format='%Y-%m-%d %H:%M')
    assigned_to = fields.Nested(UserSchema(only=("email",), many=True))
    completion_date = fields.DateTime(format='%Y-%m-%d %H:%M')
    created_by = fields.Nested(UserSchema(only=("email",)))
    created_date = fields.DateTime(format='%Y-%m-%d %H:%M')
    comments = fields.Nested(CommentSchema(many=True))

    class Meta:
        ordered = True
        dateformat = '%Y-%m-%d %H:%M'


class ProjectSchema(Schema):
    id = ObjectId()
    title = fields.String()
    status = fields.String()
    created_by = fields.Nested(UserSchema(only=("email",)))
    created_date = fields.DateTime(format='%Y-%m-%d %H:%M')
    cards = fields.Nested(CardSchema(exclude=['content', 'assigned_to', 'completion_date',
                                              'comments'], many=True))

    class Meta:
        ordered = True
        dateformat = '%Y-%m-%d %H:%M'


class UserDetailSchema(UserSchema):
    projects = fields.Nested(ProjectSchema(only=("id",), many=True))
    cards = fields.Nested(CardSchema(only=("id",), many=True))

    class Meta:
        ordered = True


user_schema = UserDetailSchema()

projects_schema = ProjectSchema(exclude=['cards', ], many=True)
project_schema = ProjectSchema()

card_schema = CardSchema()

comment_schema = CommentSchema()

