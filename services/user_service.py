import datetime
from uuid import uuid4
from dao.dao import GenericDao
from passlib.hash import pbkdf2_sha256
import jwt


def hash_password(password):
    hashed_password = pbkdf2_sha256.hash(password)
    return hashed_password


def verify_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)


def prepare_response(status_code, message=None, body=None, error=None):
    return {
        "statusCode": status_code,
        "message": message,
        "body": body,
        "error": error
    }


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }

    return jwt.encode(
        payload,
        'SECRET_KEY',
        algorithm='HS256'
    )


def decode_auth_token(auth_token):
    payload = jwt.decode(auth_token, 'SECRET_KEY')
    return payload['sub']


def user_create(user_payload):
    user_payload["user_id"] = str(uuid4())
    hashed_password = hash_password(user_payload["password"])
    user_payload["password"] = hashed_password
    GenericDao_obj = GenericDao("users")
    res = GenericDao_obj.insert_record(user_payload)
    if res:
        return prepare_response(201, message="success")
    else:
        return prepare_response(500, error="failure")


def user_update(payload, user_id):
    hashed_password = hash_password(payload["password"])
    payload["password"] = hashed_password
    payload["user_id"] = user_id
    GenericDao_object = GenericDao("users")
    response = GenericDao_object.update_record(payload, filter_query={"user_id": user_id})
    if response:
        return prepare_response(201, message="success")
    else:
        return prepare_response(500, error="failure")


def user_signin(payload):
    email = payload["email"]
    password = payload["password"]
    GenericDao_object = GenericDao("users")
    res = GenericDao_object.find_one_record(filter_query={"email": email}, projection={"_id": 0})
    if res:
        match = verify_password(password, res["password"])
        if match:
            token = encode_auth_token(res["user_id"])
            return prepare_response(201, message="Successfully logged in", body=token)
        else:
            return prepare_response(500, message="wrong email or password")
    else:
        return prepare_response(404, error="user not found")
