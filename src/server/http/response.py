import conf
from errors import HttpInternalServerError


class Html(object):
    def __init__(self, html_path, status):
        self.response = self.make_response(path=html_path, status=status)

    def __str__(self):
        return self.response

    def make_response(self, path: str, status: str):
        try:
            with open(path) as html:
                return f'HTTP/1.0 {status}\nContent-Type: {conf.TYPE}; charset={conf.CHARSET}\n\n{html.read()}'
        except Exception:
            raise HttpInternalServerError()