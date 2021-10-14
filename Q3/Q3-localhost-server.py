import http.server
import socketserver
import json
from typing import Text

PORT = 8000
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
class MyHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_POST(self):
        # - request -
        content_length = int(self.headers['Content-Length'])
        print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = input_json.decode()
        else:
            input_data = None
            
        print(input_data)
        b = input_data
        test  = toBinary(b)
        # - response -
        print(test)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_data = {'status': 'OK', 'result': test}
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))


Handler = MyHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Starting http://0.0.0.0:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
        print("Stopping by Ctrl+C")
        httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`