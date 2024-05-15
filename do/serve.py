import os.path
import socketserver
from http.server import SimpleHTTPRequestHandler, HTTPServer

def serve_directory(path, port=8000):
    class ConfiguredHandler(HTTPDirectoryRequestHandler):
        SERVED_DIRECTORY = path
        
    httpd = ThreadingHTTPServer(("", port), ConfiguredHandler)
    print("serving on port", port)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt():
        httpd.server_close()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass

class HTTPDirectoryRequestHandler(SimpleHTTPRequestHandler):
    SERVED_DIRECTORY = '.'

    def translate_path(self, path):
        path = super().translate_path(path)
        relpath = os.path.relpath(path)
        full_path =  os.path.join(self.SERVED_DIRECTORY, relpath)
        print("full_path", full_path)
        return full_path

serve_directory('.')
