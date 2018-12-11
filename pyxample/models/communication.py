import http.client


class Request:
    def __init__(self, method, url, header={}, body=None):
        self.method = method
        self.header = header
        self.body = body
        self.url = url

    def send(self):
        conn = http.client.HTTPConnection("localhost", 5333)
        conn.request(self.method, self.url, self.body, self.header)
        response = conn.getresponse().read()
        conn.close()
        return response


class Response:
    pass