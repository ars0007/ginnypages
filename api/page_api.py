from flask_restplus import Resource, Namespace
from flask import request

API = Namespace("pages", __name__)


@API.route("/")
class PagesApi(Resource):
    pass
