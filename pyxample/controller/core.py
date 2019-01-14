from pyxample.models import *
import json

valid_methods = ["PUT", "POST", "GET", "DELETE"]


def connect(ip="localhost", port=5333):
    set_server(ip, port)


def send_request(method, key, headers={}, body=None):
    if method not in valid_methods:
        raise Exception

    r = Request(method, "/" + key, headers, body)
    response = r.send()

    return response


def send_bulk_request(operations):
    ops = {"operatioons": operations}

    body = json.dumps(ops)
    r = Request("POST", "/bulk/", {"Content-Type": "application/json"}, body)
    response = r.send()

    return response
