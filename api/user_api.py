from flask_restplus import Resource, Namespace
from flask import request
import services.user_service as user_service

API = Namespace("users", __name__)


@API.route("/")
class UsersApi(Resource):
    def post(self):
        request_payload = request.get_json()
        response = user_service.user_create(request_payload)
        return response, 200


@API.route("/<string:username>")
class SingleUserApi(Resource):
    def delete(self, username):
        response = user_service.user_delete(username)
        return response, 200

    def put(self, username):
        request_payload = request.get_json()
        response = user_service.user_update(request_payload, username)
        return response, 200


@API.route("/signin")
class SignIn(Resource):
    def post(self):
        request_payload = request.get_json()
        response = user_service.user_signin(request_payload)
        return response, 200
