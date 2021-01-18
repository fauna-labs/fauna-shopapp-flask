from flask import request
from flask_restx import Resource
from shop.orders import parsers as orderParser
from shop.orders import repository as orderRepository
from shop.orders import serializers as orderSerializer
from shop.restplus import api

ns = api.namespace('orders', description='Operations related to orders')

@ns.route('/')
class Orders(Resource):

    @api.doc(security='apiKey')
    @api.expect(orderParser.list_orders_args)
    @api.marshal_with(orderSerializer.orders_list)
    def get(self):
        """
        Returns list of orders.
        """
        return orderRepository.get_orders(
            secret=request.headers.get("x-access-token"),
            **orderParser.list_orders_args.parse_args(request)
        )

@ns.route('/<order_ref>')
class Order(Resource):

    @api.doc(security='apiKey')
    @api.marshal_with(orderSerializer.order_with_status_history)
    def get(self, order_ref):
        """
        Returns order details with status history
        """
        return orderRepository.find_order(
            secret=request.headers.get("x-access-token"),
            order_ref=order_ref
        )

@ns.route('/<order_ref>/status')
class Order(Resource):

    @api.doc(security='apiKey')
    @api.expect(orderParser.update_status_args)
    @api.marshal_with(orderSerializer.order)
    def put(self, order_ref):
        """
        Returns order details with status history
        """
        return orderRepository.update_status(
            secret=request.headers.get("x-access-token"),
            order_ref=order_ref,
            **orderParser.update_status_args.parse_args(request)
        )

