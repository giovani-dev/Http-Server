from typing import NamedTuple, List
from datetime import datetime


class SlicedUrlRequest(NamedTuple):
    method: str
    endpoint: str
    http_version: str

    def __repr__(self):
        return str(self._asdict())


class SlicedRequestHeader(NamedTuple):
    # start_line: SlicedUrlRequest
    content_type: str
    user_agent: str
    content_length: float

    def __repr__(self):
        return str(self._asdict())


class SlicedRequest(NamedTuple):
    ip_adress: str
    url: SlicedUrlRequest
    body: str
    header: SlicedRequestHeader


class TargetViewRequest(NamedTuple):
    endpoint: str
    methods: List[str]
    view: object
    include: object = ...