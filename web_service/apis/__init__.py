from flask import Blueprint
from flask_restx import Api
from .user import ns as UserNameSpace

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)
api = Api(
    blueprint,
    title="my project api",
    version='1.0',
    doc='/docs',
    description="welcome my api docs"
)

# TODO: add namespace to Blueprint
api.add_namespace(UserNameSpace)