from faunadb import objects
from flask_restx import fields
from shop.restplus import api


class FaunaRef(fields.StringMixin, fields.Raw):
    def format(self, value):
        return value.id()

class FaunaTime(fields.StringMixin, fields.Raw):
    def format(self, value):
        return value.value

class FaunaCursor(fields.StringMixin, fields.Raw):
    def format(self, value):
        if isinstance(value, objects.Ref):
            return 'cursor_ref=' + value.id()
        else:
            return value

faunaPagination = api.model('Pagination', {
    "after": fields.List(FaunaCursor, readOnly=True, description='Cursor after'),
    "before": fields.List(FaunaCursor, readOnly=True, description='Cursor before')
})
