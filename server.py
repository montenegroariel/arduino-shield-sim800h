from BaseHTTPServer import BaseHTTPRequestHandler
from send_message import send_message
from encode import encode_msg, encode_phn
import urlparse, json

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
	phone, number, temperature =  parsed_path.query.split(":")
	message = "El equipo Nro " + number + " ha superado su limite de temperatura registrando " + temperature + ". Por favor verifique su funcionamiento."
	send_message(phone,message)
        self.end_headers()
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        data = json.loads(post_body)

        self.wfile.write(data['foo'])
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('10.91.2.56', 8009), GetHandler)
    print 'Starting server at http://10.91.2.56:8009'
    server.serve_forever()
