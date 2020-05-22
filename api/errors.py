# REST API Errors


class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ProjectAlreadyExistsError(Exception):
    pass


class UpdatingProjectError(Exception):
    pass


class DeletingProjectError(Exception):
    pass


class ProjectNotExistsError(Exception):
    pass


class UpdatingCardError(Exception):
    pass


class DeletingCardError(Exception):
    pass


class CardNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
     },
    "ProjectAlreadyExistsError": {
        "message": "Project with given name already exists",
        "status": 400
     },
    "UpdatingProjectError": {
        "message": "You are not authorized to modify this project",
        "status": 403
     },
    "DeletingProjectError": {
        "message": "You are not authorized to delete this project",
        "status": 403
     },
    "ProjectNotExistsError": {
         "message": "Project with given id doesn't exists",
         "status": 400
     },
    "UpdatingCardError": {
        "message": "You are not authorized to modify this card",
        "status": 403
     },
    "DeletingCardError": {
        "message": "You are not authorized to delete this card",
        "status": 403
     },
    "PCardNotExistsError": {
         "message": "Card with given id doesn't exists",
         "status": 400
     },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
     },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
     }
}