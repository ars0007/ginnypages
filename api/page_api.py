from flask_restplus import Resource, Namespace
from flask import request
import services.page_service as page_service

API = Namespace("pages", __name__)


@API.route("/")
class PagesApi(Resource):
    def post(self):
        request_payload = request.get_json()
        response = page_service.create_page(request_payload)
        return response, 200


@API.route("/<string:pageid>")
class SinglePageApi(Resource):
    def put(self, pageid):
        request_payload = request.get_json()
        response = page_service.update_page(request_payload, pageid)
        return response, 200

    def get(self, pageid):
        response = page_service.get_page(pageid)
        return response, 200

    def delete(self, pageid):
        response = page_service.delete_page(pageid)
        return response, 200
