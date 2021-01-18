from flask_restx import fields
from shop.fauna.serializers import FaunaRef, FaunaTime, faunaPagination
from shop.restplus import api

product = api.model('Product', {
    'ref': FaunaRef(readOnly=True, description='The unique identifier product'), #TBD
    'name': fields.String(attribute='data.name', required=True, description='Product name'),
    'price': fields.Integer(attribute='data.price', required=True, description='Product price'),
    'quantity': fields.Integer(attribute='data.quantity', required=True, description='How many prodacts available'),
    'createdAt': FaunaTime(attribute='data.createdAt', required=True, description='Time when product created'),
    'categories': fields.List(FaunaRef, attribute="data.categories")
})

product_list = api.inherit('Product lists', faunaPagination, {
    'data': fields.List(fields.Nested(product))
})
