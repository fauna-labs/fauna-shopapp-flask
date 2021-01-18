from flask_restx import fields
from shop.restplus import api


class FaunaRef(fields.StringMixin, fields.Raw):
    def format(self, value):
        return value.id()

class FaunaTime(fields.StringMixin, fields.Raw):
    def format(self, value):
        return value.value

faunaPagination = api.model('Pagination', {
    "after": fields.String(readOnly=True, description='Cursor after'),
    "before": fields.String(readOnly=True, description='Cursor before')
})
