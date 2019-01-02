import http.client

IP = "localhost"
PORT = 5333


def set_server(ip="localhost", port=5333):
    global IP
    global PORT
    IP = ip
    PORT = port


class Request:

    def __init__(self, method, url, header={}, body=None):
        self.method = method
        self.header = header
        self.body = body
        self.url = url
        if body:
            self.header['Content-Length'] = len(self.body.encode('utf-8'))
        else:
            self.header['Content-Length'] = 0

    def send(self):
        conn = http.client.HTTPConnection(IP, PORT)
        conn.request(self.method, self.url, self.body, self.header)
        response = conn.getresponse().read()
        conn.close()
        return response


class Response:
    pass
