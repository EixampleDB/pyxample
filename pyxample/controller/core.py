from pyxample.models import *

valid_methods = ["PUT", "POST", "GET", "DELETE"]


def send_request(method, key, headers={}, body=None):
    if method not in valid_methods:
        raise Exception

    r = Request(method, "/" + key, headers, body)
    response = r.send()

    return response

