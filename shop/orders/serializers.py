from flask_restx import fields
from shop.fauna.serializers import FaunaRef, FaunaTime, faunaPagination
from shop.restplus import api

order = api.model('Order', {
    'ref': FaunaRef(readOnly=True, description='The unique identifier of order'),
    'cutomer': FaunaRef(attribute='data.customer', required=True, description='Customer identifier'),
    'product': FaunaRef(attribute='data.product', required=True, description='Product identifier'),
    'status': fields.String(attribute='data.status', required=True, description='Current status'),
    'statusAt': FaunaTime(attribute='data.statusAt', required=True, description='Time when status applied'),
})

order_status_history = api.model('Order status history', {
    'status': fields.String,
    'statusAt': FaunaTime
})

order_with_status_history = api.inherit('Order with status history', order, {
    'status_history': fields.List(fields.Nested(order_status_history), attribute='data.status_history')
})

orders_list = api.inherit('Orders lists', faunaPagination, {
    'data': fields.List(fields.Nested(order))
})
