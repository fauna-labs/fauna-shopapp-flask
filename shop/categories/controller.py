from flask import request
from flask_restx import Resource
from shop.categories import parsers as categoryParser
from shop.categories import repository as categoryRepository
from shop.categories import serializers as categorySerializer
from shop.restplus import api

ns = api.namespace('categories', description='Operations related to categories')

@ns.route('/')
class Categories(Resource):

    @api.expect(categoryParser.list_categories_args)
    @api.marshal_with(categorySerializer.categories_list)
    def get(self):
        """
        Returns list of categories.
        """
        return categoryRepository.get_categories(categoryParser.list_categories_args.parse_args(request))
