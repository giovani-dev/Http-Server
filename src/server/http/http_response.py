



class HttpResponse(object):
    def __init__(self, _type, status_code, status_message, body_text):
        self.type = _type
        self.status_code = status_code
        self.status_message = status_message
        self.body_text = body_text
        self.server_name = "Giovani`s http server" 

    def __str__(self):
        date = self.date()
        return f"HTTP/1.0 {self.status_code} {self.status_message}\nContent-Type: {self._type}\ncontent-length: {getsizeof(self.body_text)}\nServer: {self.server_name}\nDate: {self.date()}\n\n{self.body_text}"

    def date(self) -> Any:
        repr_date = DateRepresentation()
        date = datetime.now()
        day_week_number = date.weekday()
        day_week_name = repr_date.day_name[day_week_number]
        month_name = repr_date.month_name[date.month]

        return f"{day_week_name}, {day_week_number} {month_name} {date.hour}:{date.minute}:{date.second}"

    def error(self):
        


class Response(object):
    def __init__(self): ...

    def __str__(self):
        return str( HttpResponse(_type=, status=, body=) )
