from flask_restplus import Resource, Namespace
from flask import request

API = Namespace("comments", __name__)


@API.route("/")
class CommentsApi(Resource):
    pass
