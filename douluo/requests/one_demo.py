import requests
import chardet
import traceback


def downloader(url, timeout=5, headers=None, debug=False, binary=False):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }

    redirected_url = url

    if headers:
        _headers = headers
    
    try:
        r = requests.get(url, headers=_headers, timeout=timeout)
        if binary:
            return r.content
        else:
            encoding = chardet.detect(r.content)['encoding']
            encoding = 'gb18030' if encoding.lower() == 'gb2312' else encoding
            html = r.content.decode(encoding)

        status = r.status_code
        redirected_url = r.url
    except:
        if debug:
            traceback.print_exc()
        msg = 'Failed to download url: {}'.format(url)
        print(msg)
        if binary:
            html = b''
        else:
            html = ''
        status = 0
    return status, html, redirected_url
