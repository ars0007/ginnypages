from flask import Flask
from flask_restplus import Resource, Api
from api.user_api import API as USERS_API
from api.page_api import API as PAGES_API
from api.comments_api import API as COMMENTS_API

APP = Flask(__name__)
API = Api(APP, prefix="/api")
API.add_namespace(USERS_API)
API.add_namespace(PAGES_API)
API.add_namespace(COMMENTS_API)

if __name__ == '__main__':
    APP.run()
