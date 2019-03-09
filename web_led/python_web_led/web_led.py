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

def respond(conn):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send('<h1>Hello, Micropython in a function</h1>\n')

def service_connection(conn):
    request = conn.recv(1024)
    # request = conn.readline()
    print("Request received - in service connection")
    respond(conn)
    conn.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
  s.bind(('', 80))
  s.listen(5)
  while True:
    conn, addr = s.accept()
    service_connection(conn)
finally:
  s.close()
