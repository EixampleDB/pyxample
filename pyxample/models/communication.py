import http.client


class Request:
    def __init__(self, method, url, headers={}, body=None):
        self.method = method
        self.headers = headers
        self.body = body
        self.url = url

    def send(self):
        conn = http.client.HTTPConnection("localhost", 5333)
        conn.request(self.method, self.url, self.body, self.headers)
        response = conn.getresponse().read()
        conn.close()
        return response


class Response:
    pass