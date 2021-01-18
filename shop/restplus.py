import logging
import traceback

from faunadb import errors as faunaErrors
from flask_restx import Api

from shop import settings

log = logging.getLogger(__name__)

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    },
}

api = Api(
    version='1.0',
    title='Shop',
    description='A simple demonstration of a FaunaDB Python driver',
    authorizations=authorizations
)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500

@api.errorhandler(faunaErrors.BadRequest)
def fauna_error_handler(e):
    return {'message': e.errors[0].description}, 400

@api.errorhandler(faunaErrors.Unauthorized)
@api.errorhandler(faunaErrors.PermissionDenied)
def fauna_error_handler(e):
    return {'message': "Access forbidden"}, 403
