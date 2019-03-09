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

def process():
    a = 0
    while True:
        if a % 100 == 0:
          print(a)
        yield
        a += 1

def service_connection(conn, addr):
    request = conn.recv(1024)
    print("Request received")
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send('<h1>Hello, Micropython</h1>\n')
    conn.close()

print("Preparing socket and process")
p = process()
s = socket.socket()
try:
  print("Trying bind")
  s.bind(('0.0.0.0', 80))
  s.settimeout(0.1)

  s.listen(5)
  print("Start main loop")
  while True:
    try:
      detail = s.accept()
      if detail:
          service_connection(*detail)
    except OSError:
      pass
    next(p)
finally:
  s.close()
