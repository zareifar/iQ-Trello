# REST API Views

from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from database.models import Project, Card, Comment, User
from .serializers import project_schema, projects_schema, card_schema, user_schema
from api.errors import SchemaValidationError, ProjectAlreadyExistsError, InternalServerError, UpdatingProjectError,\
    DeletingProjectError, ProjectNotExistsError, UpdatingCardError, DeletingCardError, CardNotExistsError


class UserApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        dump_data = user_schema.dumps(user)
        return Response(dump_data, mimetype="application/json", status=200)


class ProjectsApi(Resource):
    def get(self):
        projects = Project.objects()
        dump_data = projects_schema.dumps(projects)
        return Response(dump_data, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            project = Project(**body, created_by=user).save()
            user.update(push__projects=project)
            user.save()
            return {'id': str(project.id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProjectAlreadyExistsError
        except Exception:
            raise InternalServerError


class ProjectApi(Resource):
    @jwt_required
    def post(self, project_id):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            project = Project.objects.get(id=project_id)
            card = Card(**body, created_by=user, project=project).save()
            project.update(push__cards=card)
            user.update(push__cards=card)
            project.save()
            return {'id': str(card.id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProjectAlreadyExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, project_id):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            project = Project.objects.get(id=project_id, created_by=user_id)
            project.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingProjectError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, project_id):
        try:
            user_id = get_jwt_identity()
            project = Project.objects.get(id=project_id, created_by=user_id)
            project.created_by.update(pull__projects=project)
            for card in project.cards:
                project.created_by.update(pull__cards=card)
            project.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingProjectError
        except Exception:
            raise InternalServerError

    def get(self, project_id):
        try:
            project = Project.objects.get(id=project_id)
            dump_data = project_schema.dumps(project)
            return Response(dump_data, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ProjectNotExistsError
        except Exception:
            raise InternalServerError


class CardApi(Resource):
    @jwt_required
    def post(self, card_id):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            card = Card.objects.get(id=card_id)
            comment = Comment(**body, sender=user)
            card.comments.append(comment)
            card.save()
            return '', 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, card_id):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            card = Card.objects.get(id=card_id, created_by=user_id)
            card.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingCardError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, card_id):
        try:
            user_id = get_jwt_identity()
            card = Card.objects.get(id=card_id, created_by=user_id)
            card.project.update(pull__cards=card)
            card.created_by.update(pull__cards=card)
            card.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingCardError
        except Exception:
            raise InternalServerError

    def get(self, card_id):
        try:
            card = Card.objects.get(id=card_id)
            dump_data = card_schema.dumps(card)
            return Response(dump_data, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CardNotExistsError

