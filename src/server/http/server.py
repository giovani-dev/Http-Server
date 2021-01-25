from http_request import HttpRequest
from conf_socket import SocketServer

class MethodNotAllowed(Exception):
    def __init__(self):
        self.message = "405 Method Not Allowed"
        super().__init__()

    def __str__(self):
        return self.message


class HttpValidation(object):

    def __init__(self):
        self.avaible_methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATH', 'HEAD']

    def methods(self, received_method):
        if not received_method in self.avaible_methods:
            raise MethodNotAllowed


class HttpServer(object):
    def __init__(self, port):
        self.socket = SocketServer.http(port=port)
        self._request = object()
        self._response = object()

    def main(self):
        custom_json = "{'id': 1}"

        while True:    
            client_connection, client_address = self.socket.accept()
            request = client_connection.recv(1024).decode()
            response = f"HTTP/1.0 200 OK\nContent-Type: application/json\n\n{custom_json}\n"
            self._request = HttpRequest.parse(request_text=request, client=client_address)
            print(request_params._asdict())
            client_connection.sendall(response.encode())
            client_connection.close()
        self.server_socket.close()



if __name__=='__main__':
    server = HttpServer(8000).main()