import jwt


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
