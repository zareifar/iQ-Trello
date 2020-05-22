# REST API Routes

from .views import ProjectsApi, ProjectApi, CardApi, UserApi
from .auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(UserApi, '/api/profile')
    api.add_resource(ProjectsApi, '/api/projects')
    api.add_resource(ProjectApi, '/api/projects/<project_id>')
    api.add_resource(CardApi, '/api/cards/<card_id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
