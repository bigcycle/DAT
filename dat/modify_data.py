# -*- coding:utf-8 -*-


def modify_data(col):
    col = col.replace('(', '')
    col = col.replace(')', ' ')
    col = col.replace('"J42 DCM', 'J42 DCM')
    col = col.replace(':', '')
    col = col.replace('.0', '')
    return col


def modify_header(headers):
    _headers = []
    for header in headers:
        header = ''.join(header.split())
        header = header.replace('.', '_')
        header = header.replace('/', "_")
        header = header.replace('-', "_")
        header = header.replace('(', "_")
        header = header.replace(')', "_")
        _headers.append(header)
    return _headers
