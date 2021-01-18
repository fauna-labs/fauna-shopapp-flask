from flask_restx import inputs, reqparse

update_status_args = reqparse.RequestParser()
update_status_args.add_argument('status', choices=['handed_over_courier', 'delivered'], location="form", required=True)
