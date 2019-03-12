from serve import respond_html, serve_file, start_server


def main():
    routes = {
        '/': lambda conn: serve_file(conn, 'index.html'),
        '/foo': lambda conn: respond_html('conn', '<h1>Foo</h1>'),
        '/bar': lambda conn: respond_html('conn', '<h1>Bar</h1>'),
    }
    start_server(routes)


if __name__ == "__main__":
    main()
