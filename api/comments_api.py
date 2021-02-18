from flask_restplus import Resource, Namespace
from flask import request
import services.comment_service as comment_service

API = Namespace("page", __name__)


@API.route("/<string:pageId>/comments")
class CommentsApi(Resource):
    def post(self, pageId):
        request_payload = request.get_json()
        response = comment_service.create_comment(request_payload, pageId)
        return response, 200

    def put(self, pageId):
        request_payload = request.get_json()
        response = comment_service.update_comment(request_payload, pageId)
        return response, 200

    def get(self):
        response = comment_service.get_comments()
        return response, 200


@API.route("/<string:pageid>")
class SingleCommentApi(Resource):
    pass
