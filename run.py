import http.server
import socketserver


PORT = 8001


class AppRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'picard_talk.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


my_server = socketserver.TCPServer(("", PORT), AppRequestHandler)

my_server.serve_forever()
