from framework.wsgi_request import parse_environ
from framework.wsgi_response import get_response


class App:
    def __init__(self):
        self.views = {}
        self.headers = None

    def get_view(self, environ, start_response):
        url = environ['PATH_INFO']
        if not url.endswith('/'):
            self.headers['Location'] = '{}/'.format(url)
            response_tuple = (301, start_response)
            return response_tuple
        else:
            view = self.views.get(str(url))

        method = environ['REQUEST_METHOD']

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
        self.headers = request_headers
        response_tuple = self.get_view(request_headers, start_response)
        response = get_response(response_tuple, self.headers)
        return response
   