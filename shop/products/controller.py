import logging

from faunadb import errors as faunaErrors
from flask import request
from flask_restx import Resource
from shop.orders import serializers as orderSerializer
from shop.products import parsers as productParser
from shop.products import repository as productRepository
from shop.products import serializers as productSerializer
from shop.restplus import api
from werkzeug.exceptions import BadRequest

log = logging.getLogger(__name__)

ns = api.namespace('products', description='Operations related to products')


@ns.route('/')
class Products(Resource):

    @api.expect(productParser.list_products_args)
    @api.marshal_with(productSerializer.product_list)
    def get(self):
        """
        Returns list of products.
        """
        resp = productRepository.get_products(**productParser.list_products_args.parse_args(request))
        print(resp)
        return resp

    @api.expect(productParser.create_product_args)
    @api.marshal_with(productSerializer.product)
    @api.doc(security='apiKey')
    def post(self):
        """
        Create new product.
        """
        return productRepository.create_product(
            **productParser.create_product_args.parse_args(request),
            secret=request.headers.get("x-access-token")
        )
               

@ns.route('/<product_ref>')
class Product(Resource):

    @api.marshal_with(productSerializer.product)
    def get(self, product_ref):
        """
        Return product details.
        """
        return productRepository.find_product(product_ref)

    @api.expect(productParser.update_product_args)
    @api.marshal_with(productSerializer.product)
    @api.doc(security='apiKey')
    def put(self, product_ref):
        """
        Update existing product.
        """
        return productRepository.update_product(
            secret=request.headers.get("x-access-token"),
            ref=product_ref,
            data=productParser.update_product_args.parse_args(request)
        )

@ns.route('/<product_ref>/purchase')
class ProductPurchase(Resource):
    @api.marshal_with(orderSerializer.order)
    @api.doc(security='apiKey')
    def post(self, product_ref):
        """
        Purchase product.
        """
        return productRepository.purchase(
            secret=request.headers.get("x-access-token"),
            product_ref=product_ref
        )
        
