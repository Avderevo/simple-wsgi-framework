from wsgi_app import App


app = App()


@app.route('/', method=['GET', 'POST'])
def index(headers):
    return 'Home page'


@app.route('/products/')
def products(headers):
    return 'Products'


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()

