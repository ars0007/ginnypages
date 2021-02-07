from flask import Flask
from flask_restplus import Resource, Api
from api.user_api import API as USERS_API

APP = Flask(__name__)
API = Api(APP, prefix="/api")
API.add_namespace(USERS_API)

if __name__ == '__main__':
    APP.run()
