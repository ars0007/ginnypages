from flask_restplus import Resource, Namespace
from flask import request
import services.comment_service as comment_service
from utils.utils import auth

API = Namespace("page", __name__)


@API.route("/<string:pageId>/comments")
class CommentsApi(Resource):
    @auth
    def post(self, pageId):
        request_payload = request.get_json()
        response = comment_service.create_comment(request_payload, pageId)
        return response, 200

    @auth
    def put(self, pageId):
        request_payload = request.get_json()
        response = comment_service.update_comment(request_payload, pageId)
        return response, 200

    def get(self, pageId):
        response = comment_service.get_comments(pageId)
        return response, 200


@API.route("/comment/<string:commentId>")
class SingleCommentApi(Resource):
    @auth
    def delete(self, commentId):
        response = comment_service.delete_comment(commentId)
        return response, 200
