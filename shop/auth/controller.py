from flask import request
from flask_restx import Resource
from shop.auth import parsers as authParsers
from shop.auth import repository as authRepository
from shop.auth import serializers as authSerializers
from shop.restplus import api

ns = api.namespace('auth', description='Operations related to authorization')

@ns.route('/login')
class Login(Resource):

    @api.expect(authParsers.login_args)
    @api.marshal_with(authSerializers.token)
    def post(self):
        """
        Exchange credentials to access token
        """
        credentials = authParsers.login_args.parse_args(request)
        response = authRepository.login(credentials.get('email'), credentials.get('password'))
        return {"access_token": response.get("secret")}
        
