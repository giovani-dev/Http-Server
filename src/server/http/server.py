import os, sys
sys.path.append("/Users/Pichau/Documents/projects/Http-Server/src/server/http")

import socket
import logging
import threading
import conf
from random import randint
from request import RequestParser, Path
from errors import HttpBaseError
from datetime import datetime


class SocketServer(object):

    @staticmethod
    def http(port, host='0.0.0.0'):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        return server_socket

class HttpBaseServer:
    def __init__(self, port, paths):
        self.socket = SocketServer.http(port=port)
        self.path = Path(local=paths)
        print(f"[{datetime.now()}] STARTED SERVER")
  

    def serve_forever(self) -> None:
        while True:
            try:
                client_connection, client_address = self.socket.accept()
                print(f"[{datetime.now()}] CONNECTION RECEIVED FROM {client_address[0]}")
                request = client_connection.recv(1024).decode()
                response = self.route(request=request)
                client_connection.sendall(response.encode())
                threading.Thread(target=client_connection.close, args=()).start()
            except KeyboardInterrupt:
                self.socket.close()
                break
        print(f"[{datetime.now()}] CLOSED SERVER")

    def route(self, request) -> None:
        parser = RequestParser(request=request)
        request_path = parser.path()
        try:
            return self.path.route(request_path)
        except HttpBaseError as e:
            return str(e)


if __name__=='__main__':
    route = {
        '/teste': str(Html(html_path='../../test/index.html', status='200 OK'))
    }
    HttpBaseServer(port=8000, paths=route).serve_forever()
    # server = HttpServer(8000).serve_forever()
    # html_server = HtmlServe(8000).html('../../test/index.html').serve_forever()