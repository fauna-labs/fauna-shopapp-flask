from flask_restx import fields
from shop.fauna.serializers import FaunaRef, faunaPagination
from shop.restplus import api

category = api.model('Category', {
    'ref': FaunaRef(readOnly=True, description='The unique identifier product'), #TBD
    'name': fields.String(attribute='data.name', required=True, description='Product name'),
})

categories_list = api.inherit('Categories lists', faunaPagination, {
    'data': fields.List(fields.Nested(category))
})
