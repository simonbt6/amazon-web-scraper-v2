from dispatch import Dispatch
from http.server import *
from socket import socket
import socketserver
import json
import asyncio
import asyncio.tasks

from amazon import AmazonScraper

from request import Request

PORT = 9119

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        # Response
        self.send_response(200)

        # Request handling
        self.json = json.loads(self.data_string)

        request = Request(self.json['url'], 0)
        
        asyncio.run(Dispatcher.newRequest(request=request))

Handler = RequestHandler
Dispatcher = Dispatch()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()

