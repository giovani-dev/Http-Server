from typing import List, NamedTuple
from .
import re


class HttpRequest(object):
    def __init__(self):
        self.params = object()

    def __dict__(self):
        return self.params._asdict()

    @staticmethod
    def parse(request_text, client):
        ext_body = request_text.split("\r\n\r\n")[-1].replace("\n", "").replace("\r", "")
        ext_start_line = re.findall("(POST|GET|PUT|DELETE|OPTIONS|HEAD|PATCH)+(.+)", request_text)[0]
        ext_content_type = re.findall(r"Content-Type+.+", request_text)[0].split(' ')[-1].replace("\r", "").replace("\n", "")
        ext_content_length = re.findall(r"Content-Length+.+", request_text)[0].split(' ')[-1].replace("\r", "").replace("\n", "")
        ext_content_length = float(ext_content_length)
        ext_user_agent = re.findall(r"User-Agent+.+", request_text)[0].split(' ')[-1].replace("\r", "").replace("\n", "")

        line = ext_start_line[-1].replace("\r", "").replace("\n", "").split(" ")
        line = list(filter(None, line))
        ext_url = SlicedUrlRequest(method=ext_start_line[0], endpoint=line[0], http_version=line[-1])

        header = SlicedRequestHeader(content_type=ext_content_type, content_length=ext_content_length, user_agent=ext_user_agent)
        return SlicedRequest(ip_adress=client[0], body=ext_body, header=header, url=ext_url)