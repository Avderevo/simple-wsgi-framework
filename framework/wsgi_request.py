

def parse_environ(environ):
    request_headers = {}
    request_headers['CONTENT_TYPE'] = get_content(environ)
    nid_headers = ['REQUEST_METHOD',
                   'PATH_INFO', 'REMOTE_ADDR',
                   'REMOTE_HOST',
                   'CONTENT_LENGTH',
                   'CONTENT_TYPE'
                   ]

    for k, v in environ.items():
        if k.upper() in nid_headers or k.startswith('WSGI') or k.startswith('HTTP'):
            request_headers[k] = v
    request_headers['CONTENT_TYPE'] = get_content(request_headers)

    return request_headers


def get_content(environ):
    content_type = environ.get('CONTENT_TYPE')

    if not content_type or len(str(content_type)) == 0:
        content_type = 'text/html'
    
    return content_type

        
