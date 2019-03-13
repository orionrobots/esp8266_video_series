from connect import connect
try:
  import usocket as socket
except:
  import socket

def respond_html(conn, text):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send(text)
    conn.send('\n')

def serve_file(conn, filename):
    with open(filename) as fd:
        respond_html(conn, fd.read())

def service_connection(routes, conn):
    data = conn.recv(1024).decode('utf-8')
    # print(repr(data))
    request = data.split('\n',1)
    request_line = request[0]
    print("Request received", request_line)
    method, uri, _ = request_line.split()
    params = []
    if '?' in uri:
        uri, params = uri.split('?')
    if routes.get(uri):
        routes[uri](conn)

    conn.close()

def start_server(routes, async_function=None):
    print("Connecting")
    connect()
    print("Connected")
    print("Setting up")

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
                service_connection(routes, conn)
            except OSError as e:
                if e.args[0] != 110:
                    raise
            if async_function:
                async_function()
    finally:
        s.close()
