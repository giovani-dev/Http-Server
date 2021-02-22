from typing import List, NamedTuple
from abc import ABC, abstractmethod
from errors import HttpNotFound
import re


class RequestParser(object):
    def __init__(self, request):
        self.request_text = request
        print(request)
        self.start_line = re.findall(r"(POST|GET|PUT|DELETE|OPTIONS|HEAD|PATCH)+(.+)", request)
        print(self.start_line)
        self.start_line = self.start_line[0]

    def body(self):
        return self.request_text.split("\r\n\r\n")[-1].replace("\n", "").replace("\r", "")

    def method(self):
        return self.start_line[0]

    def path(self):
        path = self.start_line[1].split(" ")
        path = list(filter(None, path))
        return path[0]


class BaseRequest(ABC):

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    def base(self, *args, **kwargs): ...


class Path(BaseRequest):
    
    def __init__(self, local: dict = dict(), *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)
        self.local = local

    @property
    def base(self):
        return self.local

    @base.setter
    def base(self, values):
        if isinstance(values, dict): 
            self._local = values
        else:
            raise 

    def route(self, path):
        try:
            return self.local[path]
        except KeyError:
            raise HttpNotFound()


if __name__ == '__main__':
    # Path(request='Giovani')
    route = {
        '/teste/usuario/cadastro': '<h1>Cadastro de Usuario</h1>',
        '/teste/usuario': '<h1>Funcionalidade de usuario</h1>',
        '/teste': '<h1>Teste</h1>',
    }
    x = Path(local=route)
    y = x.route('/')
    print(y)