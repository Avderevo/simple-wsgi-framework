import http.client


def get_response(response_tuple, headers):
    if len(response_tuple) > 2:
        response = good_response(response_tuple, headers)
    else:
        response = bad_response(response_tuple, headers)

    return response


def good_response(response_tuple, headers):
    raw_code, func, start_response = response_tuple
    code, response_headers = get_args_start_response(raw_code, headers)
    start_response(code, response_headers)
    response = func(headers)
    return [response.encode('utf-8')]


def bad_response(response_tuple, headers):
    raw_code, start_response = response_tuple
    code, response_headers = get_args_start_response(raw_code, headers)
    start_response(code, response_headers)
    response = '{}' .format(code)
    return [response.encode('utf-8')]


def get_args_start_response(code, headers):
    code = "{} {}" .format(code, http.client.responses[code])
    response_headers = [(k, v) for k, v in headers.items()]
    return code, response_headers
