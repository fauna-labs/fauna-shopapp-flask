from flask_restx import fields
from shop.restplus import api

token = api.model('Tokens', {
    'access_token': fields.String(readOnly=True, description='Access token')
})
