
from src.server.http.server import HttpBaseServer
import paths


HttpBaseServer(port=8000, paths=paths.route).serve_forever()