from requests import parse_environ
from responses import get_response


class App:
    def __init__(self):
        self.views = {}

    def get_view(self, environ, start_response):
        url = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        view = self.views.get(str(url))
        if not view:
            response_tuple = (404, start_response)
        elif method not in view['method']:
            response_tuple = (505, start_response)
        else:
            response_tuple = (200, view['func'], start_response)
        return response_tuple

    def route(self, url, method=['GET']):
        def decorate(view):
            self.views[url] = {'method': method, 'func': view}
        return decorate

    def __call__(self, environ, start_response):
        request_headers = parse_environ(environ)
        response_tuple = self.get_view(request_headers, start_response)
        response = get_response(response_tuple, request_headers)
        return response


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

