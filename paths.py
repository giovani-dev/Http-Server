from src.server.http.response import Html


route = {
    '/teste': str(Html(html_path='index.html', status='200 OK')),
    '/teste/segundo': str(Html(html_path='index2.html', status='200 OK'))
}