import conf


class HttpBaseError(Exception):
    def __init__(self):
        self.message = str()
        super().__init__()

    def __str__(self):
        return self.message


class HttpNotFound(HttpBaseError):
    def __init__(self, message: str = str()):
        super(HttpNotFound, self).__init__()
        self.message = f'HTTP/1.0 404 Not Found\nContent-Type: {conf.TYPE}; charset=utf-8\n\n{message}'


class HttpInternalServerError(HttpBaseError):
    def __init__(self, message: str = str()):
        super(HttpInternalServerError, self).__init__()
        self.message = f'HTTP/1.0 500 Internal Server Error\nContent-Type: {conf.TYPE}; charset=utf-8\n\n{message}'