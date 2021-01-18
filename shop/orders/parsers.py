from flask_restx import inputs, reqparse
from shop.fauna.parsers import getFaunaCursorRequestParser

update_status_args = reqparse.RequestParser()
update_status_args.add_argument('status', choices=['handed_over_courier', 'delivered'], location="form", required=True)

list_orders_args = getFaunaCursorRequestParser(collection='orders')
