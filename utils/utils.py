import jwt
from dao.dao import GenericDao


def decode_auth_token(auth_token):
    payload = jwt.decode(auth_token, 'SECRET_KEY')
    return payload['sub']


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
