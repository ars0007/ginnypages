import jwt
from flask import request

from dao.dao import GenericDao


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, 'SECRET_KEY', algorithms='HS256')
        return prepare_response(200, body=payload['sub'])
    except jwt.DecodeError:
        return prepare_response(401, error='Token is invalid')
    except jwt.ExpiredSignatureError:
        return prepare_response(401, error='Token expired')


def auth(function):
    def inner_func(*args, **kwargs):
        print("Inner function started")
        print(args)
        authtoken = request.headers['Authorization']
        if authtoken:
            res = decode_auth_token(authtoken)
            if res['error']:
                return res
            else:
                returned_value = function(*args, **kwargs)
                print("Inner function ended")
                return returned_value
        else:
            return prepare_response(404, error="Token not provided")

    return inner_func


def prepare_response(status_code, message=None, body=None, error=None):
    return {
        "statusCode": status_code,
        "message": message,
        "body": body,
        "error": error
    }


def get_user_detials(page_details, comment=False):
    user_id = page_details["user_id"]
    user_details = GenericDao("users").find_one_record(filter_query={"user_id": user_id},
                                                       projection={"_id": 0})
    response = {}
    if comment:
        response["comment"] = page_details["comment"]
    else:
        response["content"] = page_details["content"]
    user_data = {}
    user_data["email"] = user_details["email"]
    user_data["fullname"] = user_details["firstname"] + " " + user_details["lastname"]
    response["user"] = user_data
    return response
