from connect import connect
print("Connecting")
connect()
print("Connected")
del connect
print("Setting up")

try:
  import usocket as socket
except:
  import socket

import gc
gc.collect()

def respond_html(conn, text):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send(text)
    conn.send('\n')

def service_connection(conn):
    data = conn.recv(1024).decode('utf-8')
    # print(repr(data))
    request = data.split('\n',1)
    request_line = request[0]
    # request_line = conn.readline().decode('utf-8')
    print("Request received", request_line)
    method, uri, _ = request_line.split()
    if uri.endswith('/static/foo'):
        respond_html(conn, "<h1>Foo</h1>")
    else:
        print("Sent default hello")
        with open('index.html') as fd:
            respond_html(conn, fd.read())

    conn.close()


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
  print("Trying bind")
  s.bind(('', 80))
  s.settimeout(0.1)

  s.listen(5)
  print("Start main loop")
  while True:
    try:
      conn, addr = s.accept()
      print("accepted connection")
      service_connection(conn)
    except OSError as e:
        if e.args[0] != 110:
            raise
finally:
  s.close()
