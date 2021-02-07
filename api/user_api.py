from flask_restplus import Resource, Namespace

API = Namespace("users", __name__)

API.route("/")


class UsersApi(Resource):
    def get(self):
        return "get", 200

    def post(self):
        pass
